def mayor_precio(**kwargs):

    precio_maximo = -1
    for ingrediente, precio in kwargs.items():
        if precio > precio_maximo:
            precio_maximo = precio
            ingrediente_mayor = ingrediente
    return f"el ingrediente de mayor precio es {ingrediente_mayor}"

print(mayor_precio(ajo=2, papa=3, aceite=8))