import subprocess
from tabulate import tabulate
import sys
def Ejercicio6(database,input,output,tabular):
    subprocess.check_output(["hmmscan", #orden hmm no me lee la primera linea
                     "--domtblout", # formato guarfado output
                     output, #Output
                     database, #Database
                     input #Input
                     ]
            )

    with open(output, 'r') as f:  # abrimos fichero output, solo lectura
        resultado = {} # declaramos resultado como diccinario
        cont=1 # declamaramos cont igual a 1
        for line in f :# para line dentro de fichero
            resultado[0]=["Accesion Number", "ID Dominio de Pfam", "Coordenada de inicio", "Coordenada de fin", "e-Value"] # resultado en la posicion 0 es igual
            if line[0] is not "#": # si la line en la posicion 0 es diferente a #
                line = line.split() # separamos line cuando encuentre un espacio
                ac = line[3] # ac es igual a line posicion 3
                ac = ac.split(";") # separamos ac cuando encuentre el caracter ;
                id_pfam = line[1]  # id_pfam es igual a line posicion 1
                inicio = line[19] # inicio es igual a line posicion 19
                final = line[20] # final es igual a line posicion 20
                evalue = line[6] # evalue es igual a line posicion 6
                resultado[cont] = [ac[0], id_pfam, inicio, final, evalue]  # resultado en la posicion i es igual a los siguientes datos
                cont+=1 # sumamos 1 al contador

    with open(tabular, 'w') as w:  # abrimos fichero tabular, solo escritura
        w.write(tabulate(resultado.values(),headers="firstrow"))  # escribimos en el fichero, en formato tabular, los valores de resultado y poniendo la primera fila como encabezado


if (len(sys.argv)>5 or len(sys.argv)<5):#si el  numero de parametros es mayor o menor a 5
    print('Numero de argumentos invalidos: python3 _Ejercicio6.py [database (Pfam)] [input.fa] [output.hmm] [output.txt]')
else:#sino
    Ejercicio6(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
    print('Programa ejecutado con exito')