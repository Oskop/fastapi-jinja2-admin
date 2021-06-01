from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


app = FastAPI()

app.mount("/assets", StaticFiles(directory="templates/assets"), name="assets")


templates = Jinja2Templates(directory="templates")


@app.get("/items/{id}", response_class=HTMLResponse)
async def read_item(request: Request, id: str):
    return templates.TemplateResponse("item.html", {"request": request, "id": id})

@app.get("/kardinah", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse("main/home.html", {"request": request})

@app.get("/kardinah/admin", response_class=HTMLResponse)
async def admin_home(arg):
    return templates.TemplateResponse("admin/main/index.html")
