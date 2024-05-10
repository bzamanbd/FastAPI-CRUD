from pydantic import BaseModel
from datetime import date

class TrackModel(BaseModel):
    id:int
    title:str
    artist:str
    releaseDate:date
    description:str | None = None

class TrackUpdateModel(BaseModel):
    title:str
    artist:str
    description:str | None = None
