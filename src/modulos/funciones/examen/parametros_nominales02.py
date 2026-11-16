def calcular_precio_final(precio, impuesto=0.18, descuento=0.0):
    return precio * (1 + impuesto) * (1 - descuento)
print( calcular_precio_final(precio=100, descuento=0.05))
print( calcular_precio_final(100))