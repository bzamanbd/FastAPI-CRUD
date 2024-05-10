from fastapi import APIRouter

track_router = APIRouter()

tracks:list[str] = ["TrackOne","TrackTwo","TrackThree","TrackFour","TrackFive"]

@track_router.get("/tracks", tags=["Tracks"] )
def get_tracks()->list[str]:
    return tracks