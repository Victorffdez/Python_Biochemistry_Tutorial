A continuación encontrará una serie de ejercicios relacionados con la manipulación de **fragmentos nucleotídicos o proteicos** para que siga practicando en Python:

###**Ejercicio 1** 
Defina dos posibles funciones para conocer el número de nucleótidos o aminoácidos almacenados como una lista.
??? success "Respuesta"
    ``` py linenums="1"
    def longitud_cadena (lista):
        cont = 0
        for i in lista:
            cont += 1
        return cont

    #Otra opción: utilizar la función len() ya definida.
    ```
###**Ejercicio 2** 
Determine cuántas veces aparece el nucleótido citosina (C) en un fragmento de ADN.

*Se propone de ejemplo el siguiente fragmento de ADN: ATGCGCGATCGTAGCT*  
??? success "Respuesta"
    ``` py linenums="1"
    segmento_DNA = 'ATGCGCGATCGTAGCT'
    bp = 'C'
        
    print('Nº de citosinas:', segmento_DNA.count(bp)) #La opción más simple
        
    contador = 0 #Otra opción
    numero = 0
    while numero < len(segmento_DNA):
        if bp == segmento_DNA[numero]:
            contador += 1
        numero += 1
        
    print('Nº de citosinas (bucle while):', contador)
    ```
###**Ejercicio 3** 
Determine el porcentaje de guanina/citosina (GC) en un fragmento de ADN.

*Se propone de ejemplo el siguiente fragmento de ADN: AGGCGCGTTGTGATGGTCGTAGCT*

??? success "Respuesta"
    ``` py linenums="1"
    segmento_DNA="AGGCGCGTTGTGATGGTCGTAGCT"
    total_nucleotidos = len(segmento_DNA)
            
    numero_g = segmento_DNA.count("G")
    numero_c = segmento_DNA.count("C")
                    
    contenido_gc = ((numero_g + numero_c)/total_nucleotidos)*100
    print(f"El porcentaje GC del fragmento es: {contenido_gc}")
    ```

###**Ejercicio 4** 
Defina una función que convierta un fragmento de ADN a su ARN complementario.
??? success "Respuesta"
    ``` py linenums="1"
    def ADN_ARN(segmento_DNA):
        transcripcion = {"G":"C", "C":"G", "T":"A", "A":"U"}
        cadena_arn = ""
        for caracter in segmento_DNA:
            cadena_arn += transcripcion[caracter]
        return cadena_arn 
    ```
###**Ejercicio 5** 
Determine si el último codón de un fragmento de ADN es un codón de inicio, stop u otro.

*Se propone de ejemplo el siguiente fragmento de ADN: ATGCGCGATCGTAGCT*  

??? success "Respuesta"
    ``` py linenums="1"
    segmento_DNA = 'ATGCGCGATCGTAGCT'
    codon1 = segmento_DNA[-3:]
        
    if (codon1 == 'ATG'):
        print(' El codon', codon1, 'es un codon de inicio.')
    elif ((codon1 == 'TAA') or
           (codon1 == 'TAG') or
           (codon1 == 'TGA')):
        print('El codon', codon1, 'es un codon stop.')
    else:
        print('El codon', codon1, 'es un codon diferente.')
    ```
###**Ejercicio 6** 
Defina una función que muestre la posición del codón de inicio en un fragmento de ADN.
??? success "Respuesta"
    ``` py linenums="1"
    def codon_inicio(segmento_DNA):
        for i in range(len(segmento_DNA)):
            triplete = segmento_DNA[i:i+3]
            if triplete == 'ATG':
                return(i+1) # Ya que la posición 1 es 0
    ```

###**Ejercicio 7** 
Imprima por pantalla todos los codones que comiencen por timina (T) en un fragmento de ADN.

*Se propone de ejemplo el siguiente fragmento de ADN: ATGCGCGATGTGATCGTCGTAGCT*  
??? success "Respuesta"
    ``` py linenums="1"
    segmento_DNA = 'ATGCGCGATGTGATCGTCGTAGCT'
    bases = ['A', 'T', 'C', 'G']
        
    print('Codones que empiezan por T:')
    for segunda_base in bases:
        print('Codones que empiezan por T' + segunda_base)
        for tercera_base in bases:
            print('T' + segunda_base + tercera_base)
    ```

###**Ejercicio 8** 
Determine el porcentaje de aminoácidos de un fragmento proteico.

*Se propone de ejemplo el siguiente fragmento: PCCWWLAKVRMIKGEFYVIEYAACD*
??? success "Respuesta"
    ``` py linenums="1"
    secuencia_proteica ="PCCWWLAKVRMIKGEFYVIEYAACD"
    aminoacidos = set(secuencia_proteica)
    secuencia_length = len(secuencia_proteica)
        
    for aminoacido in aminoacidos:
        aminoacido_count = secuencia_proteica.count(aminoacido)
        aminoacido_porcentaje = (aminoacido_count/secuencia_length) * 100
        print(aminoacido,":",round(aminoacido_porcentaje,1))
    ```