# ejercicio usando la tecnica *args crear
# una funcion que me permita identificar
# numeros pares de n cantidad de numeros
# pasados por arg, la funcion debera
#retornar una lista con los numeros pares identificados

def pares(*args):
    lista_pares = []
    for i in args:
        if i % 2 == 0:
            lista_pares.append(i)
    return lista_pares

print(pares(2, 5, 7, 8, 9, 10, 12))