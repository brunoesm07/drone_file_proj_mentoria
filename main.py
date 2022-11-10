from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def drone_file_root():
    return {"App": "Drone File"}

@app.post("/inserir_drone")
def create_drone():
    return {"inserir drone"}

@app.post("/inserir_piloto")
def create_piloto():
    return {"inserir piloto"}

@app.get("/drone/{numero_serie_drone}")
def read_drone(numero_serie_drone: int)
    return {drone}

@app.get("/piloto/{numero_licenca}")
def read_drone(numero_licenca: int)
    return {piloto}

@app.put("/drone/{numero_serie_drone}")
def update_drone(numero_serie_drone: int)
    return {drone}

@app.put("/piloto/{numero_licenca}")
def update_piloto(numero_licenca: int)
    return {piloto}

@app.delete("/drone/{numero_serie_drone}")
def delete_drone(numero_serie_drone: int)
    return {drone}

@app.delete("/piloto/{numero_licenca}")
def delete_piloto(numero_licenca: int)
    return {piloto}