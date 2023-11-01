'''
Define un decorador llamado `registrar_actividad` que, cuando se aplique a un método, registre la actividad en un archivo llamado `registro.txt`. La actividad debe tener el formato: "`[FECHA Y HORA]` - Se ejecutó el método `[NOMBRE DEL MÉTODO]` con los argumentos: `[ARGUMENTOS]`".


Crea una clase llamada Usuario con los siguientes métodos:
        `crear(nombre, apellido)`: establece el nombre y apellido del usuario.
        `obtener_info()`: devuelve el nombre y apellido del usuario.
        `modificar(nombre, apellido)`: modifica el nombre y apellido del usuario.

Asegúrate de aplicar el decorador `registrar_actividad` a estos métodos.

Implementa la lógica para registrar la actividad utilizando el contexto with para manejar el archivo `registro.txt`.
'''
import datetime
import time
import os

def registrar_actividad(funcion):
    def wrap(*args, **kwargs):
        with open("registro.txt", "a") as archivo:
            archivo.write(f"[{datetime.datetime.now()}] - Se ejecutó el método {funcion.__name__} con los argumentos: {args}\n")
        return funcion(*args, **kwargs)
    return wrap

class Usuario:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    @registrar_actividad
    def crear(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    @registrar_actividad
    def obtener_info(self):
        return self.nombre, self.apellido

    @registrar_actividad
    def modificar(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
        
'''
Define un decorador llamado medir_tiempo que registre el tiempo que tarda en ejecutarse la función decorada. 
El decorador debe escribir el tiempo de ejecución, junto con el nombre de la función, 
y el tamano del arreglo, en el archivo tiempos.txt, **separados por comas**. 
Basicamente un `csv` donde se guarden los tiempos de ejecucion.  

La primera linea del archivo debe de representar el nombre de las columnas, las siguientes lineas representan las observaciones:
`funcion,n,tiempo`.

Ejecuta las funciones con diferentes valores de n = [10, 1000, 10000, 100000, 1000000, 5000000] para generar datos en tiempos.txt.  
Corre cada funcion al menos unas 5 veces para cada tamanno del arreglo.
Asegurate de no sobreescribir el archivo txt para que no se elimine la ejecucion.
'''

def medir_tiempo(funcion):
    def wrap(*args, **kwargs):
        start = time.time()
        result = funcion(*args, **kwargs)
        end = time.time()

        # Check if the file exists
        flag = os.path.exists("tiempos.txt")

        # Open the file in append mode
        with open("tiempos.txt", "a") as archivo:
            # If the file didn't exist, write the header
            if not flag:
                archivo.write("funcion,n,tiempo\n")
            
            # Write the data
            archivo.write(f"{funcion.__name__},{len(args[0])},{end-start}\n")

        return result
    return wrap


import numpy as np
import pandas as pd
import polars as pl


@medir_tiempo
def sumar_lista(n):
    lista = [i for i in range(n)]
    return sum(lista)

@medir_tiempo
def sumar_tupla(n):
    tupla = tuple(i for i in range(n))
    return sum(tupla)

@medir_tiempo
def sumar_objeto(n):
    class ClaseEjemplo:
        def __init__(self, numero):
            self.numero = numero
            
    objetos = [ClaseEjemplo(i) for i in range(n)]
    return sum(obj.numero for obj in objetos)

@medir_tiempo
def sumar_usando_yield(n):
    def generador():
        for i in range(n):
            yield i
            
    return sum(generador())

@medir_tiempo
def sumar_conjunto(n):
    conjunto = set(range(n))
    return sum(conjunto)

@medir_tiempo
def sumar_valores_diccionario(n):
    diccionario = {i: i for i in range(n)}
    return sum(diccionario.values())

@medir_tiempo
def sumar_numpy_array(n):
    array = np.arange(n)
    return np.sum(array)

@medir_tiempo
def sumar_pandas_series(n):
    serie = pd.Series(range(n))
    return serie.sum()

@medir_tiempo
def sumar_polars_series(n):
    serie = pl.Series("valores", list(range(n)))
    return serie.sum()

for n in [10, 1000, 10000, 100000, 1000000, 5000000]:
    print("entró")
    sumar_lista(n)
    sumar_tupla(n)
    sumar_objeto(n)
    sumar_usando_yield(n)
    sumar_conjunto(n)
    sumar_valores_diccionario(n)
    sumar_numpy_array(n)
    sumar_pandas_series(n)
    sumar_polars_series(n)