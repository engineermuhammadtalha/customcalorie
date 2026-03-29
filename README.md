# 🍽️ CustomCalorie
> **Snap it. Know it. Own it.**
> Upload any food photo and instantly get calories, nutrition facts, health score and tips — powered by Google Gemini AI Vision.

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.110-green?logo=fastapi)
![Gemini](https://img.shields.io/badge/Google%20Gemini-1.5%20Flash-orange?logo=google)
![License](https://img.shields.io/badge/License-MIT-yellow)
![Deploy](https://img.shields.io/badge/Deploy-Render-purple?logo=render)

🌐 **Live:** [customcalorie.com](https://customcalorie.com)

---

## ✨ Features
- 📸 Upload any food photo
- 🔢 Instant calorie estimation
- 💪 Protein, carbs & fats breakdown
- 🏆 Health score (1–10)
- 💡 Personalized health tips
- ⚡ Powered by Gemini 1.5 Flash Vision AI

---

## 🚀 Run Locally

### Step 1 — Add your API key
Open `.env` and replace `YOUR_API_KEY` with your key from [aistudio.google.com](https://aistudio.google.com)

### Step 2 — Setup (run once)
**Windows:** Double-click `setup.bat`

### Step 3 — Start
**Windows:** Double-click `start_app.bat`

### Step 4 — Open
Go to: http://127.0.0.1:8000

---

## ☁️ Deploy on Render (Free)
1. Push repo to GitHub
2. Go to [render.com](https://render.com) → New Web Service → Connect repo
3. Add environment variable: `GOOGLE_API_KEY` = your real key
4. Click Deploy ✅

---

## 📁 Structure
```
customcalorie/
├── main.py              ← FastAPI backend
├── static/index.html    ← Frontend UI
├── requirements.txt     ← Dependencies
├── render.yaml          ← Render config
├── setup.bat            ← Windows setup
├── start_app.bat        ← Windows start
├── .env                 ← API Key (never pushed)
└── .gitignore
```

---

## 🛠️ Tech Stack
| Layer | Technology |
|---|---|
| Backend | FastAPI + Python |
| AI | Google Gemini 1.5 Flash |
| Frontend | HTML / CSS / JS |
| Hosting | Render (Free) |
| Domain | customcalorie.com |

---

⭐ Star this repo if you found it useful!
