from fastapi import APIRouter, HTTPException, status
from models import *
from exceptions import *

track_router = APIRouter()

tracks= []


@track_router.post("/track", tags=["Tracks"],status_code=201)
async def create_track(track:TrackModel)->TrackModel:
    tracks.append(track)
    return track     

@track_router.get("/tracks", response_model=list[TrackModel], tags=['Tracks'],status_code=200)
async def get_tracks():
    return {"tracks":tracks}

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

   
     

@track_router.put("/tracks/{track_id}",  tags=["Tracks"])
def update_track_by_id(track_id: int, track_dto: TrackUpdateModel) -> TrackModel:
    for track in tracks:
        if track.id == track_id:
            track.title = track_dto.title
            track.artist = track_dto.artist
            return track
    raise NotFoundException


    