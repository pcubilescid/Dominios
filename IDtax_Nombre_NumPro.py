import sys
import re
import gzip
def readUniProt(input):
    with gzip.open(input, 'r') as f: #abrimos fichero fasta, solo lectura
        for line in f:
            line = line.decode()  # pasamos de line typo bit a tipo string
            if line[0:2] == 'OX':
                ID = re.sub("\D","",line)
                print(ID)
            if line[0:2] == 'OS':
                line = line.replace("OS ","")
                nombre = line[2:-2]

                print(nombre)

readUniProt(sys.argv[1])