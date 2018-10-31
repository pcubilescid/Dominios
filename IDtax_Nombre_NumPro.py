import sys
import re
import gzip
from tabulate import tabulate
def readUniProt(input,output):
    with gzip.open(input, 'r') as f:  # abrimos fichero input, solo lectura
        resultado = {} # declaramos resultado como diccinario
        pro = 1
        repite = 0

        for line in f :# para line dentro de fichero
            line = line.decode()  # pasamos de line typo bit a tipo string
            resultado[0]=["TaxID","Scientific Name (Common Name)","Num_Proteins"]
            if line[0:2] == 'OX': # si la line entre la posicion 0 y 2 es igual a OX
                repite = 0 # repite igual a 0
                line = line.split('{') # separamos line cuando encuentre el caracter {
                id = re.sub("\D","",line[0]) # id es igual a todos los numeros que esten en line antes del caracter {, es decir en la posicion 0 de line
                if id in resultado: # si id esta dentro de resultado
                    resultado[id][2] += pro # resultado en la posicion id, en la posicion 2 se suma pro(1)
                else: # sino
                    resultado[id] = [id,nombre,pro] #resultado en la posicion id sera igual a posicion 0 id, posicion 1 nombre, posicion 2 pro

            elif line[0:2] == 'OS': # si line entre la posicion 0 y 2 es igual a OS
                line = line.replace("OS   ", "") # line es igual a line camiando 'OS   ' a ''
                line = line.replace(".", "") # line es igual a line cambiando '.' ''
                if repite == 1: # si repite es igual a 1
                    nombre += line[:-1] # nombre es igual al contenido que ya tenia nombre, mas line quitandole la ultima posicion (\n)
                else: # sino
                    nombre = line[:-1] # nombre es igual a line menos la ultima posicion (\n), sobreescribe lo que tenia antes nombre
                    repite = 1 # repite es igual a 1

    with open(output, 'w') as w: # abrimos fichero output, solo escritura
        w.write(tabulate(resultado.values(),headers="firstrow"))# escribimos en el fichero, en formato tabular, los valores de resultado y poniendo la primera fila como encabezado

if (len(sys.argv)>3 or len(sys.argv)<3):#si el  numero de parametros es mayor o menor a 3
    print('Numero de argumentos invalidos: python3 IDtax_Nombre_NumPro.py [input.gz] [outout.txt]')
else:#sino
    readUniProt(sys.argv[1], sys.argv[2])
    print('Programa ejecutado con exito')
