
def obtener_promedio(numeros: list[int]) -> float:
    if len(numeros) == 0:
        return 0.0
    return sum(numeros) / len(numeros)

print( obtener_promedio([10, 20, 30]))
print(obtener_promedio([7, 8, 9, 10]))