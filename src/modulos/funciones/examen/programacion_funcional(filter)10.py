palabras: list[str] = ["sol", "computadora", "luz", "programacion", "ia", "python"]

print(list(filter(lambda palabra: len(palabra) > 4, palabras)))