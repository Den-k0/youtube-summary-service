import os

from dotenv import load_dotenv

load_dotenv()

SUPADATA_API_KEY = os.getenv("SUPADATA_API_KEY")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not SUPADATA_API_KEY or not GROQ_API_KEY:
    raise ValueError("API keys are missing!")

GROQ_MODEL = os.getenv("GROQ_MODEL")
