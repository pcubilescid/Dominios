import sys
import gzip

def Ejercicio7(fasta,uniprot,tabular,output):
    id_tax={}
    id_proteina={}
    resultado = {}  # declaramos resultado como diccinario
    with open(fasta, 'r') as f:  # abrimos fichero input, solo lectura
        i=0
        resultado[0] = ["ID TAX", "ID PROTEINA", "ID DOMINIOS", "ID DOMINIOS UNIPROT", "ID DOMINIOS HMMER"]
        for line in f:  # para line dentro de fichero
            if line[0] == '>':  # si la line entre la posicion 0 y 2 es igual a OX
                line = line.split(';')  # separamos line cuando encuentre el caracter {
                id_tax[i]=line[2]
                id_proteina[i]=line[1]
                i+=1
        print(id_tax)
        print(id_proteina)


if (len(sys.argv)>5 or len(sys.argv)<5):#si el  numero de parametros es mayor o menor a 3
    print('Numero de argumentos invalidos: python3 _Ejercicio7.py [input.fa](fichero FASTA de secuencias de proteína) '
          '[input.gz](fichero comprimido de UniProt SW) [input.txt](fichero tabular) [output.txt](fichero donde grabar los resultados de las diferencias)')
else:#sino
    Ejercicio7(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
    print('Programa ejecutado con exito')