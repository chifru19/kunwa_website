from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

app = FastAPI(title="Kunwa Business Consulting Services Ltd")

@app.get("/")
def read_index():
    return FileResponse("index.html")

app.mount("/", StaticFiles(directory="."), name="static")
