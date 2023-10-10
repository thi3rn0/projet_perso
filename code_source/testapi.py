from fastapi import FastAPI

app = FastAPI()


"""
définition de la page d'index par défaut
"""
@app.get("/")
async def root():
    return {"message": "Hello World"}

