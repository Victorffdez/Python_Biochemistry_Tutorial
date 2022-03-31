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

Por este motivo, lo recomendable es utilizar la siguiente estructura.

``` py
>>> proteinas = ['hemoglobina','caseina','lacasa','albumina']
>>> for proteina in proteinas:
...     print (proteina)
```
En este caso, se ha definido la lista *proteinas*, y el bucle le indica a Python que cada elemento de esta lista se asocie con la variable *proteina*. Posteriormente, se indica que imprima cada elemento que se ha ido asignando a la variable *proteina*. La salida será la siguiente:
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

## **Condicional IF**
La estructura de control o **sentencia condicional if** permite que un programa ejecute una serie de acciones en función de si se cumple una determinada condición. 

Esta sentencia es la toma de decisión más básica, ya que consiste en comprobar si la **prueba condicional** es verdadera o falsa, y en base a esto, ejecutar o no el código que sigue a la sentencia.

### ***Sentencias if***
La sentencia if más simple está compuesta por dos elementos: una ^^prueba condicional^^ y una ^^acción^^. 
``` py
>>> organulo = 'ribosoma'
>>> if organulo == 'ribosoma':
...     print ("¡Era el organulo correcto!")
```
Como podrá comprobar, si no se cumple esta condición no se generaría ninguna salida.

!!! note "Sangrado"

    Al igual que ocurría anteriormente, es fundamental prestarle atención al sangrado. Después de la sentencia if, todas las líneas sangradas se ejecutarán si cumple la condición, y se ignorará todo el bloque si no se cumple.

### ***Sentencias if-else***
¿Qué ocurre si queremos que se genere una salida si no se cumple la condición? Para esto, utilizamos las **sentencias if-else**. 

El bloque if-else es equivalente a la sentencia if ya vista, pero incluye una sentencia else en la que se define una acción si la prueba condicional no es verdadera. Veámoslo con el mismo ejemplo de antes:
``` py
>>> organulo = 'vacuola'
>>> if organulo == 'ribosoma':
...     print ("¡Era el organulo correcto!")
>>> else:
...     print ("¡Ese no es el organulo!")
```
### ***Sentencias if-elif-else***
En muchas ocasiones, va a necesitar probar más de dos situaciones, y para ello es recomendable utilizar las **sentencias if-elif-else**. En este caso, Python va a ejecutar en orden las condiciones, y la primera que se cumpla será de la que ejecute su código asociado. Si ninguna de las condiciones es verdadera, ejecutará el código asociado a else como anteriormente.
``` py
>>> num_individuos = 1500
>>> if num_individuos < 1000:
...     print ("El numero de individuos es demasiado bajo")
>>> elif num_individuos > 5000:
...     print ("El numero de individuos es demasiado alto")    
>>> else:
...     print ("El numero de individuos para el muestreo es suficiente")
```

!!! info "Sentencias if-elif-else"

    Tenga en cuenta que puede utilizar múltiples bloques elif, añadiendo todas las pruebas condicionales que vea necesarias. Además, en este tipo de cadena Python no requiere un bloque else al final, por lo que puede omitirlo, siempre y cuando estos bloques elif engloben todas las posibles situaciones. Es decir, ha de cumplirse uno.  

### ***Combinación con listas***
La combinación de sentecias if con listas es especialmente útil. Veamos un ejemplo:
``` py
>>> proteinas = ['hemoglobina','glucosa','caseina','lacasa','albumina']
>>> for proteina in proteinas:
...    if proteina == 'glucosa':
          print(f"La {proteina} no es una proteína")
...    else:
          print (proteina)
     
```
### ***Ejemplo***
^^Comprobar si un numero es mayor a 0^^
``` py linenums="1"
>>> numero = int(input("Introduce un número:")) #Recibir un número por usuario
>>> if numero == 0:
       print("El número es igual a 0")
>>> elif numero > 0:
       print("El número es mayor a 0")
>>> else:
       print("El número es menor a 0")

#Tenga en cuenta que este es un ejemplo de las distintas opciones para realizar este ejercicio.
```

^^Divisores de un número^^
``` py linenums="1"
>>> numero = (int(input('Introduzca un numero:\n')))
>>> contador = 0
>>> print(f'Los divisores de {numero} son:')
>>> for divisor in range(1,numero+1):
        if (numero % divisor) == 0 :
            print(divisor,"es divisor")
            contador += 1
>>> print(f"El numero {numero} tiene {contador} divisores.") #Observe cómo esta sentencia queda fuera del bucle y condicional por el sangrado.
```


## **Bucles WHILE**
A diferencia de los bucles for, que ejecutan un bloque de código por cada elemento que compone la condición, los **bucles while** ejecutan el bloque de código siempre que se cumpla una condición determinada, dejándolo de repetir cuando sea falsa. 

Es decir, el bucle while nos permite realizar múltiples iteraciones basándonos en el resultado de una expresión lógica que puede tener como resultado un valor True o False.

### ***Sintaxis***
A continuación se muestra la sintaxis básica de un bucle while:
``` py
>>> i=1
>>> while (i<6):
...       print(f"Nº veces se ha completado el bucle:{i}")
...       i=i+1
>>> print("El bucle ha terminado")
```
En este caso, se ha definido la variable _i_, que aumentará una unidad cada vez que se complete el bucle. Cuando esta variable sea igual a 6, dejará de cumplirse la condición y finalizará el bucle.  

El resultado será el siguiente:
``` py
Nº veces se ha completado el bucle:1
Nº veces se ha completado el bucle:2
Nº veces se ha completado el bucle:3
Nº veces se ha completado el bucle:4
Nº veces se ha completado el bucle:5
El bucle ha terminado
```
!!! note "Bucle infinito"

    Es fácil cometer errores y programar un bucle infinito involuntariamente. Para parar este ciclo, presione ***Ctrl + C***.

### ***Trabajar con bucles while***
#### *Función break*
Existe una forma alternativa de interrumpir o cortar los ciclos: utilizando la palabra reservada _break_. Esta nos permite salir del ciclo incluso si la expresión evaluada en el bucle es verdadera.
``` py
>>> variable = int(input("Introduzca un valor >5 : "))
>>> while variable > 0:
...    print ("Actual valor de variable:", variable)
...    variable = variable -1
...    if variable == 5:
...        break
```

En este ejemplo, se muestra cómo el valor de la variable va disminuyendo una unidad hasta que sea igual a 5, finalizando el código. Observe cómo finaliza el código aunque el bucle while se siga cumpliendo (ya que el valor sigue siendo superior a 0).

#### *Función continue*
En lugar de interrumpir el bucle, podemos utilizar la sentencia _continue_ para volver al principio del bucle en función del resultado de la prueba condicional.

Veamos un ejemplo en el que un bucle imprime los números impares entre el 1 y el 20.
``` py
>>> num = 0
>>> while num <20:
...     num +=1
...     if num % 2 == 0:
...     continue
... print (num)
```

### ***Ejemplo***
^^Suma de n números enteros^^

``` py linenums="1"
>>> numero = int(input("Introduce un número: "))
>>> suma = 0
>>> x = 0
>>> while (x<=numero):
...    suma = suma+x
...    x=x+1
print(f'El resultado es {suma}')
```

## **Ejercicios**
**EJERCICIO 1**. Escribir un programa que le pida al usuario un número, y si es impar lo eleva al cuadrado, si no al cubo.
??? note "Respuesta"
    ``` py linenums="1"
        numero = int(input("Introduzca un número: "))
        if numero % 2 == 0:
           resultado = numero ** 3
        else:  
           resultado = numero ** 2
        print(resultado)
    ```
**EJERCICIO 2**. Escribir un programa que almacenen en una lista el cuadrado de los diez primeros números enteros.
??? note "Respuesta"
    ``` py linenums="1"
        squares = [] #Creación de una lista vacía 
        for value in range(1,11):
	        square = value**2
	        squares.append(square)
        print(squares)
    ```
**EJERCICIO 3**. Escribir un programa que le pida al usuario un número y le diga a qué día de la semana corresponde.
??? note "Respuesta"
    ``` py linenums="1"
        if dia == 1:
           print("Es lunes")
        elif dia == 2:
           print("Es martes")
        elif dia == 3:
           print("Es miercoles")
        elif dia == 4:
           print("Es jueves")
        elif dia == 5:
           print("Es viernes")
        elif dia == 6:
           print("Es sabado")
        else:
           print("Es domingo")
    ```
**EJERCICIO 4**. Escribir un programa que le pregunte al usuario una contraseña. Si coincide con contraseña, debe indicar que es correcta.
??? note "Respuesta"
    ``` py linenums="1"
        key = "contraseña"
        password = input("Introduce la contraseña: ")
        while password != key:
            print("La contraseña no coincide")
            password = input("Introduce la contraseña: ")
        print("La contraseña coincide")
    ```
**EJERCICIO 5**. Escribir un programa que calcule el factorial de un número introducido por el usuario.
??? note "Respuesta"
    ``` py linenums="1"
        numero = int(input("Introduzca un número:"))
        x=1
        resultado = 1
        while x <= numero:
            resultado= resultado*x
            x=x+1
        print(f'El factorial de {numero} es {resultado}')
    ```
**EJERCICIO 6**. Escribir un programa que calcule la suma de los n primeros números impares.
??? note "Respuesta"
    ``` py linenums="1"
        numero = int(input("Introduzca un valor:"))
        sumatorio = 0
        x = 1
        variable=1
        while variable<=numero:
            sumatorio=sumatorio+x
            x=x+2
            variable = variable+1
        print(f'El resultado es {sumatorio}.')
    ```

**EJERCICIO 7**. Escribir un programa que le pida al usuario un número y le diga si es un número primo o no.

??? note "Respuesta"
    ``` py linenums="1"
        numero = int(input("¿Qué número quieres saber si es primo?: \n "))
        valor = range(2, numero)
        contador = 0
        for n in valor:
            if numero % n == 0:
                contador += 1
                print("divisor:", n)
        if contador > 0:
            print("El numero no es primo")
        else:
            print("El numero es primo")
    ```


!!! cite "Enlaces de interés"

    * [**Información acerca de estructuras de control.**](https://docs.python.org/3/tutorial/controlflow.html)
    * [**Flow Control in Python.** Great Learning](https://www.youtube.com/watch?v=v4e6oMRS2QA&ab_channel=GreatLearning)
    * [**Programming in Python 3. Chapter 4.** Mark Summerfield (2010). Addison-Wesley.](https://cs.smu.ca/~porter/csc/227/ProgrammingInPython3.pdf)