from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    # Datos para las cartas, puedes cambiar esto por datos dinámicos
    cartas = [
        {"titulo": "Carta 8", "descripcion": "Descripción de la carta 1", "imagen": "https://via.placeholder.com/150"},
        {"titulo": "Carta 2", "descripcion": "Descripción de la carta 2", "imagen": "https://via.placeholder.com/150"},
        {"titulo": "Carta 3", "descripcion": "Descripción de la carta 3", "imagen": "https://via.placeholder.com/150"},
    ]
    return templates.TemplateResponse("cartas.html", {"request": request, "cartas": cartas})

