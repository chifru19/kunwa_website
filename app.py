from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

app = FastAPI(title="Kunwa Business Consulting Services Ltd")

@app.get("/")
def read_index():
    return FileResponse("index.html")

# Serve all static files (CSS, images, etc.) under the /static path
app.mount("/static", StaticFiles(directory="."), name="static")
