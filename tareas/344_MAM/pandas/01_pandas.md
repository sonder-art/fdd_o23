Tarea: Investiga como funciona apply. Revisa que tienes que hacer si quieres aplicarlo por columna o por row
Función apply es una herramienta que permite aplicar una función personalizada a filas o columnas de un DataFrame. 
2 maneras principales de usarlo: aplicarlo por columna o por fila.
  1. Aplicar apply por columna: se puede usar el método en un DataFrame y especificar el eje (axis) como 0. 
      Esto significa que la función personalizada se aplicará a cada columna del DataFrame. 
      Ejemplo:
              import pandas as pd
              
              # Crear un DataFrame de ejemplo
              data = {'A': [1, 2, 3], 'B': [4, 5, 6]}
              df = pd.DataFrame(data)
              
              # Definir una función personalizada para aplicar a cada columna
              def mi_funcion(columna):
                  return columna * 2
              
              # Aplicar la función a cada columna
              resultado = df.apply(mi_funcion, axis=0)
              print(resultado)

  En este ejemplo, la función mi_funcion se aplica a cada columna del DataFrame df. 
  El resultado será un nuevo DataFrame donde cada columna ha sido modificada de acuerdo con la función.

2. Aplicar apply por fila: se puede usar el método en un DataFrame y especificar el eje (axis) como 1. 
      Esto significa que la función personalizada se aplicará a cada fila del DataFrame. 
      Ejemplo:
          import pandas as pd
          
          # Crear un DataFrame de ejemplo
          data = {'A': [1, 2, 3], 'B': [4, 5, 6]}
          df = pd.DataFrame(data)
          
          # Definir una función personalizada para aplicar a cada fila
          def mi_funcion(fila):
              return fila.sum()
          
          # Aplicar la función a cada fila
          resultado = df.apply(mi_funcion, axis=1)
          print(resultado)

    En este ejemplo, la función mi_funcion se aplica a cada fila del DataFrame df. 
    El resultado será una Serie de Pandas que contiene el resultado de aplicar la función a cada fila.

              
Tarea: Investiga como funciona pd.concat. Revisa que tienes que hacer si quieres pegar cols o rows, y que pasa 
si los DataFrames tiene indices repetidos. 

La función pd.concat en Pandas se utiliza para combinar (concatenar) DataFrames a lo largo de un eje específico,
ya sea horizontalmente (pegar columnas) o verticalmente (pegar filas). 
También puede utilizarse para combinar DataFrames con índices repetidos.
La función tiene varios parámetros que te permiten personalizar cómo se realiza la concatenación.

  1. Pegar columnas (horizontalmente): Debes asegurarte de que los DataFrames tengan los mismos índices (si es relevante) 
    y luego utilizar pd.concat con axis=1. 
    Ejemplo:
          python
          Copy code
          import pandas as pd
          
          # Crear dos DataFrames
          df1 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
          df2 = pd.DataFrame({'C': [7, 8, 9], 'D': [10, 11, 12]})
          
          # Pegar columnas horizontalmente
          resultado = pd.concat([df1, df2], axis=1)
          print(resultado)

  2. Pegar filas (verticalmente): Debes asegurarte de que las columnas tengan los mismos nombres (si es relevante) 
      y luego utilizar pd.concat con axis=0. 
      Ejemplo:
          python
          Copy code
          import pandas as pd
          
          # Crear dos DataFrames
          df1 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
          df2 = pd.DataFrame({'A': [7, 8, 9], 'B': [10, 11, 12]})
          
          # Pegar filas verticalmente
          resultado = pd.concat([df1, df2], axis=0)
          print(resultado)

Manejo de índices repetidos: Si los DataFrames tienen índices repetidos, puedes utilizar el parámetro ignore_index 
    para restablecer los índices en el resultado concatenado. 
    Ejemplo:
          python
          Copy code
          import pandas as pd
          
          # Crear dos DataFrames con índices repetidos
          df1 = pd.DataFrame({'A': [1, 2, 3]}, index=[0, 1, 2])
          df2 = pd.DataFrame({'A': [4, 5, 6]}, index=[2, 3, 4])
          
          # Pegar filas verticalmente y restablecer índices
          resultado = pd.concat([df1, df2], axis=0, ignore_index=True)
          print(resultado)