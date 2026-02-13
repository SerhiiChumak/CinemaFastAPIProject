from fastapi import FastAPI

from routes import (
    movie_router,
    accounts_router,
    profiles_router
)

app = FastAPI(
    title="Movies Theatre",
    description="An online cinema is a digital platform that allows users to select, watch, and purchase access to movies and other video materials via the internet."
)

api_version_prefix = "/api/v1"

app.include_router(accounts_router, prefix=f"{api_version_prefix}/accounts", tags=["accounts"])
app.include_router(profiles_router, prefix=f"{api_version_prefix}/profiles", tags=["profiles"])
app.include_router(movie_router, prefix=f"{api_version_prefix}/theater", tags=["theater"])
