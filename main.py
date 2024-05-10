from fastapi import FastAPI
# from routers import TracksRouter, PlaylistRouter
from routers import *
app = FastAPI()


@app.get("/", tags=["Root"], status_code=200)
def root()->dict[str, str]:
    return {"msg":"Hello route"}

app.include_router(TracksRouter)
app.include_router(PlaylistRouter)
