#crear una funcion que cuyos parametros seran un entero una lista de enteros o  flotantes y la funcion retornara una lista de enteros 00 flotantes 
def funcion(numero: int, lista: list[int | float]) -> list[int | float]:
    resultado = []
    for elemento in lista:
        resultado.append(numero * elemento)
    return resultado