import sys
import re
import gzip
from tabulate import tabulate
def readUniProt(tax_id,input,output):
    with gzip.open(input, 'r') as f:  # abrimos fichero input, solo lectura
        count=0
        repetidoOC = 0
        repetidoS = 0
        i = 0
        resultado = ""
        for line in f :# para line dentro de fichero
            line = line.decode()  # pasamos de line typo bit a tipo string
            if line[0:2] == 'OX': # si la line entre la posicion 0 y 2 es igual a OX
                repetidoOC = 0
                repetidoS = 0
                line = line.split('{') # separamos line cuando encuentre el caracter {
                id_tax = re.sub("\D","",line[0]) # id es igual a todos los numeros que esten en line antes del caracter {, es decir en line de la posicion 0 de line
                if id_tax == tax_id:
                    count+=1
                    cabecera = "\n> " + ac_number + "; " + id + "; " + id_tax + "; " + descripcion + "\n\n"
                    print (cabecera)
                    print (secuencia)
                    resultado += cabecera + secuencia
            if line[0:2] == 'AC':
                line = line.replace("AC   ", "")  # line es igual a line camiando 'AC   ' ''
                line = line.replace(";", "-")  # line es igual a line cambiando ';' '-'
                line = line.replace(" ", "")  # line es igual a line cambiando ' ' ''
                ac_number=line[:-3]
            if line[0:2] == 'ID':
                line = line.replace("ID   ", "")  # line es igual a line camiando 'ID   ' ''
                line = line.split(' ')  # separamos line cuando encuentre el caracter ' '
                id=line[0]
            if line[0:2] == 'OC':
                line = line.replace("OC   ", "")  # line es igual a line camiando 'OC   ' ''
                #line = line.replace(".", "")  # line es igual a line cambiando '.' ''
                line = line.replace(";", "-")  # line es igual a line cambiando ';' '-'
                line = line.replace("\n", "")  # line es igual a line cambiando '\n' ''
                line = line.replace(" ", "")  # line es igual a line cambiando ' ' ''
                if repetidoOC == 0:
                    descripcion = line
                    repetidoOC = 1
                else:
                    descripcion+=line
            if line[0:2] == '  ':
                line = line.replace("     ", "")  # line es igual a line camiando 'OC   ' ''
                line = line.replace(" ", "")  # line es igual a line cambiando ' ' ''
                if repetidoS == 0:
                    secuencia = line
                    repetidoS = 1
                else:
                    secuencia+=line

        print (count)

        with open(output, 'w') as w: # abrimos fichero output, solo escritura
            w.write(resultado)


readUniProt(sys.argv[1],sys.argv[2],sys.argv[3])