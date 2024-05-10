from fastapi import APIRouter
from models import *

track_router = APIRouter()

tracks:list = []

@track_router.get("/tracks", tags=["Tracks"] )
async def get_tracks()->dict[str,list[TrackModel]]:
    return { 
        "tracks" : tracks
    }

@track_router.get("/tracks/{id}", tags=["Tracks"] )
async def get_track_by_id(id:int):
    if tracks == []:
        return{"Message":"No tracks available"}
    else:
        for track in tracks:
            if id == track.id:
                return{ "track":track}
            else:
                return{ "Message":"Track not found as you request"}
    
   



@track_router.post("/track", tags=["Tracks"],status_code=201)
async def create_track(new_track:TrackModel)->TrackModel:
    tracks.append(new_track)
    return new_track
    
    