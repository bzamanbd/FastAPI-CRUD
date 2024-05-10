from fastapi import APIRouter
from models import *

track_router = APIRouter()

tracks:list[str] = ["TrackOne","TrackTwo","TrackThree","TrackFour","TrackFive"]

@track_router.get("/tracks", tags=["Tracks"] )
async def get_tracks()->list[str]:
    return tracks

@track_router.post("/track", tags=["Tracks"],status_code=201)
async def create_track(new_track:TrackModel)->TrackModel:
    return new_track
    