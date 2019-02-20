Realizado y datos descargados 20/02/2019

Serie de programas que ayudan a comprobar, cuantos de los dominios Pfam mas relevantes encontrados en sus proteinas conocidas en UniProt SW coinciden con los dominios anotados.

Los organismos a buscar son el mono ardilla boliviano y el chimpace

Para facilitar la busqueda de estos organimos tenemos la siguiente informacion:

· Chimpanzee (Pan)

https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?mode=Info&id=9596&lvl=3&p=has_linkout&p=blast_url&p=genome_blast&lin=f&keep=1&srchmode=1&unlock

- Taxonomy ID: 9596 (for references in articles please use NCBI:txid9596) Pan 
- Taxonomy ID: 9597 (for references in articles please use NCBI:txid9597) Pan paniscus
- Taxonomy ID: 9598 (for references in articles please use NCBI:txid9598) Pan troglodytes


· Black-capped squirrel monkey(Saimiri boliviensis)

https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?mode=Info&id=39432&lvl=3&p=mapview&p=has_linkout&p=blast_url&p=genome_blast&lin=f&keep=1&srchmode=1&unlock

- Taxonomy ID: 39432 (for references in articles please use NCBI:txid39432)


Necesidades para el funcionamiento de los programas: 

· Python

- Version 3 de python
- librerias especificas, en requirements.txt 


· Docker

- sudo apt-get install docker-ce

Para correr los programas: 

docker run --rm -ti -v /home/pacuci/Desktop/projects/Dominios:/app/data -v /home/pacuci/Desktop/projects/Dominios/DB:/database dominios5 python3 ... parametros segun que programa ejecutes


