import os

import pymysql
from dotenv import load_dotenv
from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

load_dotenv()  # lee el archivo .env

app = FastAPI(title="Subnáutica")

# CSS, imágenes y sonidos se sirven desde /static/...
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


def conectar():
    """Equivale a mysqli_connect + mysqli_select_db de PHP."""
    return pymysql.connect(
        host=os.getenv("DB_HOST", "localhost"),
        port=int(os.getenv("DB_PORT", "3306")),
        user=os.getenv("DB_USER", "root"),
        password=os.getenv("DB_PASSWORD", ""),
        database=os.getenv("DB_NAME", "subnautica"),
        charset="utf8mb4",
        cursorclass=pymysql.cursors.DictCursor,  # filas como diccionarios
    )


# ---------- PÁGINAS ----------

@app.get("/", response_class=HTMLResponse)
def inicio(request: Request):
    return templates.TemplateResponse(request, "index.html")


@app.get("/usuarios", response_class=HTMLResponse)
def usuarios(request: Request):
    return templates.TemplateResponse(request, "usuarios.html")


# ---------- FORMULARIO (reemplaza registro.php) ----------

@app.post("/registro")
def registrar(
    nombre: str = Form(...),
    correo: str = Form(...),
    apellido: str = Form(""),
    gender: str = Form(""),
    Comentario: str = Form(""),
):
    conexion = conectar()
    try:
        with conexion.cursor() as cursor:
            # Los %s evitan la inyección SQL (el PHP original era vulnerable)
            cursor.execute(
                "INSERT INTO encuesta (nombre, apellido, correo, gender, Comentario) "
                "VALUES (%s, %s, %s, %s, %s)",
                (nombre, apellido, correo, gender, Comentario),
            )
        conexion.commit()
    finally:
        conexion.close()

    # Después de guardar, redirige a la tabla (evita reenvíos al pulsar F5)
    return RedirectResponse(url="/registros", status_code=303)


@app.get("/registros", response_class=HTMLResponse)
def ver_registros(request: Request):
    conexion = conectar()
    try:
        with conexion.cursor() as cursor:
            cursor.execute("SELECT * FROM encuesta")
            registros = cursor.fetchall()
    finally:
        conexion.close()

    return templates.TemplateResponse(
        request, "registros.html", {"registros": registros}
    )
