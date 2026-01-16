from fastapi import FastAPI
import json

app = FastAPI()

@app.get("/historico")
def historico():
    return json.load(open("historico.json"))
