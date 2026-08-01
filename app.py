from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
import os

app = FastAPI(title="Kunwa Business Consulting Services Ltd")

# In-memory storage for reviews (or you can save to a file/database)
reviews_db = [
    {"name": "Client", "rating": "5", "comment": "Exceptional supply chain and procurement guidance. Highly recommended!"}
]

@app.get("/", response_class=HTMLResponse)
def read_index():
    index_path = os.path.join(os.path.dirname(__file__), "index.html")
    if os.path.exists(index_path):
        with open(index_path, "r", encoding="utf-8") as f:
            html_content = f.read()

        # Dynamically render reviews into the HTML
        reviews_html = ""
        for r in reviews_db:
            reviews_html += f"""
            <div class="service-card" style="margin-bottom: 20px;">
                <h3>{r['name']} <span style="color: #d4af37; font-size: 0.9rem;">(Rating: {r['rating']} / 5)</span></h3>
                <p>{r['comment']}</p>
            </div>
            """

        html_content = html_content.replace('<div id="reviews-container"></div>', reviews_html)
        return html_content
    return "<h1>Index page not found</h1>"

@app.post("/submit-review")
def submit_review(name: str = Form(...), rating: str = Form(...), comment: str = Form(...)):
    reviews_db.append({"name": name, "rating": rating, "comment": comment})
    return RedirectResponse(url="/#reviews", status_code=303)

@app.post("/submit")
def handle_submission(name: str = Form(...), email: str = Form(...), message: str = Form(...)):
    return {"status": "success", "message": f"Thank you {name}, your service request has been received!"}

app.mount("/", StaticFiles(directory="."), name="static")
