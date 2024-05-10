from fastapi import APIRouter
from models import *

track_router = APIRouter()

tracks:list = []

@track_router.get("/tracks", tags=["Tracks"] )
async def get_tracks()->dict[str,list[TrackModel]]:
    return { 
        "tracks" : tracks
    }

@track_router.get("/tracks/{track_id}", tags=["Tracks"] )
async def get_track_by_id(track_id:int):
     for track in tracks:
            if track.id == track_id:
                return{ "track":track}
            
            
@track_router.delete("/tracks/{track_id}", tags=["Tracks"] )
async def delete_track(track_id:int):
    if tracks == []:
        return{"Message":"No tracks available"}
    else:
        for track in tracks:
            if track.id == track_id:
                tracks.remove(track)
                return{ "Message": f"{track.title} is deleted"}            

@track_router.put("/tracks/{track_id}", tags=["Tracks"] )
async def update_track(track_id:int, trackDTO: TrackUpdateModel):
    if tracks == []:
        return{"Message":"No tracks available"}
    else:
        for track in tracks:
            if track.id == track_id:
                track.title = trackDTO.title
                track.artist = trackDTO.artist
                track.description = trackDTO.description
                return{ "updated": track}
    
   
@track_router.post("/track", tags=["Tracks"],status_code=201)
async def create_track(new_track:TrackModel)->TrackModel:
    tracks.append(new_track)
    return new_track
    
    