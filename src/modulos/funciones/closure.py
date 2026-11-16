##crea una funcion tipo closure que me permita ingresar nombre apellido y me retorne un mensaje con ambos datos 

def creador (nombre:str):
    def apellido(ap:str):
        return(f"tu nombre es:{nombre} y tu apellido es {ap}") 
    return apellido 
alumno1=creador("david")
print(alumno1("goliat"))

###usando closure crear una funcion multiplicador que reciva por parametro el 
# factor que devuelva una funcion que permita multiplicarcualquier numero por el factor
def multiplicador(factor: int | float):
    def multiplicar(numero: int | float):
        return factor * numero
    return multiplicar

por2 = multiplicador(2)
print(por2(10))
por5 = multiplicador(5)
print(por5(10))