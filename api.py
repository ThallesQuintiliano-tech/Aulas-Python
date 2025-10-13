from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
      return {"Hello": "World"}
# instalar fastapi
# pip install fastapi uvicorn
# Rodar Servidor
# uvicorn api:app --reload