Las **estructuras de control** son aquellas que permiten modificar el flujo normal de ejecución de instrucciones de un programa, dependiendo del resultado de unas condiciones.

Estas estructuras nos permiten realizar acciones típicas en nuestros scripts, como pueden ser bucles o la toma de decisiones.

<figure markdown>

  ![estcontrol](estructuras_control.png){ width="700" height="500" }
   <figcaption> Lógica de Programación. Universidad Politécnica de Puebla (UPP). </figcaption>

</figure>

## **Bucles FOR**

Un **bucle** es una estructura de control que repite un bloque de instrucciones, denominado _cuerpo_, siendo cada repetición conocida como _iteración_. En el caso del **bucle for**, se repite el bloque de instrucciones un número determinado de veces.

Los bucles nos permiten realizar las mismas acciones con los elementos de una lista, como puede ser realizar una misma operación matemática con cada elemento.

### ***Sintaxis***

Si tiene una lista con diferentes elementos, como distintos tipos de proteínas, y quiere imprimir por pantalla todos los nombres, puede hacerlo de forma individual como ya se enseñó anteriormente. Esto nos conduce a los siguientes problemas:

* Código muy repetitivo.
* Trabajo lento y poco eficiente.
* Cada vez que se altere la longitud de la lista, cambiar el código.

Por este motivo, utilizaríamos la siguiente estructura.

``` py
>>> proteinas = ['hemoglobina','caseina','lacasa','albumina']
>>> for proteina in proteinas:
...     print (proteina)
```
En este caso, se ha definido la lista *proteinas*, y el bucle for le indica a Python que cada elemento de esta lista se asocie con la variable *proteina*. Posteriormente, se indica que imprima cada elemento que se ha ido asignando a la variable *proteina*. La salida será la siguiente:
``` py
hemoglobina
caseina
lacasa
albumina
```
Por tanto, Python va imprimiendo el valor actual de la variable *proteina*, que va cambiando al repetir el bucle. Cuando ya no hay más elementos en la lista, finaliza el programa. 

!!! info "Nomenclatura de la variable"

    Tenga en cuenta que puede elegir el nombre que quiera para la variable temporal. Se ha elegido en este caso *proteina* porque conviene utilizar nombres significativos, que representen los elementos de la lista. 

Es muy importante tener cuidado con las líneas sangradas. A veces, el bucle se puede ejecutar sin problemas pero que no produzca el resultado esperado. Veamos algunos ejemplos de esto:
``` py
>>> proteinas = ['hemoglobina','caseina','lacasa','albumina']
>>> for proteina in proteinas:
...     print (f"La {proteina} es una proteína.")
>>> print (proteina)
```
Este código imprime por pantalla el siguiente texto. Observe cómo en la última línea de código, únicamente se muestra el último elemento asociado a la variable *proteina*.
``` py
La hemoglobina es una proteína.
La caseina es una proteína.
La lacasa es una proteína.
La albumina es una proteína.
albumina
```

### ***Trabajar con bucles for***
#### *Función range ()*
La función *range ()* se utiliza principalmente para generar y trabajar con una serie de números. Veamos un ejemplo simple:
``` py
>>> for numero in range (1,4): #Imprime hasta el número n-1
...     print (numero)

>>> for valor in range (4): 
...     print (valor)
```
Esto daría lugar a la siguiente salida por pantalla:
``` py
1
2
3

0
1
2
3
```

#### *Función list ()*
Los resultados generados por la función range () pueden convertirse directamente en una lista. Para esto se utiliza la función list ().
``` py
>>> lista = list(range(2,19,2))
>>> lista
[2,4,6,8,10,12,14,16,18]
```
Observe que en este caso el rango determinado es *(2,19,2)*. Los dos primeros argumentos indican el rango de valor de los elementos (entre 2 y 19), y el tercero indica el tamaño de salto entre los valores (de 2 en 2).

### ***Ejemplo***
^^Tabla de multiplicar del 5^^

``` py linenums="1"
>>> for numero in range (11):
       multiplicacion = 5 * numero
       print (f"5 * {numero} = {multiplicacion}")
```
``` py 
5 * 0 = 0
5 * 1 = 5
5 * 2 = 10
5 * 3 = 15
5 * 4 = 20
5 * 5 = 25
5 * 6 = 30
5 * 7 = 35
5 * 8 = 40
5 * 9 = 45
5 * 10 = 50


```

## **Sentencias IF**



## **Bucles WHILE**

dd

## **Ejercicios**

