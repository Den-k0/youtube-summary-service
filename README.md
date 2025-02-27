# YouTube Video Transcript and Summary Service

This project provides an API that allows users to process YouTube videos by generating transcripts and summaries. It retrieves the transcript of the video, summarizes it using AI, and stores the information in a database.

## Features

- Fetches YouTube video transcript using the Supadata API.
- Generates a summary of the transcript using the Groq API.
- Stores video data (URL, transcript, summary) in a SQLite database.
- Provides endpoints to retrieve processed videos and their details.

## Technologies Used

- **Python 3.12**
- **FastAPI**: Web framework for building the API.
- **SQLAlchemy**: ORM for interacting with the database.
- **SQLite**: Database for storing video data.
- **Groq API**: For summarizing the transcript.
- **Supadata API**: For fetching YouTube video transcripts.

## Installation

### Prerequisites

- Python 3.12+
- Docker (for containerization)
- Poetry (for dependency management)

### Setup

1. Clone the repository:

    ```bash
    git clone https://github.com/Den-k0/youtube-summary-service.git
    cd youtube-summary-service
    ```

2. Install dependencies:

    ```bash
    poetry install --no-root  # Install dependencies
    poetry run alembic upgrade head  # Apply database migrations
    ```

3. Create a `.env` file from the `.env.sample`:

    ```bash
    cp .env.sample .env  # Create a `.env` file from `.env.sample` and put your Supadata & Groq API keys
    ```

4. Add your Supadata API key and Groq API key to the `.env` file:

    ```
    SUPADATA_API_KEY=your_supadata_api_key
    GROQ_API_KEY=your_groq_api_key
    GROQ_MODEL=llama-3.3-70b-versatile
    ```

### Running the Application

#### Run with Docker

To run the application with Docker, use:

```bash
docker compose up --build
```

#### Run locally

To run the application locally, use:

```bash
poetry run uvicorn src.main:app --host 0.0.0.0 --port 8000
```
