from sqlalchemy.orm import Mapped, mapped_column

from src.database import Base


class Video(Base):
    __tablename__ = "videos"

    id: Mapped[int] = mapped_column(
        primary_key=True, autoincrement=True
    )
    youtube_url: Mapped[str] = mapped_column(
        unique=True, nullable=False
    )
    transcript: Mapped[str] = mapped_column(nullable=False)
    summary: Mapped[str] = mapped_column(nullable=False)
