## **Variables y constantes**
El concepto de **^^variable^^** hace referencia a un nombre simbólico o identificador que se asocia a un dato que se almacena en la memoria principal del ordenador, y se utiliza de forma habitual en programación para guardar distintos tipos de datos y operar con ellos posteriormente. 

* **Variables auxiliares**. También se llaman variables temporales. Son las que necesitamos para realizar algo de manera temporal, y seguramente esa variable no la necesites una vez ha cumplido su objetivo. 
* **Variables acumulativas**. Sirven para almacenar un número y sus valores consecutivos. Suelen utilizarse en bucles como *for* y *while*.

Una **^^constante^^** es un tipo de variable la cual no puede ser cambiada. Por tanto, es un valor que no debe ser alterado/modificado durante la ejecución de un programa, únicamente leído. Python no tiene tipos de constantes integrados, pero los programadores utilizan mayúsculas para indicar que una variable debería tratarse como una constante y no alterarse.

``` py
>>> NUM_AMINOACIDOS = 500 
```

### ***Nombrar y usar variables***
Cuando utilizamos variables en Python, tenemos que seguir una serie de normas y directrices. Algunas de estas directrices únicamente se emplean para que el código sea fácil de leer y entender, adquiriendo universalidad; mientras que romper algunas reglas provocará errores durante la ejecución del código.

* Los nombres de variable solo pueden contener **letras, números y guiones bajos**. No pueden empezar por un número, pero sí por una letra o guion. 
       
     _Ej_. Puede llamar a un variable *variable1* pero no *1variable*. 
    
* Los **guiones bajos** pueden servir para separar las palabras, ya que los espacios no están permitidos.

    _Ej_. Puede llamar a una variable *primera_variable* pero no *primera variable*.

* Los **nombres** de variable deben ser **cortos** pero descriptivos.

* No use **palabras** que Python tiene **reservadas** para un propósito concreto como *print, return o finally*.

!!! note "**Palabras reservadas**"

     Puede verificar si una palabra esta reservada utilizando el módulo integrado ***keyword***.
    ``` py
        >>> import keyword
        >>> keyword.iskeyword ("print")
        True
        >>> keyword.iskeyword ("fecha")
        False
    ```

### ***¿Cómo escribir una variable?***
Para asignar un valor a una variable se utiliza el operador de igualdad (=). A la izquierda de la igualdad se escribe el nombre de la variable y a la derecha el valor que se quiere dar a la variable.

``` py
>>> edad_paciente = 41
>>> obj_estudio = "proteína"
```

Para visualizar el valor de una variable, basta con escribir su nombre:

``` py
>>> edad_paciente = 41
>>> edad_paciente
41
>>>
```

Podemos asignar un solo valor a múltiples variables de la siguiente manera:
``` py
>>> x = y = z = 5
```

Además, podemos asignar múltiples valores a múltiples variables de la siguiente manera:

``` py
>>> a, b, c = 5, 'abcde', 9
```

!!! info "del"

    La instrucción ***del*** borra completamente una variable.
     ``` py
     >>> x = 5
     >>> x
     5
     >>> del x
     >>> x
     ERROR
     ```

### ***Tipos de variables***
La información que se guarda en una variable puede ser de muchos tipos:

* **Números** (enteros, decimales, imaginarios, en notación científica, en base decimal o en otras bases, etc.)
* **Cadenas de texto** (una sola letra o más letras, del juego de caracteres ASCII o Unicode, etc)
* **Conjuntos de números o texto** (matrices, listas, tuplas, etc.)
* **Estructuras más complicadas** (punteros, diccionarios, etc.)

Aunque se definan de forma similar, para Python no es lo mismo un número entero, un número decimal o una cadena ya que, por ejemplo, dos números se pueden multiplicar pero dos cadenas no (aunque una cadena sí que se puede multiplicar por un número). A continuación puede ver ejemplos de estas diferencias.

``` py
>>> fecha_actual = 2022
```
En este caso la variable *fecha_actual* está almacenando un número entero.

``` py
>>> fecha_actual = "2022"
```
En este caso la variable *fecha_actual* está almacenando una cadena formada por cuatro letras.

``` py
>>> fecha_actual = ["marzo", 2022]
```
En este caso la variable *fecha_actual* está almacenando una lista. Este tipo de elemento se verá más adelante.

#### *Datos numéricos*
Secuencia de dígitos que representan números, pudiendo incluir el - para negativos y el . para decimales. El tipo de datos de número se divide en los siguientes cinco tipos de datos en Python:

* **Entero.** No son más que números enteros, y pueden ser de diferentes tipos: positivo, negativo, cero y largo.
* **Entero largo.** El sufijo L se usa para la representación de enteros largos en Python, y estos se utilizan para almacenar números grandes sin perder precisión.
``` py 
>>> variable = 10000000L
```

* **Octales y hexadecimales.** Para representar el número octal que tiene base 8 en Python, agregue un 0 previamente para que el intérprete de Python pueda reconocer que el valor esté en base 8 y no en base 10. Para representar el número hexadecimal, agregue 0x. 
``` py 
>>> variable = 014
>>> variable
12  #Python devuelve por salida el valor en base decimal
```

* **Números de punto flotante.** Simbolizan los números reales que se escriben con un punto decimal que divide las partes entera y decimal. Los números de punto flotante también pueden venir con notación científica con E o e, indicando la potencia de 10.* 
``` py 
>>> variable = 7.9e2 #Esto es igual a 7.9 * 10**2
```

* **Números complejos.** Los números complejos tienen la forma 'a + bj', donde a es el valor flotante de la parte real y b es el valor flotante de la parte imaginaria, y j representa la raíz cuadrada de −1. 
``` py 
>>> variable = 5 + 3j
```

!!! info "Conversión entre tipos de números"

    Hay algunas funciones integradas de Python que nos permiten convertir números explícitamente de un tipo a otro. Un ejemplo es ***int ()***. 
     ``` py
     >>> valor = 1.5
     >>> valor = int (valor)
     >>> valor
     1
     ```
    En el siguiente enlace puede encontrar más información sobre las [funciones de conversión](https://en.wikibooks.org/wiki/Python_Programming/Numbers).

#### *Cadenas de caracteres*
Las cadenas de caracteres son secuencias que contienen caracteres encerrados entre comillas, simples o dobles. También podemos usar comillas triples, pero generalmente las comillas triples se usan para crear cadenas de documentos o cadenas de varias líneas.
``` py 
>>> cadena1 = 'bioquimica'
>>> cadena2 = "cromosoma"
```
En Python, se puede acceder individualmente a los caracteres de la cadena, desde ambas direcciones: hacia adelante y hacia atrás. Hacia adelante comienza desde 0, 1, 2... ; mientras que hacia atrás comienza desde −1, −2...
``` py 
>>> cadena1 = 'bioquimica'
>>> cadena1[1]
i
>>> cadena1[-2]
c
```

A continuación se muestran algunas de las funciones disponibles para trabajar con cadenas:

* *^^Función len()^^*. Función que devuelve la longitud de la cadena.
``` py 
>>> cadena = 'espermatozoide'
>>> len(cadena)
14
```
* *^^Mostrar parte de la cadena^^*. A continuación se muestra sintaxis para imprimir por pantalla parte de la cadena, ya sea el principio, final o una parte intermedia.
``` py 
>>> cadena = 'espermatozoide'
>>> cadena[2:6]
perma
>>> cadena[:6]
esperma
>>> cadena[6:]
atozoide
```

* *^^Cadena inversa^^*. No hay ninguna función integrada para invertir una cadena en Python, pero la forma más fácil es usar un segmento que comienza al final de la cadena y va hacia atrás.
``` py 
>>> cadena = 'espermatozoide' [::-1]
>>> cadena
ediozotamrepse
```

* *^^Concatenar cadenas^^*. El operador + se usa para agregar una cadena a otra cadena.
``` py 
>>> cadena_1 = 'La hemoglobina' 
>>> cadena_2 = 'es una proteina'
>>> cadena_final = cadena_1 + cadena_2
>>> cadena_final
La hemoglobina es una proteina
```

* *^^Reemplazar elementos^^*. El método *replace()* reemplazará un elemento específico con otro.
``` py 
>>> cadena_1 = 'AAATTGGCCAA' 
>>> cadena_final = cadena_1.replace("A", "T")
>>> cadena_final
TTTTTGGCCTT
```
!!! info "Otras funciones"

    En el siguiente enlace puede encontrar más funciones disponibles para trabajar con [cadenas](https://docs.python.org/2.5/lib/string-methods.html). Es importante que se familiarice con estas, ya que será importante a la hora de trabajar con secuencias de ADN, ya sea reemplazando, contando, o identificando nucléotidos por ejemplo.

#### *Booleanos*
Contiene únicamente dos elementos, True y False, que representan los valores lógicos verdadero y falso respectivamente. Por este motivo también se denominan **lógicos**. Todos los otros valores son interpretados por defecto a True.
``` py 
>>> False == False
False
>>> 0 == False
True
>>> None == False
False
```

### ***Alcance de las variables***
Las variables en Python son ^^locales^^ por defecto. Esto quiere decir que las variables definidas y utilizadas en el bloque de código de una función, solo tienen existencia dentro de la misma, y no interfieren con otras variables del resto del código.

En caso de que sea conveniente o necesario, una variable local puede convertirse en una variable global declarándola explícitamente como tal con la [**sentencia global**](https://docs.python.org/3/reference/simple_stmts.html#the-global-statement).

## **Operadores**
En Python, tenemos un conjunto de símbolos especiales que realizan varios tipos de operaciones, como operaciones lógicas, operaciones matemáticas y más. Estos símbolos se denominan **operadores**. Los valores sobre los que los operadores realizan sus respectivas operaciones se conocen como **operandos**.

### ***Aritméticos***
Los operadores aritméticos se utilizan para realizar varias operaciones matemáticas simples como sumas, restas y multiplicaciones.  

| OPERADOR      | NOMBRE             |      FUNCIÓN     | 
| :---------: | :----------------: |:---------: |
| `+`       | `Suma`             | Este operador suma los valores de los datos numéricos |
| `-`       | `Resta`              | Este operador resta los valores de los datos numéricos  |
| `*`    | `Multiplicación`             | Este operador multiplica los valores de los datos numéricos |
| `/`       | `División`              | Este operador divide los valores de los datos numéricos. El resultado es un número real  |
| `**`    | `Exponente`             | Este operador calcula el exponente entre los valores de los datos numéricos |
| `%`       | `Módulo`              | Este operador devuelve el resto de la división entre los dos operandos  |
| `//`  | `División entera`             | Este operador devuelve la parte entera del cociente de la división entre dos operandos  |

El orden de precedencia de ejecución de los operadores aritméticos es:

1. Exponente: **
2. Multiplicación, División, División entera, Módulo: *, /, //, % 
3. Suma, Resta: +, -

``` py title="EJEMPLOS"
>>> 5 * 6
30
>>> 8 / 3
2.66667
>>> 8 // 3
2
>>> 7 % 2
1
```

### ***Relacionales***
También se conocen como **operadores de comparación** porque comparan los valores en ambos lados del operador. Después de la comparación, devuelve el valor booleano, es decir, verdadero o falso. 

| OPERADOR      | NOMBRE             |      FUNCIÓN     | 
| :---------: | :----------------: |:---------: |
| `==`       | `Igual a`             | Si los dos operandos comparados son iguales, devuelve verdadero |
| `!=`       | `No igual a`              | Si los dos operandos comparados no son iguales, devuelve verdadero  |
| `<`    | `Menor que`             | Si el valor del operando izquierdo es menor que el del operando derecho, devuelve verdadero |
| `>`       | `Mayor que`              | Si el valor del operando izquierdo es mayor que el del operando derecho, devuelve verdadero  |
| `<=`    | `Menor o igual que`             | Si el valor del operando izquierdo es menor o igual que el del operando derecho, devuelve verdadero |
| `>=`       | `Mayor o igual que`              | Si el valor del operando izquierdo es mayor o igual que el del operando derecho, devuelve verdadero  |

``` py title="EJEMPLOS"
>>> 7 == 9
False
>>> 5*2 != 30/2
True
>>> "genoma" == "genoma"
True
>>> 5**2 <= 15
False
```

### ***De Asignación***
Los operadores de asignación se utilizan para asignar valores a las variables de Python . La asignación a veces se realiza directamente y, a veces, el operador primero realiza algún tipo de operación matemática y luego asigna el valor al operando.

| OPERADOR      | NOMBRE             |      FUNCIÓN     | 
| :---------: | :----------------: |:---------: |
| `=`       | `Asignación`             | Asigna a la variable del lado izquierdo cualquier variable o resultado del lado derecho |
| `+=`       | `Sumar y asignar`              | Realiza la suma y luego el resultado se asigna al operando de la izquierda  |
| `-=`    | `Restar y asignar`             | Realiza la resta y luego el resultado se asigna al operando de la izquierda |
| `*=`       | `Multiplicar y asignar`              | Realiza la multiplicación y luego el resultado se asigna al operando de la izquierda  |
| `/=`    | `Dividir y asignar`             | Realiza la división y luego el resultado se asigna al operando de la izquierda |
| `%=`       | `Módulo y asignar`              | Realiza el módulo y luego el resultado se asigna al operando de la izquierda  |
| `**=`       | `Exponente y asignar`              | Realiza exponente, y luego el resultado se asigna al operando de la izquierda  |
| `//=`       | `División entera y asignar`              | Realiza la división de piso y luego el resultado se asigna al operando de la izquierda  |

``` py title="EJEMPLOS"
>>> x = 5
>>> x += 10
>>> x
15
>>> y = 5
>>> y *= 20
>>> y
100
```

### ***Lógicos***
Los operadores lógicos se utilizan principalmente para declaraciones condicionales. Hay tres tipos de operadores lógicos: ***AND, OR y NOT.***

| OPERADOR      | NOMBRE             |      FUNCIÓN     | 
| :---------: | :----------------: |:---------: |
| `AND`       | `Logical AND`             | Devuelve TRUE cuando ambas expresiones son verdaderas, de lo contrario FALSE |
| `OR`       | `Logical OR`              | Devuelve TRUE si al menos una condición es verdadera, de lo contrario FALSE  |
| `NOT`    | `Logical NOT`             | Devuelve TRUE cuando la expresión no es verdadera |

``` py title="EJEMPLOS"
>>> (2<1) and (2<3)
False
>>> (2<1) or (2<3)
True
>>> not (5>4)
False
>>> not (5 != 5*1)
True
```

## **Ejercicios**
**EJERCICIO 1**. Escribir un programa que almacene la cadena _¡Hola Mundo!_ en una variable y luego muestre por pantalla el contenido de la variable.

??? note "Respuesta"
    ``` py linenums="1"
        mensaje = "¡Hola Mundo!"
        print(mensaje)
    ```

**EJERCICIO 2**. Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice de masa corporal y lo almacene en una variable.

??? note "Respuesta"
    ``` py linenums="1"
        peso = input("¿Cuál es tu peso en kg? ")
        estatura = input("¿Cuál es tu estatura en metros?")
        imc = round(float(peso)/float(estatura)**2,2)
        print("Tu índice de masa corporal es " + str(imc))
        # En este caso el índice de masa corporal se ha redondeado con dos decimales.
    ```

**EJERCICIO 3**. Escribir un programa que pida al usuario que introduzca una frase en la consola y muestre por pantalla la frase invertida.

??? note "Respuesta"
    ``` py linenums="1"
        frase = input("Introduce una frase: ")
        print(frase[::-1])
    ```

**EJERCICIO 4**. Escribir un programa que transforme grados Kelvin en grados Celcius.

??? note "Respuesta"
    ``` py linenums="1"
        grados_kelvin = input("Indique los grados en unidades Kelvin:")
        grados_celcius = (grados_kelvin - 273.15)
        print(f"El valor en unidades Celcius es {grados_celcius}")
    ```
**EJERCICIO 5**. Escribir un programa que pregunte por consola el precio de un producto en euros con dos decimales y muestre por pantalla el número de euros y el número de céntimos del precio introducido.

??? note "Respuesta"
    ``` py linenums="1"
        precio = input("Introduce el precio del producto con dos decimales:  ")
        print(precio[:precio.find('.')], 'euros y', precio[precio.find('.')+1:], 'céntimos.')
    ```

**EJERCICIO 6**. Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario lo introduzca, muestre por pantalla el número de letras que tiene el nombre en mayúsculas.

??? note "Respuesta"
    ``` py linenums="1"
         nombre = input("¿Cómo te llamas? ")
         print(nombre.upper() + " tiene " + str(len(nombre)) + " letras")
    ```

!!! cite "Enlaces de interés"

    * [**Información acerca de cadenas de caracteres.**](https://docs.python.org/es/3/library/string.html)
    * [**How to use Strings in Python**](https://www.youtube.com/watch?v=Ctqi5Y4X-jA&ab_channel=ProgrammingwithMosh)
    * [**Operadores**](https://support.microsoft.com/es-es/office/tabla-de-operadores-e1bc04d5-8b76-429f-a252-e9223117d6bd)
