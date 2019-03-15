#!/usr/bin/env nextflow

myFile4 = file("$baseDir/EJERCICIO4/IDtax_Nombre_NumPro.py")
myUni = file("$baseDir/DB/uniprot_sprot_mammals.dat.gz")
myRes4 = file("$baseDir/resultados/cuatro.txt")

process cuatro {

	input: 
	file myFile4
	file myUni

	//output:
	//file myRes4 into Exit_4

	"""
	python3 $myFile4 $myUni $myRes4
	"""
}

myFile5 = file("$baseDir/EJERCICIO5/Proteinas_1Organismo_Fasta.py")
myRes5 = file("$baseDir/resultados/cinco.fa")

process cinco {

	input: 
	file myFile5
	file myUni

	//output:
	//file myRes5 into Exit_5

	"""
	python3 $myFile5 39432 $myUni $myRes5
	"""
}

myFile6 = file("$baseDir/EJERCICIO6/Ejercicio6.py")
myPfam = file("$baseDir/DB/minifam")
myRes6H = file("$baseDir/resultados/seis.hmm")
myRes6T = file("$baseDir/resultados/seis.txt")

process seis {

	input: 
	//val proteinas from Exit_5
	file myRes5
	file myFile6
	file myPfam

	//output:
	//file myRes6H into Exit_6H
	//file myRes6T into Exit_6T

	"""
	hmmpress $myPfam
	python3 $myFile6 $myPfam $myRes5 $myRes6H $myRes6T
	"""
}

myFile7 = file("$baseDir/EJERCICIO7/Ejercicio7.py")
myRes7 = file("$baseDir/resultados/siete.txt")

process siete {

	input: 
	//val proteinas from Exit_5
	file myRes5
	file myFile7
	file myUni
	//val seistab from Exit_6T
	file myRes6T

	//output:
	//file myRes7 into Exit_7

	"""
	python3 $myFile7 $myRes5 $myUni $myRes6T $myRes7
	"""
}






