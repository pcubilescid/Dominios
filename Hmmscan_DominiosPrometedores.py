import sys
from tabulate import tabulate
def readUniProt(input,output):
    with open(input, 'r') as f:  # abrimos fichero input, solo lectura
        resultado = {} # declaramos resultado como diccinario

        for line in f :# para line dentro de fichero
            resultado[0]=["Accesion Number"]
            if line[0] == '>': # si la line en la posicion 0 igual a >
                line = line.split(';')  # separamos line cuando encuentre el caracter ;
                ac = line[0][1:] # ac es igual a la posicion 0 de la linea desde el caracter en la posicion 2 hasta el final
                print (ac)
                if ac in resultado: # si ac esta dentro de resultado
                    print("Mal")
                else: # sino
                    resultado[ac] = [ac] #rsulytado en la posicion ac es igual a ac

    with open(output, 'w') as w:  # abrimos fichero output, solo escritura
        w.write(tabulate(resultado.values(),headers="firstrow"))  # escribimos en el fichero, en formato tabular, los valores de resultado y poniendo la primera fila como encabezado


#if (len(sys.argv)>3 or len(sys.argv)<3):#si el  numero de parametros es mayor o menor a 3
 #   print('Numero de argumentos invalidos: python3 Hmmscan_DOminiosPrometedores ')
#else:#sino
readUniProt(sys.argv[1], sys.argv[2])
print('Programa ejecutado con exito')
