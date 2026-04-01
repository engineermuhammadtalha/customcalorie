# 🍽️ CustomCalorie — AI-Powered Nutrition Analyzer

<div align="center">

![CustomCalorie Banner](https://img.shields.io/badge/CustomCalorie-AI%20Nutrition%20Analyzer-brightgreen?style=for-the-badge&logo=google&logoColor=white)

[![Live Demo](https://img.shields.io/badge/🚀%20Live%20Demo-customcalorie.hf.space-green?style=for-the-badge)](https://engineermuhammadtalha-custom-calorie.hf.space)
[![Hugging Face](https://img.shields.io/badge/Hosted%20on-Hugging%20Face-yellow?style=for-the-badge&logo=huggingface)](https://huggingface.co/spaces/engineermuhammadtalha/custom-calorie)
[![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.110-teal?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com)
[![Gemini AI](https://img.shields.io/badge/Powered%20by-Gemini%20AI-orange?style=for-the-badge&logo=google)](https://aistudio.google.com)

**Snap it. Know it. Own it.**

*Upload any food photo and instantly get calories, macros, health score and tips — powered by Google Gemini AI vision.*

</div>

---

## ✨ Features

- 📸 **Photo Upload** — drag & drop or click to upload any food image
- 🔥 **Calorie Estimation** — accurate per-serving calorie count
- 💪 **Macro Breakdown** — protein, carbs and fats in grams
- ⚡ **Health Score** — 1-10 rating with healthy/unhealthy badge
- 💡 **Health Tips** — personalized nutrition advice
- 🌙 **Beautiful Dark UI** — modern, responsive design
- ⚡ **Instant Results** — analysis in under 3 seconds

---

## 🚀 Live Demo

👉 **[https://engineermuhammadtalha-custom-calorie.hf.space](https://engineermuhammadtalha-custom-calorie.hf.space)**

Try it with any food photo — pizza, biryani, salad, burger, anything!

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | FastAPI (Python 3.11) |
| AI Model | Google Gemini 2.5 Flash Vision |
| Frontend | Vanilla HTML/CSS/JS |
| Hosting | Hugging Face Spaces (Docker) |
| Domain | customcalorie.com |

---

## 📦 Local Setup

```bash
# 1. Clone the repo
git clone https://github.com/engineermuhammadtalha/customcalorie.git
cd customcalorie

# 2. Install dependencies
pip install -r requirements.txt

# 3. Add your API key
echo "GOOGLE_API_KEY=your_key_here" > .env

# 4. Run the app
uvicorn main:app --reload
```

Open [http://localhost:8000](http://localhost:8000) in your browser.

Get your free Google API key at [aistudio.google.com](https://aistudio.google.com)

---

## 📁 Project Structure

```
customcalorie/
├── main.py              # FastAPI backend + Gemini API integration
├── requirements.txt     # Python dependencies
├── Dockerfile           # Docker config for Hugging Face
├── README.md            # This file
├── .env                 # Local API key (never committed)
├── .gitignore           # Blocks .env from GitHub
└── static/
    └── index.html       # Frontend UI
```

---

## 🌐 Deployment

This app is deployed on **Hugging Face Spaces** using Docker — free forever.

To deploy your own copy:
1. Fork this repo
2. Create a new Space on [huggingface.co](https://huggingface.co) with Docker SDK
3. Add `GOOGLE_API_KEY` as a secret in Space settings
4. Push — it deploys automatically!

---

## 📄 License

MIT License — free to use, modify and distribute.

---

<div align="center">

Built with ❤️ by [Muhammad Talha](https://github.com/engineermuhammadtalha)

⭐ Star this repo if you found it useful!

</div>
