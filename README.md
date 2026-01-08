# WebBriefAI 🚀

**WebBriefAI** is an AI-powered web orchestration tool that transforms complex URLs into concise, actionable summaries. By combining custom web scraping with the latest **Gemini 2.5 Flash-Lite** model, it provides a high-speed, streaming interface for rapid information synthesis.

## 🌟 Key Features
- **Intelligent Scraping:** Utilizes `BeautifulSoup4` to strip noise (scripts, CSS, ads) and extract core text content.
- **Cross-Provider Orchestration:** Uses the **OpenAI Python SDK** to interface with **Google Gemini API** endpoints, demonstrating API interoperability.
- **Streaming UI:** Implements a typewriter-style streaming output using `Gradio` for a modern user experience.
- **Secure Access:** Built-in authentication layer to protect API usage.

## 🛠️ Tech Stack
- **Language:** Python 3.12
- **LLM:** Gemini 2.5 Flash-Lite (via OpenAI-compatible endpoint)
- **Frontend:** Gradio
- **Scraping:** BeautifulSoup4 & Requests
- **Environment Management:** `uv` & `python-dotenv`

## 📂 Project Structure
```text
.
├── app.py              # Main Gradio application & LLM logic
├── scraper.py          # Web scraping & content cleaning module
├── requirements.txt    # Project dependencies
└── .env                # Local API keys (excluded via .gitignore)
```

## 🚀 Getting Started

1. **Clone the repo:** git clone:
    ```
    git clone https://github.com/kristheticcc/Web-Brief-AI.git
   ```
2. **Install dependencies:**
   ```
   pip install -r requirements.txt
   ```
3. **Set up environment variables:** Create a `.env` file with your API keys
4. **Run the app:** python app.py
   