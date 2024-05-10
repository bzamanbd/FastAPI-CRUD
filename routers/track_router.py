from fastapi import APIRouter
from models import *

track_router = APIRouter()

tracks:list = []

@track_router.get("/tracks", tags=["Tracks"] )
async def get_tracks()->dict[str,list[TrackModel]]:
    return { 
        "tracks" : tracks
    }

@track_router.post("/track", tags=["Tracks"],status_code=201)
async def create_track(new_track:TrackModel)->TrackModel:
    tracks.append(new_track)
    return new_track
    
    