from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, Response  
import markdown

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/favicon.ico", include_in_schema=False)
async def favicon():
    return Response(status_code=204)

@app.post("/api/convert")
async def convert(request: Request):
    data = await request.json()
    md_text = data.get("markdown", "")
    html = markdown.markdown(
        md_text,
        extensions=["fenced_code", "codehilite", "tables", "sane_lists"]
    )
    return {"html": html}

@app.get("/", response_class=HTMLResponse)
async def index():
    with open("static/index.html", "r", encoding="utf-8") as f:
        return f.read()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)