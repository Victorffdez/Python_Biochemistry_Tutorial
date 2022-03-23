Una **estructura de datos** es una colección de datos (normalmente de tipo simple) que se caracterizan por su organización y las operaciones que se definen en ellos. Por tanto, una estructura de datos vendrá caracterizada tanto por unas ciertas relaciones entre los datos, como las operaciones posibles en ella. 

Dentro de las diferentes estructuras de datos destacan:

* Listas. 
* Tuplas.
* Conjuntos.
* Diccionarios

## **Listas**
Una **lista** es una colección de elementos en un orden particular, y son el tipo de objeto colección ordenada más flexible en Python, pudiendo albergar objetos de cualquier tipo de datos, como números, cadenas u otras listas anidadas.

En Python, los corchetes ([ ]) indican una lista, y dentro, los elementos individuales se separan por comas. A continuación tiene unos ejemplos de posibles listas.
``` py
>>> numeros = [0,1,2,3,4,5]
>>> diccionario = ['mutación', 'nucleótido']
>>> lista = [0,1,2, 'mutación']
>>> lugar_fecha = [ ['Córdoba', 2022], ['Madrid', 2021] ] 
# El último es un ejemplo de lista que contiene otras listas
```
Si pedimos a Python que imprima por pantalla esta lista, nos devolverá lo siguiente.
``` py
>>> numeros 
[0,1,2,3,4,5]
```
!!! note "Elementos de una lista"

    Tenga en cuenta que al definir una lista se puede hacer referencia a otras variables. Esto será realmente útil.
    ``` py
    >>> cadena_ADN = 'ATAGCGCGCATT'
    >>> num_cromosoma = 14
    >>> lista = [cadena_ADN, num_cromosoma]
    >>> lista
    ['ATAGCGCGCATT', 14]
    ```

### ***Acceder a los elementos***
Podemos acceder a cualquiera de los elementos de una lista indicando a Python la posición del elemento deseado. Para ello, escriba el nombre de la lista seguido del índice del elemento entre corchetes.
``` py
>>> lista = ['A','T','G','C']
>>> lista [0]
A
>>> lista [-1]
C
# El orden de los elementos es 0,1,2,3...-3,-2,-1.
```

### ***Cambiar, añadir y eliminar elementos***
Para sustituir un elemento en la lista, use el nombre de la lista seguido del índice del elemento que desea modificar y del nuevo valor que desea.
``` py
>>> celula = ['membrana','nucleo','pared','citosol']
>>> lista [2]
pared
>>> lista[2] = 'organulos'
>>> lista [2]
organulos
```

En lugar de sustituir un elemento, puede interesarle añadir uno nuevo. La forma más sencilla de hacerlo es utilizando el método *append ()*.

``` py
>>> celula = ['membrana','nucleo','pared','citosol']
>>> celula.append ('organulos')
>>> celula
['membrana','nucleo','pared','citosol', 'organulos']
```
Como se observa, el elemento *organulos* se añade al final de la lista. Podemos añadir un elemento en cualquier posición con el método *insert ()*. Para esto, habrá que especificar el índice del nuevo elemento y su valor. 
``` py
>>> celula = ['membrana','nucleo','pared','citosol']
>>> celula.insert (0,'organulos')
>>> celula
['organulos', 'membrana','nucleo','pared','citosol']
```

Si en lugar de añadir elementos, desea eliminarlos, hay distintas formas para hacerlo. 

* ^^Sentencia _del_^^. Esta se utiliza para eliminar un elemento en particular, del que conocemos la posición.
``` py
>>> celula = ['membrana','nucleo','pared','citosol']
>>> del celula[2]
>>> celula
['membrana','nucleo','citosol']
```
* ^^Método _remove_^^. Este se utilizará si desconocemos la posición del elemento que deseamos eliminar, solo conocemos su valor.
``` py
>>> celula = ['membrana','nucleo','pared','citosol']
>>> celula.remove(pared)
>>> celula
['membrana','nucleo','citosol']
```
!!! note "Método remove"

    Tenga en cuenta que este método solo eliminará la primera aparición del valor. Si este está repetido en la lista, habrá que utilizar un bucle. Se verá como realizarlo en el siguiente apartado.

* ^^Método _pop ()_^^. Elimina el elemento de una lista, pero permite trabajar con él después de quitarlo. 
``` py
>>> celula = ['membrana','nucleo','pared','citosol']
>>> celula_pop = celula.pop (2)
>>> celula
['membrana','nucleo','citosol']
>>> celula_pop
nucleo
```

### ***Otras funciones***

* ***Count ()***. Este método recibe un elemento como argumento, y cuenta la cantidad de veces que aparece en la lista.
``` py
>>> celula = ['membrana','nucleo', 'membrana', 'membrana', pared','citosol']
>>> celula.count(membrana)
3
```
* ***Sort ()***. Este método ordena la lista alfabéticamente.
``` py
>>> celula = ['membrana','nucleo','pared','citosol']
>>> celula_sort ()
>>> celula
['citosol','membrana','nucleo','pared']
```

* ***Reverse ()***. Este método invierte el orden original de la lista.
``` py
>>> celula = ['membrana','nucleo','pared','citosol']
>>> celula_reverse ()
>>> celula
['citosol','pared','nucleo','membrana']
```

!!! note "Método reverse ()"

    Observe que este método no genera un orden alfabético inverso, simplemente invierte el orden de la lista. Para realizarlo, tendría que utilizar previamente sort (). 

* ***Len ()***. Este método devuelve la longitud de la lista, es decir, el número de elementos que la componen.
``` py
>>> celula = ['membrana','nucleo','pared','citosol']
>>> len (celula)
4
```

* ***min () / max ()***. Este método devuelve el valor mínimo o máximo de una lista.
``` py
>>> edad = [40, 33, 25, 86, 67]
>>> min (edad)
25
```
## **Tuplas**

## **Conjuntos**

## **Diccionarios**

