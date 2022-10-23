from fastapi import FastAPI,status
import uvicorn
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from routers.recipes_router.recipes import recipesRoute
from fastapi.responses import JSONResponse

app = FastAPI()

app.mount("/client/build", StaticFiles(directory="./client/build"), name="build")
app.include_router(recipesRoute)


@app.get('/sanity', response_class= JSONResponse , status_code= status.HTTP_200_OK)
def root():
    return {"message":"OK"}


@app.get('/')
def root():
    return FileResponse('./client/build/index.html')

if __name__ == "__main__":
    uvicorn.run("server:app",host="localhost", port=8000,reload=True)