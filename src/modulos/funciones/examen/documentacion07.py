def calcular_potencia(base: float, exponente: float) -> float:
    """
    1. Breve explicación:
    Calcula la potencia de un numero elevando la base al exponente indicado.

    2. Especificación y tipos de los parámetros:
    base (float): numero base que se va a elevar.
    exponente (float): exponente al que se eleva la base.

    3. Restricciones:
    El exponente no debe ser negativo.

    4. Características del valor que retorna:
    Retorna un numero flotante (float) con el resultado de base ** exponente.
    """
    return base ** exponente

print(calcular_potencia(2, 3))