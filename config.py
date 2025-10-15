import os
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = "AIzaSyAdvNaGEjFHgTpRkk-IGWXMohtlg_XJBNo"
if not GEMINI_API_KEY:
    raise RuntimeError("Missing GEMINI_API_KEY environment variable.")
