# language: es
Característica: Multiplicacion de dos numeros enteros no negativos en base 10
 
  Escenario: Multiplicacion exitosa de dos enteros positivos
    Dado los numeros enteros 7 y 8
    Cuando realizo la multiplicacion
    Entonces el resultado debe ser 56

  Escenario: Intento de multiplicacion con un numero negativo
    Dado los numeros enteros -5 y 10
    Cuando intento realizar la multiplicacion
    Entonces se lanza una excepcion de "Ambos numeros deben ser enteros positivos"