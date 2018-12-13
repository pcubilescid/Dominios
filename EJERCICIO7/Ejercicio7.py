import sys
from tabulate import tabulate
import gzip

def Ejercicio7(fasta,uniprot,tabular,output):
    resultado = {} # declaramos resultado como diccinario
    id_proteina = {}
    id_tax = {}
    id_hmm = {}
    id_uni = {}
    pfam = {}
    ac = {}
    ac2 = {}
    ac_number = {}

    resultado[0] = ["ID TAX", "ID PROTEINA", "ID DOMINIOS", "ID DOMINIOS UNIPROT", "ID DOMINIOS HMMER"]

    with gzip.open(uniprot, 'r') as u:  # abrimos fichero input, solo lectura
        i = 1
        j = 1
        repite = 0
        for line3 in u:  # para line dentro de fichero
            line3 = line3.decode()  # pasamos de line typo bit a tipo string
            if line3[0:2] == 'AC':  # si la line entre la posicion 0 y 2 es igual a AC
                line3 = line3.replace("AC   ", "")  # line es igual a line camiando 'AC   ' por ''
                line3 = line3.replace(";", "|")  # line es igual a line cambiando ';' por '|'
                line3 = line3.replace(" ", "")  # line es igual a line cambiando ' ' por ''
                ac_number[j] = line3[0:-2]  # ac_number es igual a line menos las 2 ultimas posiciones
                j += 1
                i += 1
                repite = 0

            if line3[:10] == 'DR   Pfam;': # si line3 desde el inicio hasta la posicion 10 es igual a 'DR   Pfam;'
                line3 = line3.replace(" ", "")  # line es igual a line cambiando ' ' por ''
                line3 = line3.split(';')  # separamos line cuando encuentre el caracter ;
                if repite == 0:
                    pfam[i] = line3[1]  # id_hmm[i] es igual a line2 en la posicion uno
                    repite = 1
                else:
                    pfam[i] += "," + line3[1]

    with open(fasta, 'r') as f:  # abrimos fichero input, solo lectura
        i = 1
        j = 1

        for line in f:  # para line dentro de fichero
            if line[0] == '>':  # si la line entre la posicion 0 y 2 es igual a OX
                line = line.split(';')  # separamos line cuando encuentre el caracter ;
                ac[j] = line[0][1:] # ac[i] es igual a line de la posicion 0 desde el caracter 1 hasta el final
                while ac_number[i] != ac[j]: # si ac2[j] es igual a ac[i] (ac son accesion number)
                    i += 1
                if ac_number[i] == ac[j]: # si ac_number en la posicion i es igual a ac en la posicion j
                    try:
                        print(pfam[i])
                        id_uni[j] = pfam[i]
                    except KeyError:
                        pfam[i] = "-"
                        id_uni[j] = pfam[i]
                    j += 1

    with open(fasta, 'r') as f:  # abrimos fichero input, solo lectura
        i = 1
        for line in f:  # para line dentro de fichero
            if line[0] == '>':  # si la line entre la posicion 0 y 2 es igual a OX
                line = line.split(';')  # separamos line cuando encuentre el caracter ;
                id_tax[i]=line[2] # id_tax[i] es igual a line en la posicion 2
                id_proteina[i]=line[1] # id_proteina[i] es igual a line en la posicion 1
                ac[i] = line[0][1:] # ac[i] es igual a line de la posicion 0 desde el caracter 1 hasta el final
                i += 1

    with open(tabular, 'r') as t: # abrimos fichero tabular solo lectura
        repite = 0
        i = 1
        j = 1
        for line2 in t: # para line2 dentro de fichero t
            line2 = line2.split()  # separamos line cuando encuentre un espacio
            dom = line2[1].split(".")
            if line2[1][0] == "P": # si line2 en la posicion 1 el caracter 0 es igual a P
                ac2[j] = line2[0] # ac2[j] es igual a line2 posicion 0
                if ac2[j] == ac[i]: # si ac2[j] es igual a ac[i] (ac son accesion number)
                    if dom[0] not in id_hmm[i]:
                        if repite == 1: # si repite es igual  a 1
                            id_hmm[i] += "," + dom[0] # id_hmm[i] es mas igual a espacio mas line2 en la posicion 1 (concatetar los dominios)
                        else:
                            id_hmm[i] = dom[0] # id_hmm[i] es igual a line2 en la posicion uno
                            repite = 1
                        j += 1 # añadimos 1 al contador j
                else:
                    repite=0
                    i += 1 # añadimos 1 al contador i
                    if ac2[j] == ac[i]: # si ac2[j] es igual a ac[i] (ac son accesion number)
                        id_hmm[i] = dom[0] # id_hmm[i] es igual a line2 en la posicion uno
                        repite = 1
                        j += 1 # añadimos 1 al contador j

    i = 1
    for x in id_proteina: # para x dentro de id_proteina
        try:
            resultado[i] = [id_tax[i], id_proteina[i], "-", id_uni[i], id_hmm[i]]

        except KeyError:
            id_hmm[i] = "-"
            resultado[i] = [id_tax[i], id_proteina[i], "-", id_uni[i], id_hmm[i]]
        i += 1


    with open(output, 'w') as w:  # abrimos fichero output, solo escritura
        w.write(tabulate(resultado.values(),headers="firstrow"))  # escribimos en el fichero, en formato tabular, los valores de resultado y poniendo la primera fila como encabezado


if (len(sys.argv)>5 or len(sys.argv)<5):#si el  numero de parametros es mayor o menor a 3
    print('Numero de argumentos invalidos: python3 _Ejercicio7.py [input.fa](fichero FASTA de secuencias de proteína) '
          '[input.gz](fichero comprimido de UniProt SW) [input.txt](fichero tabular) [output.txt](fichero donde grabar los resultados de las diferencias)')
else:#sino
    Ejercicio7(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
    print('Programa ejecutado con exito')