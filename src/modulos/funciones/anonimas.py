# haciendo uso de lambda crear una funcion que me muestre un mensaje perzonalizado 
mensaje = lambda nombre: f"Hola {nombre}, bienvenido a Python Avanzado"
print(mensaje("luz"))

#crear una funcion para calcular el area de un rectangulo , siendo la formula la siguiente a=b*h 
area:int= lambda b, h: b * h
print (area (5,6))
#crear una funcion que verifique si un numero es par o impar 

es_par = lambda n: n % 2 == 0

if es_par(4):
    print("es par")
else:
    print("es impar")