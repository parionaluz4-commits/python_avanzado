# Funciones en python

las funciones  nos permiten el mejor codigo y utilizarlo cunado sea nesesario.

```python
# ejemplo deseamos crear un programa en python
python que nos permite sumar dos numeros

numero_uno:int=45
numero_dos:int=70
numero_tres:int=78
numero_cuatro:int=20

suma:int=numero_uno+numero_dos
suma_dos:int=numero_tres+numero_cuatro

print(suma)
print(suma_dos)
```
como hacemos reutilizable el ejercicio
anterior y mas lejible.
para eso utilizaremos funciones.
la caracteristica de una funcion en
python es la siguiente:
1. debe comenzar con la palabra reservada
`def`.
2. debe tener un nombre que de a entender
que realizara la funcion.
3. debera tener parametros y estos
estaran encerrados en parentesistes `()`.
no todas las funciones resibiran
parametros aun asi debera tener los `()`
4. las funciones deberan retornar datos atravez de la palabra reservada `return`

```python
# crear un programa que me permita sumar dos numeros
def sumar(a:int,b):
    return a+b

print(sumar(78,56))
print(sumar(45,5))

```
# posicionales
```python
def suma(a,b): # en este caso tenemos una funcion suma que recibe dos parametros a,b
    suma(34,45) # en este caso estoy llamando a la funcion
# en este caso en concreto podemos decir que estamos pasando como argumento pasando los datos
# valor respectivo en el orden que le pasamos a las variables., 34 -> a , 45 -> b

def login(usuario="", password=""):
    return " acceso correcto"
login(password="12345678", usuario="tupapi")
```
# esta funcion es una funcion nominal porque para pasar los valores tengo que indicar la variable a la que se le va asignar el parametro
# de la funcion

## conociendo mas sobre funciones parametros y argumentos
sobre los parametros argumentos nominales es ampliamente usado para configuraciones para distintas configuraciones y que se puede pasar
solo los argumentos que se usaran y dejar los parametros por defecto si no se van a modificar
# tenemos un programa que me permite acceder a internet que tiene parametros por defecto sin embargo si se actualiza uno de los accesos
# se podra modificar el valor
## primer caso acceso por defecto
``` python
def config(user="admin", pass="1234", port="8080", BSSID="wifi"):
    return "conectando a internet"
config(BSSID="laboratorio1")

# segundo caso 1 bssid cambi por el del laboratorio1
def config(user="admin", pass="1234", port="8080", BSSID="wifi"):
    return "conectando a internet"
config(BSSID="laboratorio1")

## reyner desea conectarse al wifi de una luz pregunta como se llama tu wifi y cual es la contraseña, respuesta le dice el wifi es a56
# y su contraseña es 12345678
def config(user="admin", pass="1234", port="8080", BSSID="wifi"):
    return "conectando a internet"
config(BSSID="a56", pass="12345678")
```
### conociendo *args y **kwargs (empaquetado y desempaquetado de argumentos posicionales)
esta tecnica nos permite empaquetar nuestros argumentos cuando no sabemos la cantidad de datos que vamos a pasar. imaginemos que nos piden una funcion para suma n cantidad de numeros la solucion seria empaquetar los argumentos y luego desempaquetarlos para ello en la definicion de la funcion dentro de los paarametros debemos usar el operador '*' delante del nombre del parametro posicional esto hara que todos los argumentos se almacenen en un tupla `()`(lista`[]`) esto nos permite recorrer dentro de sus elementos para poder desempaquetarlo y realizar las operaciones necesarias.

``` python
#deseamos crear una funcion que nos permita sumar n cantidad de numeros 
#n es un numero variable puede ser 3,7,8 ....n 
def suma(*args):
    # *args = (2,5,7,8,9)
    acumulado = 0
    for i in args:
        acumulado += i
    return acumulado
print (suma(2,5,7,8,9))

```
### desempaquetando argumentos nominales 
en es caso como en el anterior utilizaremos el operador '*' la casuistic es el mismo sin embargo
paraa desempaquetar aargumento nominales usaremos '**' delante del nombre del parametro nominal
diferencias del anterior esto se empaqueta en un diccionario {clave:valor}
``` python
#debemos crear una funcion que permita saber encontrar la persona con mayor calificacion.
def mejor_alumno(**kwargs)
  #**kwargs= {noemi=20,eduardo=18, david=19}
  nota_maxima=-1
  for alumno,nota in kwargs.items():
    if nota > nota_maxima
     nota_maxima = nota 
     mejor_alumno = alumno 
return mejor_alumno 
mejor_alumno(noemi=20,eduardo=18, david=19)
``` 
## funciones anonimas 

las funciones anonimas en python son llamadas `lambda` , estas funciones yienen las siguientes propiedades:
1. se escribe en una unica sentencia`(linea)` 
2. no tiene nombre `(anonima)` .
3. su cuerpo conlleva un `return`  implicito.
4. puede recibir cualquier numero de parametros.
 ``` python
 lambda a,b: a+b 
``` 
la estructura para definir una funcion `lambda` es la siguiente:
 1. escribir la palabra reservada `lambda` 
 2. especificar la cantidad de parametros 
 3. indicar los datos de retorno 

 >[!TIP]    puesto que esta funcion es anonima para ejecutarla debemos almacenar la funcion en una variable 
 ``` python
suma= lambda a,b: a+b 
suma(3,6)
``` 
## documentacion 
python nos permite documentar una funcion con el objetivo de explicar mejor determinada zonas de nuestro codigo para esto usamos una cadena de texto despues de la definicion de una funcion a esta cadena de texto se le conoce como ``docstring` y esta delimitado por triples `"""aqui el texto"""`. 
 ``` python
def suma(a,b):
    """
    funcion para realizar la suma de dos numeros 
    """
### los docstring tambien nos permite explicar los parametros que recibe y los datos de salida
def resta(a,b):
    """
    a=b un numero entero
    b= a un numero entero 
    en ambos casos a, b no deben recibir valores menorea 0.
    retornara un dato entero <int> positivo
    """
    return a-b 
``` 
 >[!WARNING] en el proceso de documentacion teneer encuenta de incluir al menos lo siguiente:1. breve explicacion sobre que hace la funcion 2. especificaciones y caracteristicas de los parametros  incluyendo sus tipos. 3. restricciones de la funcion. 4. el valor retorna y sus caracteristicas 
 ### type-hints (anotaciones de tipo)
 nos permite indicar que tipo de datos recibira una variable, parametro y el valor de retorno 