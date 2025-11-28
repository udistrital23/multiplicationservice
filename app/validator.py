def multiplicacion(factor1, factor2):
	"""Multiplica dos números enteros no negativos.

	Requisitos basados en los tests/feature:
	- Ambos parámetros deben ser de tipo `int`.
	- Ambos deben ser >= 0 (no negativos). Si alguno es negativo o no es entero,
	  se lanza una excepción con el mensaje exacto:
	  "Ambos numeros deben ser enteros positivos"

	Devuelve el producto de los dos factores.
	"""
	# Validar tipos: deben ser enteros
	if not isinstance(factor1, int) or not isinstance(factor2, int):
		raise ValueError("Ambos numeros deben ser enteros positivos")

	# Validar no negativos
	if factor1 < 0 or factor2 < 0:
		raise ValueError("Ambos numeros deben ser enteros positivos")

	return factor1 * factor2

