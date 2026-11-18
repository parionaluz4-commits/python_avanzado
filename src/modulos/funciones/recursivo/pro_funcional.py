# ejercicio para map()
# recuerda map sirve para trasformar todos los elementos

# Ejercicio 1: Tienes una lista de numeros y quieres obtener una
# nueva lista con el cubo (elevado a 3) de cada numero.
numeros = [1, 2, 3, 4, 5]
cubos = list(map(lambda x: x ** 3, numeros))
print(cubos)

## ejercicio 2: Tienes una lista de temperaturas (algunas bajo cero).
# filtra la lista para quedarte solo con las temperaturas positivas
# (mayores a 0).
temp: list[int | float] = [-2, 10, 0, -20, -1, -10, 18, 23.0]
nueva_tem = list(filter(lambda t: t > 0, temp))
print(f"las temperaturas mayores a cero son: {nueva_tem}")

# ejercicio combinando map() y filter()
## Tienes una lista de numeros. Primero filtra para quedarte solo con
# los numeros pares. Luego usa, map para multiplicarlos por 10 los
# numeros pares.
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = list(filter(lambda n: n % 2 == 0, numeros))
nueva_num = list(map(lambda n: n * 10, pares))
print(f"los numeros pares multiplicados por 10 son: {nueva_num}")
