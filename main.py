from fastapi import FastAPI
from src.models.user import User
from src.services.sheets import Sheets

app = FastAPI()


@app.get("/")
async def rootGet():
    return {"status": "sucess", 'message': "API funcionando!"}


@app.post("/")
async def rootPost(data: User):
    serviceSheets = Sheets()
    responseServiceSheets = serviceSheets.register(data)

    if not 'Sucesso' in responseServiceSheets:
        return {"status": "Error", "message": "Durante o processo de registro ocorreu um erro."}

    return {"status": "Sucess", "message": "Parabens! Você foi pré-registrado. Boa Sorte!!!"}
