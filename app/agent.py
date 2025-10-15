import google.generativeai as genai
from langchain_google_genai import ChatGoogleGenerativeAI
from config import GEMINI_API_KEY

# ✅ Configure Gemini
genai.configure(api_key=GEMINI_API_KEY)

# ✅ Initialize LangChain Gemini Model
LC_MODEL = ChatGoogleGenerativeAI(
    model="gemini-2.5-pro",
    temperature=0.2,
    google_api_key=GEMINI_API_KEY
)

# ✅ System behavior (defines assistant role)
SYSTEM_PROMPT = """
You are a helpful AI coding assistant. You:
- Explain code clearly
- Help troubleshoot bugs
- Generate clean documentation
- Respond in Markdown with code blocks where needed
- Keep explanations concise and developer-friendly
"""

EXAMPLES = [
    {
        "role": "user",
        "content": "What is a Python decorator?"
    },
    {
        "role": "assistant",
        "content": "A decorator in Python is a function that modifies the behavior of another function without changing its code. Example:\n```python\ndef my_decorator(func):\n    def wrapper():\n        print('Before call')\n        func()\n        print('After call')\n    return wrapper\n```"
    },
    {
        "role": "user",
        "content": "Fix this error: TypeError: x is undefined in JavaScript."
    },
    {
        "role": "assistant",
        "content": "That error means you're accessing a variable before it has a value. Example cause:\n```js\nconsole.log(x.length); // x was never assigned\n```\n✅ Fix: make sure x is defined first:\n```js\nconst x = 'hello';\nconsole.log(x.length);\n```"
    }
]

def run_agent(messages):
    final_msgs = [
        {"role": "system", "content": SYSTEM_PROMPT},
        *EXAMPLES,
        *messages
    ]

    latest_user_msg = next(
        (m["content"] for m in reversed(messages) if m["role"] == "user"),
        ""
    )

    response = LC_MODEL.invoke(latest_user_msg)
    return response.content
