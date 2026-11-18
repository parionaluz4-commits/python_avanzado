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


## type-hints(anotaciones de tipo)
Nos permite indicar que tipo de datos tendra una variable, parametro y el valor de retorno de una funcion.
Para utilizarlos debemos de indicar el tipo de dato despues del separador ':', en el caso del valor de retorno usaremos '->' luego el tipo de dato y finalmente el separador ':' que indica el inicio del bloque de codigo de la funcion.
Las 'anotaciones de tipo' son una herramienta que nos permite complementar la documentacion de nuestro codigo
**tenemos los siguientes**

+ **simple**

- int -> numeros enteros
- float -> numeros decimales
- bool -> datos boleanos,(verdad o falso)
- str -> datos de texto o cadena
- list -> listas '[]'
- tuple -> tuplas '()'
- dict -> diccionarios '{}'

+ **compuestos**

existen casos en los que necesitamos mas exclusividad en la *anotacion de tipos* ¿que ocurre si queremos indicar una *lista de cadenas* o un *conjunto de enteros*?

- list[str] -> lista de cadenas de texto
- list[int] -> lista de numeros enteros
- dict[str,float] -> diccionario donde las claves son cadenas de texto y los valores son flotantes/decimales

+ **multiples**

en el caso que queramos indicar de un determinado parametro puede ser de un 'tipo o de otro' tenemos que especificarlo usando el operador '|'
en el caso que queramos ser dato de tipo tupla o diccionario
- tuple|dict -> puede ser dato de tipo tupla o diccionario
- list[str|int] -> lista cuyos elementos pueden ser cadena de texto o enteros
- dict[str|float|int] -> diccionario cuya clave puede ser texto, decimal o entero, y valor lo mismo.

## closure
una closrue (clausura) son funciones que establecen una funcion interior,o retorna una funcion estas funciones se carcterizan por recordar el valor de los argumentos que se le pasan 
```python
    def multiplicando(n):
      def multiplicador(m):
        return n*m
    return multiplicador  

```
# FUNCION EN PYTHON

## 1. FUNCIONES BÁSICAS
```python
def calcular_area_rectangulo(base, altura):
    return base * altura

print(calcular_area_rectangulo(5, 4))
```

## 2. PARÁMETROS NOMINALES O POR DEFECTO
```python
def calcular_precio_final(precio, impuesto=0.18, descuento=0.0):
    return precio * (1 + impuesto) * (1 - descuento)

print(calcular_precio_final(precio=100, impuesto=0.18, descuento=0.10))
print(calcular_precio_final(100))
```

## 3. TYPE HINTS
```python
def calcular_promedio(numeros: list[float]) -> float:
    if len(numeros) == 0:
        return 0
    return sum(numeros) / len(numeros)

print(calcular_promedio([10, 20, 30]))
```

## 4. EMPAQUETADO NOMINAL (**kwargs)
```python
def crear_perfil(nombre, **datos):
    perfil = {"nombre": nombre}
    perfil.update(datos)
    return perfil

print(crear_perfil("Ana Luz", edad=20, ciudad="Puquio", carrera="Sistemas"))
```

## 5. EMPAQUETADO POSICIONAL (*args)
```python
def sumar_todo(*numeros):
    return sum(numeros)

print(sumar_todo(1, 2, 3, 4, 5))
print(sumar_todo(10, 20))
```

## 6. FUNCIONES ANÓNIMAS (lambda)
```python
area = lambda base, altura: base * altura
print(area(5, 4))

mayor = lambda a, b: a if a > b else b
print(mayor(10, 25))
```

## 7. DOCUMENTACIÓN (docstring)
```python
def calcular_potencia(base: float, exponente: float) -> float:
    """
    Calcula la potencia de un número.
    Parámetros:
    base (float): número base.
    exponente (float): exponente al que se eleva.
    Retorna:
    float: resultado de base ** exponente.
    Ejemplo:
    >>> calcular_potencia(2, 3)
    8.0
    """
    return base ** exponente

print(calcular_potencia(2, 3))
print(calcular_potencia.__doc__)
```

## 8. Closure
```python
def crear_contador():
    contador = [0]
    def incrementar():
        contador[0] += 1
        return contador[0]
    return incrementar

mi_contador = crear_contador()
print(mi_contador())
print(mi_contador())
print(mi_contador())
```

## 9. Programacion funcional
Python es un lenguaje de programacion multidigma, y uno de sus paradigmas que mejor funcion tiene es la funcional.
Python usa, tres map(), filter(), reduce(), pero nosotros solo usaremos map(), filter(), estas funciones integradas de python sirven para procesar y transformar colecciones de datos (listas, diccionarios) de manera muy eficiente.

> [!TIP] Importante:
> las funciones map() y filter() reciben 2 parametros primero la funcion a ejecutar y segundo el iterable en el que va a actuar. la funcion que recibe como parametro puede ser normal o puede ser anonima (lambda)

### 1. map()
map aplica una funcion especifica a cada uno de los elementos de una coleccion (iterables) y devuelve un nuevo iterable con los resultados
```python
# de una lista de numeros deseamos calcular, la potencia de cada numero
numeros = [2, 7, 8, 20, 4, 3, 9, 12, 11, 16, 17]

## cuando deseamos trabajar con una funcion anonima tenemos que declarar primero la funcion antes de pasarla por parametro.
def f(x):
    ## una vez creada pasamos la funcion como parametro
    return x**2

## cuando deseamos trabajar con funciones anonimas usamos lambda dentro del parametro
print(list(map(f, numeros)))
print(list(map(lambda x: x**2, numeros)))
# [4, 49, 64, 400, 16, 9, 81, 144, 121, 256, 289]
```

### 2. filter():
filter pasa cada elemento de una coleccion por una funcion y solo se queda con aquellos elementos donde la funcion devuelva true (es decir filtra los datos en una condicion)
```python
# imagina que tienes una lista de numeros y solo quieres quedarte con los numeros pares.
numeros: list[int] = [2, 7, 8, 20, 4, 3, 9, 12, 11, 16, 17]

print(list(filter(lambda x: x % 2 == 0, numeros)))
# [2, 8, 20, 4, 12, 16]
```

> [!WARNING] Nota Importante:
> Tanto map() como filter() NO devuelven listas directamente, sino iteradores, esto es para ahorrar memoria (evaluacion perezosa o lazy evaluation), si quieres ver el resultado como una lista tradicional, siempre debes envolver en list().

## listas por   compresion 
# listas por comprensión
num:list[int]=[2,3,4,6,7,9,11,12,15,17,18]
por_diez:list[int]=[n*10 for n in num if n%2==0]
print(por_diez)
cuadrados:list[int]=[n**2 for n in num if n%2==0]
print(cuadrados)

# diccionarios por comprensión
pares_x10:dict[int,int]={n:n*10 for n in num if n%2==0}
print(pares_x10)
cuadrados_dict:dict[int,int]={n:n**2 for n in num if n%2==0}
print(cuadrados_dict)