from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from code_source.presentation.web.controller.module_controller import ModuleController
app = FastAPI()


"""
définition de la page d'accueil
"""
@app.get("/")
async def root():
    return {"message": "Hello World"}

# @app.post("/modules")
# async def get_modules(classe: str = Form(...), matiere: str = Form(...)):
#     # controller = ModuleController()
#     # """voir dans la doc de fastapi comment remplir les paramètres classe et matières"""
#     # return HTMLResponse(content=controller.get_modules(classe=, matiere=), status_code=200)
#     pass
"""
page formulaire
"""
@app.post("/modules")
async def trier_modules(classe: int = Form(...), matiere: int = Form(...)):
    controller = ModuleController()
    return HTMLResponse(content=controller.trier_modules(classe, matiere), status_code=200)