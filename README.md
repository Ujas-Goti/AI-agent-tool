# AI Agent – Gemini + LangChain + Flask (Web UI + API)

A lightweight developer assistant for **code explanation, documentation drafting, and troubleshooting**.
- **LLM:** Google Gemini (via `google-generativeai`)
- **Orchestration:** LangChain (`langchain-google-genai`)
- **Server:** Flask
- **Interfaces:** Chat-style **Web UI** + JSON **API**

# ✅ Setup & Run Instructions (Gemini + LangChain + Flask)

### 1️⃣ Clone the Project
```bash
git clone https://github.com/Ujas-Goti/AI-agent-tool.git
cd ai-agent-tool
```

### 2️⃣ Create & Activate Virtual Environment
```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# macOS / Linux
python3 -m venv .venv
source .venv/bin/activate
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Add Gemini API Key
Create a `.env` file in the **project root** with:
```
GEMINI_API_KEY=your_api_key_here
```
Get your key from: https://aistudio.google.com/app/apikey

### 5️⃣ Run the App
```bash
python run.py
```

Access the app at:
```
http://localhost:5000
```

### ✅ Features
- Light/Dark mode toggle  
- Streaming assistant replies  
- Reset feature

To clear manually:
```bash
curl -X POST http://localhost:5000/api/reset
```
or click **Reset** in the UI.
