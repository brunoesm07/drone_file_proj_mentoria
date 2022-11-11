from fastapi import FastAPI

description = """
Drone File é um sistema de gestão de drones.

Obtenha informações sobre seu drone e quais dos seus pilotos estão aptos a pilota-lo! 

## Você poderá:

* Incluir novos drones e pilotos
* Pesquisar todos os pilotos aptos a utilizar determinado drone
* Pesquisar todas as informações de drones e pilotos a sua escolha.
"""

tags_metadata = [
    {
        "name": "drones",
        "description": "Incluir, pesquisar, editar ou deletar **drones** no sistema.",
    },
    {
        "name": "pilotos",
        "description": "Incluir, pesquisar, editar ou deletar **pilotos** no sistema.",
    },
]

app = FastAPI(
    title="Drone File",
    description=description,
    version="0.0.1",
    openapi_tags=tags_metadata
)

@app.get("/")
def drone_file_root():
    return {"App": "Drone File"}

@app.post("/drones/", status_code=201, tags=["drones"])
def create_drones():
    return {}

@app.post("/pilotos/", status_code=201, tags=["pilotos"])
def create_pilotos():
    return {}

@app.get("/drones/{numero_serie_drone}", tags=["drones"])
def read_drones(numero_serie_drone: int):
    return {"drones": {numero_serie_drone}}

@app.get("/drones", tags=["drones"])
def read_drones():
    return {"drones"}

@app.get("/drones/{numero_serie_drone}/pilotos", tags=["drones"])
def read_drones():
    return {"drones": {"numero_serie_drone": "pilotos"}}

@app.get("/pilotos/{numero_licenca}", tags=["pilotos"])
def read_drones(numero_licenca: int):
    return {"pilotos": {numero_licenca}}

@app.put("/drones/{numero_serie_drone}", tags=["drones"])
def update_drones(numero_serie_drone: int):
    return {}

@app.put("/pilotos/{numero_licenca}", tags=["pilotos"])
def update_pilotos(numero_licenca: int):
    return {}

@app.delete("/drones/{numero_serie_drone}", tags=["drones"])
def delete_drones(numero_serie_drone: int):
    return {f"O drone com nº de serie {numero_serie_drone} foi deletado."}

@app.delete("/pilotos/{numero_licenca}", tags=["pilotos"])
def delete_pilotos(numero_licenca: int):
    return {f"O piloto com nº de licença {numero_licenca} foi deletado."}
