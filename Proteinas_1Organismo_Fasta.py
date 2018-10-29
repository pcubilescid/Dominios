import sys
import re
import gzip
from tabulate import tabulate
def readUniProt(tax_id,input):
    with gzip.open(input, 'r') as f:  # abrimos fichero input, solo lectura
        count=0
        repetido = 0
        for line in f :# para line dentro de fichero
            line = line.decode()  # pasamos de line typo bit a tipo string
            if line[0:2] == 'OX': # si la line entre la posicion 0 y 2 es igual a OX
                repetido=0;
                line = line.split('{') # separamos line cuando encuentre el caracter {
                id_tax = re.sub("\D","",line[0]) # id es igual a todos los numeros que esten en line antes del caracter {, es decir en line de la posicion 0 de line
                if id_tax == tax_id:
                    count+=1
                    print (ac_number)
                    print (id)
                    print (descripcion)
            if line[0:2] == 'AC':
                ac_number=line
            if line[0:2] == 'ID':
                id=line
            if line[0:2] == 'OC':
                if repetido == 0:
                    descripcion=line
                    repetido=1
                else:
                    descripcion+=line

        print (count)

readUniProt(sys.argv[1],sys.argv[2])