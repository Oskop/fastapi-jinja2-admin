from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


app = FastAPI()

app.mount("/assets", StaticFiles(directory="view/static/assets"), name="assets")


templates = Jinja2Templates(directory="view")


@app.get("/admin/template/{page}", response_class=HTMLResponse)
async def admin_home(request: Request, page: str):
    return templates.TemplateResponse("templates/{}".format(page) + ".html", {"request": request})
