# Defina dos posibles funciones para conocer el número de nucleótidos o aminoácidos almacenados como una lista.
# Se propone como lista el siguiente fragmento de ADN: ATGCGCGATCG

segmento_DNA = ['A','T','G','C','G','C','G','A','T','C','G']
def longitud_cadena (segmento_DNA):
    cont = 0
    for i in segmento_DNA:
        cont += 1
    return cont

#Otra opción:
longitud = len(segmento_DNA)
print(longitud)


# Determine cuántas veces aparece el nucleótido citosina (C) en un fragmento de ADN almacenado como cadena.
# Se propone de ejemplo el siguiente fragmento de ADN: ATGCGCGATCGTAGCT

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


#Determine el porcentaje de guanina/citosina (GC) en un fragmento de ADN almacenado como cadena.
# Se propone de ejemplo el siguiente fragmento de ADN: AGGCGCGTTGTGATGGTCGTAGCT

segmento_DNA="AGGCGCGTTGTGATGGTCGTAGCT"
total_nucleotidos = len(segmento_DNA)

numero_g = segmento_DNA.count("G")
numero_c = segmento_DNA.count("C")

contenido_gc = ((numero_g + numero_c)/total_nucleotidos)*100
print(f"El porcentaje GC del fragmento es: {contenido_gc}")


# Defina una función que convierta un fragmento de ADN a su ARN complementario.

def ADN_ARN(segmento_DNA):
    transcripcion = {"G":"C", "C":"G", "T":"A", "A":"U"}
    cadena_arn = ""
    for caracter in segmento_DNA:
        cadena_arn += transcripcion[caracter]
    return cadena_arn


# Determine si el último codón de un fragmento de ADN es un codón de inicio, stop u otro. El fragmento se ha almacenado como cadena en la respuesta, aunque puede solucionarlo como desee.
# Se propone de ejemplo el siguiente fragmento de ADN: ATGCGCGATCGTAGCT

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


# Defina una función que muestre la posición del primer nucleótido que constituye el codón de inicio en un fragmento de ADN.

def codon_inicio(segmento_DNA):
    for i in range(len(segmento_DNA)):
        triplete = segmento_DNA[i:i+3]
        if triplete == 'ATG':
            return(i+1) # Ya que la posición 1 es 0
    else:
        return ("No hay codón de inicio.")


# Imprima por pantalla todos los codones que comiencen por timina (T).

bases = ['A', 'T', 'C', 'G']

print('Codones que empiezan por T:')
for segunda_base in bases:
    print('Codones que empiezan por T' + segunda_base)
    for tercera_base in bases:
        print('T' + segunda_base + tercera_base)


# Determine el porcentaje de aminoácidos de un fragmento proteico almacenado como cadena.
# Se propone de ejemplo el siguiente fragmento: PCCWWLAKVRMIKGEFYVIEYAACD

secuencia_proteica ="PCCWWLAKVRMIKGEFYVIEYAACD"
aminoacidos = set(secuencia_proteica)
secuencia_length = len(secuencia_proteica)

for aminoacido in aminoacidos:
    aminoacido_count = secuencia_proteica.count(aminoacido)
    aminoacido_porcentaje = (aminoacido_count/secuencia_length) * 100
    print(aminoacido,":",round(aminoacido_porcentaje,1))




