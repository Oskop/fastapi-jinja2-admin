from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


app = FastAPI()

app.mount("/assets", StaticFiles(directory="view/static/assets"), name="assets")
# app.mount("/admin_assets", StaticFiles(directory="view/admin/assets"), name="admin_assets")


templates = Jinja2Templates(directory="view")


@app.get("/items/{id}", response_class=HTMLResponse)
async def read_item(request: Request, id: str):
    return templates.TemplateResponse("item.html", {"request": request, "id": id})

@app.get("/kardinah/pendaftaran", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse("templates/index.html", {"request": request})

@app.get("/kardinah/admin", response_class=HTMLResponse)
async def admin_home(request: Request):
    return templates.TemplateResponse("admin/base/index.html", {"request": request})
