from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, Response  
import markdown

md = FastAPI()

@md.post("/md/convert")
async def convert(rq: Request):
    data = await rq.json()
    md_base = data.get("markdown", "")
    html = markdown.markdown(
        md_base,
        extensions=["fenced_code", "codehilite", "tables", "sane_lists"]
    )
    return {"html": html}

@md.get("/", response_class=HTMLResponse)
async def index():
    with open("md.html", "r", encoding="utf-8") as f:
        return f.read()
    
