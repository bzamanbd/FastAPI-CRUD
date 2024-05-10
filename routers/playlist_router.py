from fastapi import APIRouter

playlist_router = APIRouter()

playlist:list[str] = ["PlaylistOne","PlaylistTwo","PlaylistThree"]

@playlist_router.get("/playlists", tags=["Playlist"], status_code=200)
async def get_playlist()->list[str]:
    return playlist 

@playlist_router.post("/playlist", tags=["Playlist"], status_code=201)
def create_playlist(new_playlist:str):
    playlist.append(new_playlist)
    return playlist

