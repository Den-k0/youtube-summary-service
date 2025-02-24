from pydantic import BaseModel, ConfigDict


class VideoBaseSchema(BaseModel):
    youtube_url: str


class VideoRequestSchema(VideoBaseSchema):
    pass


class VideoResponseSchema(VideoBaseSchema):
    id: int
    transcript: str
    summary: str

    model_config = ConfigDict(from_attributes=True)
