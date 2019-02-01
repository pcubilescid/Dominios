# official Python runtime as a parent image
FROM python:3.6     

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt
RUN wget http://eddylab.org/software/hmmer/hmmer.tar.gz
RUN tar xf hmmer.tar.gz
RUN cd hmmer-3.2.1 && ./configure && make && make check && make install

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
ENV NAME PrimerDockerfile

# Run app.py when the container launches
#CMD ["python3", "EJERCICIO4/IDtax_Nombre_NumPro.py uniprot_sprot_mammals.dat.gz resultados/salidaEjercicio4.txt"]
#CMD ["python3", "EJERCICIO5/Proteinas_1Organismo_Fasta.py 39432 uniprot_sprot_mammals.dat.gz resultados/fasta.txt"]
#CMD ["python3", "EJERCICIO6/Ejercicio6.py database/minifam resultados/fasta.txt resultados/salidaEjercicio6.hmm resultados/salidaEjercicio6.txt"]
#CMD ["python3", "EJERCICIO7/Ejercicio7.py resultados/fasta.txt uniprot_sprot_mammals.dat.gz resultados/salidaEjercicio6.txt resultados/diferencias.txt"]


