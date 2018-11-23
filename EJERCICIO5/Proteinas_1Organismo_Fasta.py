import sys
import re
import gzip

def readUniProt(tax_id,input,output):
    with gzip.open(input, 'r') as f:  # abrimos fichero input, solo lectura
        repetidoOC = 0
        repetidoS = 0
        resultado = "" #declaramos resultado como string
        for line in f :# para line dentro de fichero
            line = line.decode()  # pasamos de line typo bit a tipo string
            if line[0:2] == 'OX': # si la line entre la posicion 0 y 2 es igual a OX
                repetidoOC = 0
                repetidoS = 0
                line = line.split('{') # separamos line cuando encuentre el caracter {
                id_tax = re.sub("\D","",line[0]) # id es igual a todos los numeros que esten en line antes del caracter {, es decir en  posicion 0 de line
                if id_tax == tax_id: # si el id_tax es igual al tax_id (introducido por el usuario)
                    cabecera = ">" + ac_number + ";" + id + ";" + id_tax + ";" + descripcion + "\r" # la cabecera es igual al accession number principal de la entrada, el identificador único de la entrada, el identificador taxonómico del organismo, y la descripción larga recomendada, empezando por el caracter '> ' y separando cada punto con ;
                    resultado += cabecera + secuencia# resultado es += a la cabecera mas la secuencia
            elif line[0:2] == 'AC': # si la line entre la posicion 0 y 2 es igual a AC
                line = line.replace("AC   ", "")  # line es igual a line camiando 'AC   ' por ''
                line = line.replace(";", "|")  # line es igual a line cambiando ';' por '|'
                line = line.replace(" ", "")  # line es igual a line cambiando ' ' por ''
                ac_number = line[:-2] # ac_number es igual a line menos las 2 ultimas posiciones
            elif line[0:2] == 'ID': # si la line entre la posicion 0 y 2 es igual a ID
                line = line.replace("ID   ", "")  # line es igual a line camiando 'ID   ' por ''
                line = line.split(' ')  # separamos line cuando encuentre el caracter ' '
                id = line[0] # id es igual a line de la posicion 0
            elif line[0:2] == 'OC': # si la line entre la posicion 0 y 2 es igual a OC
                line = line.replace("OC   ", "")  # line es igual a line camiando 'OC   ' por ''
                #line = line.replace(".", "")  # line es igual a line cambiando '.' por ''
                line = line.replace(";", "|")  # line es igual a line cambiando ';' por '|'
                line = line.strip()  # eliminacion saltos de lineas
                line = line.replace(" ", "")  # line es igual a line cambiando ' ' por ''
                if repetidoOC == 0: # si repetidoOC es igual a 0
                    descripcion = line # descripcion es igual a line
                    repetidoOC = 1 # repetidoOC sera igual a 1
                else: #sino
                    descripcion += line #descripcion es mas igual a line
            elif line[0:2] == '  ': # si la line entre la posicion 0 y 2 es igual a '  '
                line = line.replace("     ", "")  # line es igual a line camiando '     ' por ''
                line = line.replace(" ", "")  # line es igual a line cambiando ' ' por ''
                if repetidoS == 0: # si repetidoS es igual a 0
                    secuencia = line # secuencia es igual a line
                    repetidoS = 1 # repetidoS sera igual a 1
                else: #sino
                    secuencia += line #secuencia es mas igual a line

        with open(output, 'w') as w: # abrimos fichero output, solo escritura
            w.write(resultado) # escribimos en el fichero el contenido de resultado

if (len(sys.argv)>4 or len(sys.argv)<4):#si el  numero de parametros es mayor o menor a 4
    print('Numero de argumentos invalidos: python3 Proteinas_1Organismo_Fasta.py [id_taxonomico] [input.gz] [outout.fa]')
else:#sino
    readUniProt(sys.argv[1], sys.argv[2], sys.argv[3])
    print('Programa ejecutado con exito')
