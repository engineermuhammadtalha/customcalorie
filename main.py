import os
import base64
import json
import requests
from fastapi import FastAPI, UploadFile, File
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, JSONResponse
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def home():
    with open("static/index.html") as f:
        return f.read()

@app.get("/health")
async def health():
    return {"status": "ok", "api_key_set": bool(os.getenv("GOOGLE_API_KEY"))}

@app.post("/analyze")
async def analyze(file: UploadFile = File(...)):
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key or api_key == "YOUR_API_KEY":
        return JSONResponse(status_code=400, content={"error": "API Key missing."})
    try:
        image_data = await file.read()
        image_base64 = base64.b64encode(image_data).decode()

        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent?key={api_key}"

        payload = {
            "contents": [{
                "parts": [
                    {"text": """Look at this food image and respond ONLY with this exact JSON, no extra text:
{
  "food_name": "name of the food",
  "description": "brief description",
  "calories": "estimated calories per serving",
  "protein": "protein in grams",
  "carbs": "carbs in grams",
  "fats": "fats in grams",
  "health_score": 7,
  "is_healthy": true,
  "health_tips": ["tip 1", "tip 2", "tip 3"]
}"""},
                    {"inline_data": {"mime_type": file.content_type, "data": image_base64}}
                ]
            }]
        }

        response = requests.post(url, json=payload, timeout=30)
        result = response.json()

        # Show full error if something went wrong
        if "error" in result:
            return JSONResponse(status_code=400, content={"error": result["error"].get("message", str(result["error"]))})

        if "candidates" not in result:
            return JSONResponse(status_code=500, content={"error": f"Unexpected response: {json.dumps(result)[:200]}"})

        text = result["candidates"][0]["content"]["parts"][0]["text"].strip()
        if "```json" in text:
            text = text.split("```json")[1].split("```")[0].strip()
        elif "```" in text:
            text = text.split("```")[1].split("```")[0].strip()

        return JSONResponse(json.loads(text))

    except Exception as e:
        print(f"ERROR: {str(e)}")
        return JSONResponse(status_code=500, content={"error": str(e)})