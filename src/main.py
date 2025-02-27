from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from src.crud import create_video, get_all_videos
from src.database import get_db
from src.models import Video
from src.schemas import VideoCreateSchema, VideoResponseSchema, VideoListSchema
from src.services import get_transcript, get_summary

app = FastAPI()


@app.post("/process-video/", response_model=VideoResponseSchema)
def process_video(request: VideoCreateSchema, db: Session = Depends(get_db)):
    existing_video = (
        db.query(Video)
        .filter(Video.youtube_url == request.youtube_url)
        .first()
    )
    if existing_video:
        return existing_video

    transcript = get_transcript(request.youtube_url)
    summary = get_summary(transcript)

    return create_video(db, request, transcript, summary)


@app.get("/videos/", response_model=list[VideoListSchema])
def get_videos(db: Session = Depends(get_db)):
    return get_all_videos(db)
