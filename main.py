import uvicorn
from fastapi import FastAPI

from application.router import api_router
from databases.session import engine, Base

app = FastAPI(
    openapi_url="/ram-swagger/openapi.json",
    docs_url="/ram-swagger/docs",
    redoc_url="/ram-swagger/redoc",
    redirect_slashes=False
)


@app.on_event("startup")
async def startup():
    Base.metadata.create_all(bind=engine)
    pass


@app.on_event("shutdown")
async def shutdown():
    pass

app.include_router(api_router, prefix='/ram')

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8080)
