from fastapi import APIRouter, HTTPException, status
from models import *
from exceptions import *

track_router = APIRouter()

tracks:list[TrackModel]= []


@track_router.post("/track", tags=["Tracks"],status_code=201)
async def create_track(track:TrackModel)->TrackModel:
    tracks.append(track)
    return track     

@track_router.get("/tracks", response_model=list[TrackModel], tags=['Tracks'],status_code=200)
async def get_tracks()->list[TrackModel]:
    return tracks

@track_router.get("/tracks/{track_id}",response_model=TrackModel, tags=["Tracks"],status_code=200)
async def get_track_by_id(track_id:int)->TrackModel:
    for track in tracks:
            if track.id == track_id:
                return track
    raise NotFoundException
            
            
@track_router.delete("/tracks/{track_id}", response_model=TrackModel, tags=["Tracks"])
async def delete_track(track_id:int)->TrackModel:
    for track in tracks:
          if track.id == track_id:
               tracks.remove(track)
               return track
    raise NotFoundException
  

@track_router.put("/tracks/{track_id}", response_model=TrackModel, tags=["Tracks"])
def update_track_by_id(track_id: int, track_dto: TrackUpdateModel) -> TrackModel:
    for track in tracks:
        if track.id == track_id:
            track.title = track_dto.title
            track.artist = track_dto.artist
            return track
    raise NotFoundException


    