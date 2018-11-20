import subprocess
from tabulate import tabulate
import sys
def Ejercicio6(database,input,output,tabular):
    subprocess.check_output(["hmmscan",
                     "--pfamtblout",
                     output, #Output
                     database,
                     input #Input
                     ]
            )


    with open(input, 'r') as f:  # abrimos fichero input, solo lectura
        resultado = {} # declaramos resultado como diccinario
        id_pfam=""
        for line in f :# para line dentro de fichero
            resultado[0]=["Accesion Number", "ID Dominio de Pfam", "Coordenada de inicio", "Coordenada de fin", "e-Value"]
            if line[0] == '>': # si la line en la posicion 0 igual a >
                line = line.split(';')  # separamos line cuando encuentre el caracter ;
                ac = line[0][1:] # ac es igual a la posicion 0 de la linea desde el caracter en la posicion 2 hasta el final

            #with open(output, 'r') as r:
             #   for line in r:
              #      if line[0] is not "#" and line[0] is not "\n":
               #         line = line.strip()  # eliminacion saltos de linea
                #        line = line.split()
                 #       id_pfam = line[0]
                  #      print (id_pfam)
                resultado[ac] = [ac, "-", "-", "-", "-"]  # rsulytado en la posicion ac es igual a ac

    with open(tabular, 'w') as w:  # abrimos fichero output, solo escritura
        w.write(tabulate(resultado.values(),headers="firstrow"))  # escribimos en el fichero, en formato tabular, los valores de resultado y poniendo la primera fila como encabezado


if (len(sys.argv)>5 or len(sys.argv)<5):#si el  numero de parametros es mayor o menor a 3
    print('Numero de argumentos invalidos: python3 _Ejercicio6.py [database (Pfam)] [input.fa] [output.hmm] [output.txt]')
else:#sino
    Ejercicio6(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
    print('Programa ejecutado con exito')