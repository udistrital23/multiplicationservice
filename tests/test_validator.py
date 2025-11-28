
import pytest

def multiplicar(a: int, b: int) -> int:
    return a * b

def test_multiplicacion_exitosa_pequenos():
    assert multiplicar(3, 4) == 12

def test_multiplicacion_exitosa_grandes():
    assert multiplicar(50, 20) == 1000

@pytest.mark.parametrize("factor1, factor2", [
    (-5, 10),     # Factor1 negativo
    (10, -5),     # Factor2 negativo
    (-10, -5),    # Ambos negativos
])
def test_numeros_negativos(factor1, factor2):
    with pytest.raises(Exception) as excinfo:
        multiplicar(factor1, factor2)
    assert str(excinfo.value) == "Ambos numeros deben ser enteros positivos"

@pytest.mark.parametrize("factor1, factor2", [
    (4, 3.5),     # Factor2 es flotante
    (3.5, 4),     # Factor1 es flotante
    (4.1, 5.2)    # Ambos son flotantes
])
def test_numeros_no_enteros(factor1, factor2):
    with pytest.raises(Exception) as excinfo:
        multiplicar(factor1, factor2)
    assert str(excinfo.value) == "Ambos numeros deben ser enteros positivos"
