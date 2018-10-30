import sys
import re
import gzip
from tabulate import tabulate
def readUniProt(tax_id,input):
    with gzip.open(input, 'r') as f:  # abrimos fichero input, solo lectura
        count=0
        repetidoOC = 0
        repetidoS = 0
        for line in f :# para line dentro de fichero
            line = line.decode()  # pasamos de line typo bit a tipo string
            if line[0:2] == 'OX': # si la line entre la posicion 0 y 2 es igual a OX
                repetidoOC = 0
                repetidoS = 0
                line = line.split('{') # separamos line cuando encuentre el caracter {
                id_tax = re.sub("\D","",line[0]) # id es igual a todos los numeros que esten en line antes del caracter {, es decir en line de la posicion 0 de line
                if id_tax == tax_id:
                    count+=1
                    cabecera = "> " + ac_number + "; " + id + "; " + id_tax + "; " + descripcion
                    print (cabecera)
                    print (secuencia + "\n")
            if line[0:2] == 'AC':
                line = line.replace("AC   ", "")  # line es igual a line camiando 'AC   ' ''
                #line = line.replace(";", ",")  # line es igual a line cambiando ';' ','
                ac_number=line[:-2]
            if line[0:2] == 'ID':
                line = line.replace("ID   ", "")  # line es igual a line camiando 'ID   ' ''
                line = line.split(' ')  # separamos line cuando encuentre el caracter ' '
                id=line[0]
            if line[0:2] == 'OC':
                line = line.replace("OC   ", "")  # line es igual a line camiando 'OC   ' ''
               # line = line.replace(".", "")  # line es igual a line cambiando '.' ''
               # line = line.replace(";", ",")  # line es igual a line cambiando ';' ','
                if repetidoOC == 0:
                    descripcion = line[:-1]
                    repetidoOC = 1
                else:
                    descripcion+=line[:-1]
            if line[0:2] == '  ':
                line = line.replace("     ", "")  # line es igual a line camiando 'OC   ' ''
                line = line.replace(" ", "")  # line es igual a line cambiando ' ' ''
                if repetidoS == 0:
                    secuencia = line[:-1]
                    repetidoS = 1
                else:
                    secuencia+=line[:-1]

        print (count)

readUniProt(sys.argv[1],sys.argv[2])