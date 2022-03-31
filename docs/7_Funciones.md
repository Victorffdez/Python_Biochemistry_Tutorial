## **¿Qué es una función?**
Una **función** es un bloque de código que ha sido diseñado para realizar una tarea, y que una vez definida puede utilizarse en el momento que se desee.

Es decir, si tiene que realizar una misma tarea varias veces, en lugar de repetir una y otra vez el código, lo más eficiente es definirlo en una función y utilizarlo de forma mucho más simple. Esto hace que el código sea más ^^legible^^ y ^^limita los errores^^ de escritura.

A continuación aprenderá a trabajar con funciones, aunque de hecho ya ha las ha estado utilizando. A lo largo del tutorial ha utilizado funciones básicas como *print ()* o *len ()*, ya implementadas en Python.
## **Definir y llamar una función**
Las funciones en Python se crean usando la palabra clave ***def***, seguida de un nombre de función y parámetros de función entre paréntesis. Veamos un ejemplo:
``` py
>>> def saludar_usuario ():
...     print ("¡Hola a todos!")
```

Esta es la estructura más simple para definir una función. En este caso, la función se denomina *saludar_usuario ()*, y como para esta tarea no se necesita información, los paréntesis no contienen parámetros (aunque es ^^fundamental^^ incluirlos). Tras los dos puntos, las siguientes líneas sangradas forman el denominado **cuerpo de la función** que contiene la tarea a realizar, en este caso un saludo al usuario.

### ***Llamada***
Para llamar a una función, hay que escribir su nombre seguida de la información que sea necesaria entre paréntesis.

* En el caso de la función *print ()*, como ya se habrá dado cuenta, es necesario escribir entre los paréntesis información, si no esta dará error.
* Al contrario, en la función anterior no es necesaria información, por lo que simplemente definiéndola ya dará el resultado esperado.
``` py
>>> saludar_usuario ()
¡Hola a todos!
```

## **Modificar la función**
### ***Parámetro y argumento***
Si deseamos que la función salude a una persona en concreto, tenemos que incluir **parámetros** de la función entre paréntesis. Ahora Python esperará que proporcionemos un valor a esta función. Veamos dos ejemplos:
``` py
>>> def saludar_usuario (usuario):
...     print (f"¡Hola {usuario}!")
>>> saludar_usuario ("Victor")
¡Hola Victor!
```
``` py
>>> def multiplicacion (a, b):
...     return (a*b)
>>> resultado = multiplicacion (7,5)
>>> multiplicacion
35
```
Aunque a veces se pueden llegar a utilizar de forma similar, es importante tener claro dos conceptos:

* **Parámetro**: usuario; a,b.
* **Argumento**: Víctor; 7,5.

Como observará en el segundo ejemplo, Python asocia cada argumento introducido con un parámetro (a-7, b-5). Esta asociación es muy importante, ya que podemos obtener algún resultado inesperado si mezclamos argumentos al llamar la función.
``` py
>>> def saludo (nombre, profesion):
...     print (f"Me llamo {nombre} y soy {profesion}.")
>>> saludo("estudiante", "Victor")
Me llamo estudiante y soy Victor.
```

Observe que cuando llama a la función, PyCharm le indica sobre qué parámetro está escribiendo su argumento. Esto es muy útil y evita muchos errores de escritura como el anterior. Otra forma de solucionarlo es utilizar los **argumentos de palabra clave**.
``` py
>>> def saludo (nombre, profesion):
...     print (f"Me llamo {nombre} y soy {profesion}.")
>>> saludo(profesion="estudiante", nombre="Victor")
Me llamo Victor y soy estudiante.
```

Al escribir una función, podemos definir un **argumento predeterminado** para cada parámetro. Si se utilizan argumentos predeterminados, no es necesario incluirlos al llamar la función. 
``` py
>>> def saludo (nombre, profesion="estudiante"):
...     print (f"Me llamo {nombre} y soy {profesion}.")
>>> saludo("Victor")
Me llamo Victor y soy estudiante.
```

!!! note "Argumentos predeterminados"

    Tenga en cuenta que no es posible utilizar un argumento predeterminado antes que un parámetro no prederminado. Por lo tanto, en primer lugar escriba todos los valores no predeterminados.

### ***Cuerpo de la función***
En el cuerpo de una función se pueden encontrar todo tipo de estructuras, desde estructuras de datos simples como listas, hasta estructuras de control como bucles. 
!!! example "BUCLE FOR. Sumatorio de una lista."

    ``` py
        >>> def sumatorio(lista):
        ...     suma=0
        ...     for x in range(len(lista)):
        ...         suma=suma+lista[x]
        ...     print(suma)
        >>> lista = [3,5,6,7]
        >>> sumatorio(lista)
        21
    ```

!!! example "SENTENCIA IF-ELSE. Mayor/menor de una lista."

    ``` py
        >>> def mayormenor(lista):
        ...    may=lista[0]
        ...    men=lista[0]
        ...    for x in range(1,len(lista)): #Esta función se definió en las cadenas de caracteres
        ...        if lista[x]>may:
        ...            may=lista[x]
        ...        else:
        ...            if lista[x]<men:
        ...                men=lista[x]
        ...    print("El valor mayor de la lista es", may)
        ...    print("El valor menor de la lista es", men)
        >>> lista = [3,5,6,7]
        >>> mayormenor(lista)
        El valor mayor de la lista es 7
        El valor menor de la lista es 3
    ```

### ***Funciones ya definidas***
Como se ha comentado anteriormente, Python ya contiene algunas funciones que puede utilizar denominadas [**funciones Built-in**](https://docs.python.org/es/3.8/library/functions.html). En el apartado _Estructuras de datos_ puede encontrar algunos ejemplos ya utilizados como _len ()_, _max ()_ o _reverse ()_. A continuación puede encontrar otros ejemplos:

| FUNCIÓN | DESCRIPCIÓN | 
|:--:|:--:|
| `chr()`  | Convierte el número entero que representa el código Unicode en el carácter correspondiente| 
|  `input()` | Permite recibir información del usuario, convirtiéndola en una cadena |  
|  `sorted()`	 |  Devuelve una lista ordenada |
|  `help()` |  Obtener información acerca de un argumento indicado |  
|  `abs()` |  Devuelve el valor absoluto de un número |
|  `id()` |  Retorna la identidad de un objeto  |   

## **Módulos**

## **Ejercicios**