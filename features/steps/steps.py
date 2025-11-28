from behave import given, when, then

from app.validator import multiplicacion


@given('los numeros enteros {a} y {b}')
def step_given_numeros_enteros(context, a, b):
	context.a = int(a)
	context.b = int(b)
	context.result = None
	context.exc = None


@when('realizo la multiplicacion')
def step_when_realizo_multiplicacion(context):
	try:
		context.result = multiplicacion(context.a, context.b)
	except Exception as e:
		context.exc = e


@when('intento realizar la multiplicacion')
def step_when_intento_multiplicacion(context):
	try:
		context.result = multiplicacion(context.a, context.b)
	except Exception as e:
		context.exc = e


@then('el resultado debe ser {expected}')
def step_then_resultado(context, expected):
	assert context.exc is None, f"Se lanzó una excepción inesperada: {context.exc}"
	assert context.result == int(expected), f"Resultado esperado {expected}, obtenido {context.result}"


@then('se lanza una excepcion de "{message}"')
def step_then_excepcion(context, message):
	assert context.exc is not None, "No se lanzó ninguna excepción"
	assert str(context.exc) == message, f"Mensaje de excepción esperado '{message}', obtenido '{context.exc}'"

