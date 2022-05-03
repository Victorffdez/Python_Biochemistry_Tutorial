## **¿Qué es Biopython?**
[Biopython](https://biopython.org/) es el paquete de Python más utilizado en el ámbito de la biología computacional, con una gran cantidad de herramientas útiles en bioinformática. 

Esta librería fue creada en el año 1999 por _Brad Chapman_ y _Jeff Chang_, y actualmente está soportada por el _Proyecto Biopython_, una asociación de desarrolladores de herramientas en el lenguaje informático Python.

<figure markdown>
  ![matplot](logo_biopython.png){ width="350" height="350" }
</figure>

### ***Ventajas***

* ^^Compatibilidad con diferentes formatos.^^ Biopython permite el tratamiento de archivos en diversos formatos utilizados en el ámbito biológico, presentando total compatibilidad con los archivos procedentes de GenBank, PDB, PubMed, ExPASy...
* ^^Tratamiento de secuencias.^^ Permite trabajar con secuencias tanto nucleotídicas como aminoacídicas.
* ^^Herramientas incorporadas.^^ Herramientas para realizar operaciones comunes en secuencias, como traducción, transcripción, longitud de cadenas...
* ^^Herramientas para realizar alineamientos de secuencias.^^
* ^^Amplio uso.^^ Al ser el paquete más utilizado en biología computacional junto a [Bioconductor](https://www.bioconductor.org/), encontrará una gran cantidad de foros actualizados que le serán de ayuda. Además se incluyen herramientas nuevas que le pueden ser de utilidad, así como actualizaciones de las herramientas anteriores.

Como bioquímico interesado en la bioinformática, es fundamental que se familiarice con Biopython, ya que es una herramienta fundamental actualmente en el lenguaje Python para el tratamiento de datos biológicos.

### ***Instalación***
En primer lugar debe instalar el paquete _biopython_. Para ello, como se explicó en el apartado [PyCharm](3_Pycharm.md), vaya a la ventana de _Python Packages_ e instálelo.

<figure markdown>

  ![matplot](biopython_instalacion.png){ width="800" height="500" }
    <figcaption> Instalación del paquete *biopython* </figcaption>
</figure>

Otra opción sería utilizar el siguiente comando en la consola:
```
pip install biopython
```

## **Trabajo con secuencias**
Sin duda los elementos u objetos centrales en el tratamiento de datos biológicos son las **secuencias**. 

En este apartado aprenderá algunos conceptos básicos sobre el maneja del **objeto _Seq_**, objeto más utilizado en el paquete Biopython, que contiene muchas funciones en común con las cadenas. 

### ***Ejemplos ***
``` py linenums="1"
from Bio.Seq import Seq
seq = Seq("AGAGCCGACTTTACT")

num_nucleotidos= len(seq) #Almacena el número de nucleótidos

primer_nucleotido= seq[0] #Almacena el primer nucleótido

num_guaninas = seq.count("G") #Almacena el número de guaninas

cortar_secuencia= seq[0:6] #Almacena la secuencia desde el primer nucleótido hasta el séptimo

cadena_complementaria= seq[::-1] #Almacena la cadena complementaria

#Porcentaje de G+C
porcentaje_GC = 100 * float(seq.count("G") + seq.count("C")) / len(seq)

#Biopython ya contiene un módulo integrado que simplifica esta tarea
from Bio.SeqUtils import GC
calculo_porcentaje_GC= GC(seq)
```

### ***Transcripción y traducción***
En primer lugar veamos cómo realizar una **transcripción** en Biopython. Para esto crearemos objetos _Seq_ para la hebra de ADN codificante y la hebra molde/template:
``` py linenums="1"
from Bio.Seq import Seq
seq_codificante = Seq("AATGCGGCTTAACCACAC")
print(seq_codificante)
seq_molde = seq_codificante.reverse_complement()
print(seq_molde)
```
Debe tener en cuenta que la secuencia molde es leída por la polimerasa en dirección 3'-5', por lo que la secuencia codificante aparece en dirección 5'-3'. Por tanto se muestra por pantalla la siguiente salida:
``` py 
AATGCGGCTTAACCACAC
GTGTGGTTAAGCCGCATT
```
Una vez hemos creado la hebra molde y la codificante, vamos a llevar a cabo la transcripción. Recuerde que la transcripción se puede ver como la sustitución de A->U en la hebra codificante.
``` py linenums="1"
from Bio.Seq import Seq
seq_codificante = Seq("AATGCGGCTTAACCACAC")
seq_molde = seq_codificante.reverse_complement()
ARN_mensajero = seq_codificante.transcribe()
print(ARN_mensajero)
```
Si únicamente posee la hebra molde, y desea realizar la transcripción sin necesidad de crear la hebra codificante, puede utilizar la acción combinada de ambas funciones anteriores:
``` py linenums="1"
from Bio.Seq import Seq
seq_molde = Seq("GTGTGGTTAAGCCGCATT")
ARN_mensajero = seq_molde.reverse_complement().transcribe()
```
Por último, si lo que desea es realizar una transcripción inversa, es decir, pasar del ARN mensajero a la hebra codificante:
``` py linenums="1"
from Bio.Seq import Seq
ARN_mensajero = Seq("AAUGCGGCUUAACCACAC")
seq_codificante = ARN_mensajero.back_transcribe()
```
Una vez finalizada la transcripción, veamos cómo llevar a cabo la **traducción** partiendo de la secuencia nucleotídica del ARN mensajero obtenida.
``` py linenums="1"
from Bio.Seq import Seq
seq_codificante = Seq("AATGCGGCTTTACCACAC")
seq_molde = seq_codificante.reverse_complement()
ARN_mensajero = seq_codificante.transcribe()

proteina= ARN_mensajero.translate()
print(proteina)
```
Esto debería mostrar por pantalla la siguiente secuencia aminoacídica:
``` py 
NAALPH
```
También podría realizar la traducción desde la hebra codificante de ADN. En este caso se ha introducido una mutación en la secuencia: T 11 -> A 11.  
``` py linenums="1"
from Bio.Seq import Seq
seq_codificante = Seq("AATGCGGCTTAACCACAC")
seq_molde = seq_codificante.reverse_complement()

proteina= seq_codificante.translate()
print(proteina)
```
En este caso, el resultado será el siguiente:
``` py 
NAA*PH
# El asterisco indica que es un codón stop.
```
Aunque a priori parece un método muy básico, hay algunos **aspectos adicionales** en la traducción que hay que tener en cuenta.

La tabla de traducción que utiliza Biopython se basa en la tablas indicadas en el [NCBI](https://www.ncbi.nlm.nih.gov/Taxonomy/Utils/wprintgc.cgi), utilizando de forma predeterminada el código genético estándar (_Tabla 1_). En algunos casos necesitará utilizar tablas de traducción diferente, por ejemplo si está tratando con un genoma mitocondrial. Esto se puede indicar de diversas formas:
``` py linenums="1"
from Bio.Seq import Seq
seq_codificante = Seq("AATGCGGCTTAACCACAC")
seq_molde = seq_codificante.reverse_complement()

proteina= seq_codificante.translate(table="Vertebrate Mitochondrial") #1ª Forma
proteina= seq_codificante.translate(table=2) # 2ª Forma
```
Como ha visto en uno de los ejemplos anteriores, Biopython va a detectar un codón de parada indicándolo con un asterisco. Lo normal es que desee llevar a cabo la traducción hasta este codón y detenerse:
``` py linenums="1"
from Bio.Seq import Seq
seq_codificante = Seq("AATGCGGCTTAACCACAC")
seq_molde = seq_codificante.reverse_complement()

proteina= seq_codificante.translate(to_stop=True)
print(proteina)
```

## **Trabajo con archivos**

## **Alineamientos**

## **Blast**

## **¿Entrez, ExPASy, PDB, Cap 20 archivos secuencias?**
