#!/bin/bash

set -e
# Este ejemplo comprueba si existe un directorio, para crearlo y llenarlo de lo que quieras
if [ ! -f /database/minifam ] ; then
	# Crea el directorio
	mkdir -p /database
	# Cambia a él
	cd /database
	
	wget http://ftp.ebi.ac.uk/pub/databases/uniprot/current_release/knowledgebase/taxonomic_divisions/uniprot_sprot_mammals.dat.gz
	
	wget http://ftp.ebi.ac.uk/pub/databases/Pfam/releases/Pfam32.0/Pfam-A.hmm.gz
	
	gzip -d Pfam-A.hmm.gz
	
	mv Pfam-A.hmm minifam
	hmmpress minifam

	# Going back to the working directory
	cd /app
fi

# Por último, ejecuta lo que haya en el CMD
exec "$@"
