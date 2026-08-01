from fastapi import FastAPI, Form
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, RedirectResponse
import os

app = FastAPI(title="Kunwa Business Consulting Services Ltd")

reviews_db = [
    {"name": "Client", "rating": "5", "comment": "Exceptional supply chain and procurement guidance. Highly recommended!"}
]

@app.get("/", response_class=FileResponse)
def read_index():
    return "index.html"

@app.post("/submit-review")
def submit_review(name: str = Form(...), rating: str = Form(...), comment: str = Form(...)):
    reviews_db.append({"name": name, "rating": rating, "comment": comment})
    return RedirectResponse(url="/#reviews", status_code=303)

@app.post("/submit")
def handle_submission(name: str = Form(...), email: str = Form(...), message: str = Form(...)):
    return {"status": "success", "message": f"Thank you {name}, your service request has been received!"}

app.mount("/static", StaticFiles(directory="."), name="static")
