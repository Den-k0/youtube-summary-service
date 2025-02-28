from pydantic import BaseModel, ConfigDict


class VideoBaseSchema(BaseModel):
    youtube_url: str


class VideoCreateSchema(VideoBaseSchema):
    pass


class VideoResponseSchema(VideoBaseSchema):
    id: int
    transcript: str
    summary: str

    model_config = ConfigDict(from_attributes=True)


class VideoListSchema(VideoBaseSchema):
    id: int
    summary: str
