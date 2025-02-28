from sqlalchemy import select
from sqlalchemy.orm import Session
from src.models import Video
from src.schemas import VideoCreateSchema


def create_video(
    db: Session, video_data: VideoCreateSchema, transcript: str, summary: str
) -> Video:
    """
    Create a new video entry in the database.

    This function creates a new video record in the database using
    the provided data (YouTube URL, transcript, and summary).
    It commits the transaction and returns the created video object.

    Args:
        db (Session): The database session used to interact with the database.
        video_data (VideoCreateSchema): The data schema containing the
            video information, including the YouTube URL.
        transcript (str): The transcript of the YouTube video.
        summary (str): The summary of the YouTube video.

    Returns:
        Video: The created video object, which includes
        the YouTube URL, transcript, and summary.

    Raises:
        SQLAlchemyError: If there is an issue with the database operation.
    """
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
    """
    This function queries the database and retrieves
    all video records stored in the `Video` table.

    Args:
        db (Session): The database session used to interact with the database.

    Returns:
        list: A list of all video records stored in the `Video` table.

    Raises:
        SQLAlchemyError: If there is an issue with the database operation.
    """
    return db.scalars(select(Video)).all()
