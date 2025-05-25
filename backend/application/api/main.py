from http.cookiejar import debug

from fastapi import APIRouter, FastAPI

app = FastAPI(
    title='Chat',
    debug=True,
)
api_router = APIRouter()


@api_router.get("/")
async def root():
    return {"message": "Hello World"}


app.include_router(api_router)