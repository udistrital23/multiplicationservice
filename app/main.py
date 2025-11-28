from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

from app.validator import multiplicacion


class SumaRequest(BaseModel):
    numero_a: int
    numero_b: int


class SumaResponse(BaseModel):
    resultado: int


app = FastAPI(title="Base Converter Service")


@app.post("/multiplicacion", response_model=SumaResponse)
async def suma(req: SumaRequest):
    try:
        resultado = multiplicacion(
            req.numero_a,
            req.numero_b
        )
        return SumaResponse(resultado=resultado)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
