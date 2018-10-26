import sys
import re
import gzip
from tabulate import tabulate
def readUniProt(input,output):
    with gzip.open(input, 'r') as f: #abrimos fichero fasta, solo lectura
        i = 0
        resultado = {}
        nombre = ''
        pro = 1
        repite = 0

        for line in f:
            line = line.decode()  # pasamos de line typo bit a tipo string
            resultado[0]=["TaxID","Scientific Name (Common Name)","Num_Proteins"]
            if line[0:2] == 'OX':
                repite = 0
                line = line.split('{')
                id = re.sub("\D","",line[0])
                if id in resultado:
                    resultado[id][2] += pro
                else:
                    resultado[id] = [id,nombre,pro]

            if line[0:2] == 'OS':
                line = line.replace("OS   ", "")
                line = line.replace(".", "")
                if repite == 1:
                    nombre += line[:-1]
                else:
                    nombre = line[:-1]
                    repite = 1

        print(tabulate(resultado.values()))

    with open(output, 'w') as w:
        w.write(tabulate(resultado.values(),headers="firstrow"))

readUniProt(sys.argv[1],sys.argv[2])