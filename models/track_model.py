from pydantic import BaseModel
from datetime import date

class TrackModel(BaseModel):
    title:str
    artist:str
    releaseDate:date
    description:str | None = None
