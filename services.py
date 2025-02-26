import os

import requests
from dotenv import load_dotenv
from fastapi import HTTPException
from groq import Groq

load_dotenv()

SUPADATA_API_KEY = os.getenv("SUPADATA_API_KEY")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

GROQ_MODEL = "llama-3.3-70b-versatile"

if not SUPADATA_API_KEY or not GROQ_API_KEY:
    raise ValueError("API keys are missing!")


def get_transcript(youtube_url: str) -> str:
    response = requests.get(
        f"https://api.supadata.ai/v1/youtube/transcript?url={youtube_url}&text=true",
        headers={"x-api-key": SUPADATA_API_KEY}
    )

    if response.status_code != 200:
        raise HTTPException(
            status_code=response.status_code,
            detail=f"Supadata API error: {response.text}"
        )

    transcript_data = response.json()
    return transcript_data.get("content", "")


def get_summary(transcript: str) -> str:
    client = Groq(api_key=GROQ_API_KEY)

    transcript_trimmed = transcript[:6000]

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": f"Summarize the following transcript: {transcript_trimmed}"
            }
        ],
        model=GROQ_MODEL,
    )

    return chat_completion.choices[0].message.content
