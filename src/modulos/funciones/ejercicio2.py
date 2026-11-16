# crear un programa que asigneun puntaje a cda letra del
# abcdarios y que un funcion me permita saber la letra que tenga menor puntaje mayr puntaje y la media


import random
abecedario = "abcdefghijklmnopqrstuvwxyz"
puntajes = {}

for letra in abecedario:
    puntajes[letra] = random.randint(1, 100)

print("Puntajes:", puntajes)
def letra_menor_puntaje(diccionario):
    letra_menor = min(diccionario, key=diccionario.get)
    return letra_menor, diccionario[letra_menor]
def letra_mayor_puntaje(diccionario):
    letra_mayor = max(diccionario, key=diccionario.get)
    return letra_mayor, diccionario[letra_mayor]
def media_puntaje(diccionario):
    total = sum(diccionario.values())
    media = total / len(diccionario)
    return media
menor_letra, menor_puntaje = letra_menor_puntaje(puntajes)
mayor_letra, mayor_puntaje = letra_mayor_puntaje(puntajes)
media = media_puntaje(puntajes)

print(f"\nLetra con MENOR puntaje: {menor_letra} con {menor_puntaje} puntos")
print(f"Letra con MAYOR puntaje: {mayor_letra} con {mayor_puntaje} puntos")
print(f"Media de puntajes: {media:.2f}")