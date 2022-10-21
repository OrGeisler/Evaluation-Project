from fastapi import FastAPI
import uvicorn
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from routers.first_router.first_router import firstRoute

app = FastAPI()

app.mount("/client/build", StaticFiles(directory="./client/build"), name="build")
app.include_router(firstRoute)


@app.get('/sanity')
def root():
    return {"message":"Server is up and running"}


@app.get('/')
def root():
    return FileResponse('./client/build/index.html')

if __name__ == "__main__":
    uvicorn.run("server:app",host="localhost", port=8000,reload=True)