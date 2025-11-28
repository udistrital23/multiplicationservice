# Multiplication Service

Proyecto pequeño que expone un endpoint para multiplicar dos números enteros no negativos
y contiene pruebas unitarias y de comportamiento (BDD).

**Archivos clave**:
- `app/main.py`: FastAPI app que expone el endpoint `/multiplicacion`.
- `app/validator.py`: Implementa la función `multiplicacion(factor1, factor2)`.
- `features/validacion.feature`: Escenarios BDD en español (behave).
- `features/steps/steps.py`: Implementación de los pasos Gherkin para los escenarios.
- `tests/test_validator.py`: Tests con `pytest` que validan comportamiento de la multiplicación.

**Comportamiento esperado de `multiplicacion`**:
- Recibe dos parámetros numéricos.
- Ambos deben ser enteros (`int`) y no negativos (>= 0).
- Si alguna validación falla, se debe lanzar una excepción con el mensaje exacto:
  `Ambos numeros deben ser enteros positivos`.

**API**
- Endpoint: `POST /multiplicacion`
- Payload (JSON):

```json
{
  "numero_a": 7,
  "numero_b": 8
}
```

- Respuesta (200):

```json
{
  "resultado": 56
}
```

Ejemplo con `curl` (suponiendo el servidor en `http://127.0.0.1:8000`):

```bash
curl -sS -X POST http://127.0.0.1:8000/multiplicacion \
  -H "Content-Type: application/json" \
  -d '{"numero_a":7, "numero_b":8}'
```

Nota: la función utilizada por el endpoint es `multiplicacion` en `app/validator.py`.

**Instalación y ejecución**

- Crear un entorno virtual e instalar dependencias:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

- Ejecutar la aplicación (por ejemplo con uvicorn):

```bash
uvicorn app.main:app --reload
```

**Pruebas**

- Tests unitarios con `pytest`:

```bash
pytest -q
```

- Pruebas de comportamiento (BDD) con `behave`:

```bash
behave -q
```

**Notas y recomendaciones**
- `features/validacion.feature` contiene dos escenarios: multiplicación exitosa
  y intento con número negativo que debe producir la excepción con el mensaje
  exacto indicado arriba.
- Si el endpoint devuelve códigos 500 en caso de error de validación, considera
  adaptar `app/main.py` para capturar `Exception` generadas por `multiplicacion`
  y transformarlas en `HTTPException(status_code=400, detail=...)`.

Si quieres, ejecuto los tests aquí y corrijo cualquier fallo detectado.
