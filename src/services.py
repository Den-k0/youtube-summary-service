import requests
from fastapi import HTTPException
from groq import Groq

from src.config import SUPADATA_API_KEY, GROQ_API_KEY, GROQ_MODEL


def get_transcript(youtube_url: str) -> str:
    """
    Get the transcript of a YouTube video from Supadata API.

    This function sends a GET request to the Supadata API to fetch
    the transcript of the YouTube video specified by the URL. If the
    request is successful, it returns the transcript content as a string.

    The `SUPADATA_API_KEY` is retrieved from the 'config.py' file.

    Args:
        youtube_url (str): The URL of the YouTube
        video to fetch the transcript for.

    Returns:
        str: The transcript content of the video,
        or an empty string if no content is found.

    Raises:
        HTTPException: If the API response status code is not 200.
    """
    response = requests.get(
        f"https://api.supadata.ai/v1/youtube/transcript?url={youtube_url}&text=true",
        headers={"x-api-key": SUPADATA_API_KEY},
    )

    if response.status_code != 200:
        raise HTTPException(
            status_code=response.status_code,
            detail=f"Supadata API error: {response.text}",
        )

    transcript_data = response.json()
    return transcript_data.get("content", "")


def get_summary(transcript: str) -> str:
    """
    Get a summary of the transcript using the Groq API.

    This function sends a request to the Groq API to generate a summary of the
    provided transcript. It uses the Groq model specified by the environment
    variable `GROQ_MODEL` to generate the summary. The transcript is trimmed to
    a length of 6000 characters before being sent to the API.

    The `GROQ_API_KEY` is retrieved from the 'config.py' file.

    Args:
        transcript (str): The transcript to summarize.

    Returns:
        str: The summary of the transcript provided by the Groq API.

    Raises:
        Exception: If the Groq API fails
        to return a response or an error occurs.
    """
    client = Groq(api_key=GROQ_API_KEY)

    transcript_trimmed = transcript[:6000]

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a helpful assistant. Your task is to provide"
                    "a summary for the user's request. Return only the"
                    "summary without any additional information."
                    "If the user discusses dangerous or illegal topics,"
                    "respond with: I couldn't process this information."
                ),
            },
            {
                "role": "user",
                "content": (
                    f"Summarize the following transcript: {transcript_trimmed}"
                ),
            },
        ],
        model=GROQ_MODEL,
    )

    return chat_completion.choices[0].message.content
