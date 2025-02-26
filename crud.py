from sqlalchemy.orm import Session
from models import Video
from schemas import VideoCreateSchema


def create_video(
    db: Session, video_data: VideoCreateSchema, transcript: str, summary: str
) -> Video:
    db_video = Video(
        youtube_url=video_data.youtube_url,
        transcript=transcript,
        summary=summary,
    )
    db.add(db_video)
    db.commit()
    db.refresh(db_video)
    return db_video


def get_all_videos(db: Session):
    return db.query(Video).all()
