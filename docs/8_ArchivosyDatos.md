Como bioquímico, en la mayoría de ocasiones necesitará trabajar con **archivos y datos** en Python. Por ese motivo, en este apartado aprenderá conceptos básicos relacionados con la lectura y manipulación de archivos, y la importación/exportación de datos.

## **Trabajar con un archivo**
### ***Lectura***
Para poder aprender a trabajar con un archivo de texto (_.txt_), necesitará crear uno utilizando el editor de texto que desee o el propio IDE. Es fundamental que almacene este archivo en el mismo directorio donde esté trabajando. 

A continuación le proponemos un ejemplo, en este caso un archivo que contiene el número pi (10 decimales por línea).
``` title="num_pi.txt"
3.1415926535 
  8979323846
```
Una vez creado el archivo, veamos como **abrirlo e imprimir** el contenido en la pantalla en un archivo _.py_.
``` py title="leer_pi.py"
>>> with open ("num_pi.txt") as file_object:
...    contenido = file_object.read()
>>> print (contenido)
```

* **Función open()**. Le indica a Python qué archivo deseamos abrir, buscándolo en el mismo directorio que *leer_pi.py*.
* **File_object**. La función open () devuelve un objeto, que lo asignaremos a esta variable.
* **Función read()**. Lee todo el contenido del archivo y lo guarda como una cadena denominada *contenido*. Una vez creada la cadena, la imprimimos por pantalla.

!!! note "Eliminar línea en blanco"

    Se habrá dado cuenta que al final de la salida se muestra una línea en blanco que no estaba en el archivo original. Si la quiere eliminar, utilice **rstrip()** al utilizar la función _print()_.

Aunque existe probabilidad de que su archivo *.txt* se encuentre en el mismo directorio de trabajo, normalmente estará en otro diferente. Para que Python pueda abrir y leer archivos de un directorio distinto, debe incluir la **ruta de archivo**. 
``` py title="leer_pi.py"
>>> with open ("C:\\Users\\Downloads\\num_pi.txt") as file_object:
...    contenido = file_object.read()
>>> print (contenido)
```
También podría asignar una variable a esta ruta y utilizarla en la llamada.
``` py title="leer_pi.py"
>>> ruta_archivo = "C:\\Users\\Downloads\\num_pi.txt"
>>> with open (ruta_archivo) as file_object:
...    contenido = file_object.read()
>>> print (contenido)
```
!!! info "Ruta de archivo"

    En la ruta de archivo, habrá observado que se utilizan **barras dobles** (\\) en lugar de una barra simple (\) como de constumbre. La barra simple se utiliza en Python para introducir algun caracter especial, como \n para un salto de línea. Por este motivo se deben utilizar dobles en la ruta de archivo. 
    
    Si lo desea, para evitar esto puede utilizar **barras hacia delante** (/) para indicar la ruta. 

#### *Línea a línea*
Si desea examinar cada línea al leer un archivo, puede incluir un bucle for en el objeto del archivo.
``` py title="leer_pi.py" 
>>> archivo = "num_pi.txt" #Asignamos el nombre del archivo a una variable
>>> with open (archivo) as file_object:
...    for linea in file_object:
...    print(linea)
```
Esto dará como resultado la siguiente salida:
```  
3.1415926535 

  8979323846
  
```
De nuevo, puede utilizar **rstrip()** en la función _print()_ para eliminar las líneas en blanco.

### ***Acciones***
#### *Crear una lista*
Podemos guardar todas las líneas que componen un archivo en una lista, para poder trabajar con esta como hemos visto a lo largo del tutorial. A continuación se muestra cómo crear esta lista e imprimirla.
``` py title="lista_pi.py" 
>>> archivo = "num_pi.txt" 
>>> with open (archivo) as file_object:
...    lineas = file_object.readlines()

>>  for linea in lineas:
       print(linea.rstrip())
```
El método utilizado **readlines()** lee cada línea de un archivo y la almacena en una lista. 

#### *Crear una cadena*
Imagine que está trabajando con un archivo FASTA y desea crear una cadena con todos los caracteres, ya sean nucleótidos o aminoácidos, para poder trabajar con esta cadena de forma sencilla.
``` py title="cadena_pi.py" 
>>> archivo = "num_pi.txt" 
>>> with open (archivo) as file_object:
...    lineas = file_object.readlines()
>>> cadena_pi = ""  #Creamos una variable para almacenar los caracteres
>>  for linea in lineas:
       cadena_pi+= linea.rstrip() 
```
Si imprime esta cadena, el resultado será el siguiente:
```  
3.1415926535   8979323846 
```
Para eliminar el espacio en blanco, en lugar de _rstrip()_ debe utilizar **strip()**. Ya tiene almacenados todos los caracteres en una cadena, y puede trabajar con la misma.
``` py
>>> longitud = len(cadena_pi)
>>> longitud
22
```
``` py
>>> fragmento_problema = "99843"
>>> if fragmento_problema in cadena_pi:
...    print ("El fragmento aparece.")
>>> else:
...    print ("El fragmento no aparece.")
```
#### *Escribir*
Si desea escribir texto en un archivo _.txt_ vacío, debe indicárselo a Python en la función _open()_.
``` py title="escribir_archivo.py" 
>>> archivo = "nuevo_archivo.txt" 
>>> with open (archivo, "w") as file_object: 
...    file_object.write("¡Estoy escribiendo un archivo!")
```
!!! info ""w""

    Podemos abrir el archivo en modo escritura _"w"_, lectura _"r"_ (por defecto), anexo _"a"_ y lectura-escritura _"r+"_.

## **Importar/Exportar datos**
Python soporta una gran variedad de archivos de datos, aunque a continuación se enseñará a importar los tipos de archivos de datos más empleados: ***.txt***, con los que se ha enseñado previamente a trabajar; y ***.csv***. Las siglas _CSV_ vienen del inglés _"Comma Separated Values"_, siendo valores separados por comas.
### ***NumPy***
Una de las librerías disponibles para el manejo de datos es **NumPy**. NumPy es una librería de Python especializada en el cálculo numérico y el análisis de datos, principalmente en la operación con funciones matemáticas.

* Para importar un archivo _.txt_:

``` py
>>> import numpy as np
>>> datos = np.loadtxt("archivo.txt", delimiter=",") #El delimitador por defecto es un espacio en blanco
```
Si el delimitador tiene cabecera, podemos saltar esta fila con **skyprows**, y para trabajar con columnas utilizamos el argumento **usecols**. Si nuestro archivo contiene valores no numéricos , utilizaremos loadtxt()**astype(str)**. 

``` py
>>> import numpy as np
>>> datos = np.loadtxt("archivo.txt", delimiter=",", skiprows=1, usecols=[0,1]).astype(str)
    #Importa las columnas 1 y 2 del archivo.txt, delimitadas por coma, eliminando la primera fila de cabecera.
    # Una de estas columnas contiene valores no numéricos. 
```

En el siguiente [enlace](https://numpy.org/doc/stable/reference/generated/numpy.loadtxt.html) puede encontrar más funciones que le serán útiles.

* Para importar un archivo _.csv_:

``` py
>>> import numpy as np
>>> datos = np.recfromcsv("datos.csv")
```
### ***Pandas***
La **librería Pandas** ayuda a llevar a cabo todo el trabajo de análisis de datos en Python de una forma fluida y rápida. En este caso los datos importados se almacenan en un ^^dataframe^^, que no es más que un conjunto de observaciones y variables (muy empleado en lenguajes como R). 

Para importar un archivo _.csv_:
``` py
>>> import pandas as pd
>>> dataframe = pd.read_csv("datos.csv")
```
Al igual que con NumPy, se pueden incluir argumentos como **nrows**, que limita el número de filas; funciones como **head()** y **tail()**, que limita la visualización de datos... Puede encontrar una guía ampliada en el siguiente [enlace](https://www.analyticsvidhya.com/blog/2021/05/pandas-functions-13-most-important/). 

En la **exportación de datos** se trabaja de forma muy similar a la importación. Para exportar los datos a un archivo _.csv_ le recomiendo emplear _Pandas_, ya que resulta realmente fácil y rápido:
``` py
>>> import pandas as pd
>>> df.to_csv("archivo.csv")
```

### ***Otros archivos***
De forma similar a como se trabaja con archivos _.csv._, con _Pandas_ puede trabajar archivos de diferentes extensiones. A continuación se muestran algunas funciones que le pueden resultar de utilidad.

| FORMATO | IMPORTAR | EXPORTAR |
|:--:|:--:|:--:|
| `csv`  | pd.read_csv()| df.to_csv()|
|  `json` | pd.read_json() | df.to_json()| 
|  `excel`	 |  pd.read_excel() | df.to_excel()|
|  `sql` |  pd.read_sql() |  df.to_sql()|

!!! cite "Enlaces de interés"

    * [**Aprende Python.** Sergio Delgado Quintero (2022).](https://aprendepython.es/_downloads/907b5202c1466977a8d6bd3a2641453f/aprendepython.pdf)
    * [**Importar y Guardar datos en Python con Pandas.** Pro Ciencia.](https://www.youtube.com/watch?v=nM_X7TGQqY0&ab_channel=ProCiencia)

