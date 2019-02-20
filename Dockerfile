# official Python runtime as a parent image
FROM python:3.6     

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD EJERCICIO* docker-build.sh requirements.txt /app/

RUN ln -s /usr/local/bin/entrypoint.sh / # backwards compat

# Install any needed packages specified in requirements.txt
RUN ./docker-build.sh

ADD entrypoint.sh /app

# Make port 80 available to the world outside this container
#EXPOSE 80

# Define environment variable
#ENV NAME PrimerDockerfile

ENTRYPOINT ["bash","entrypoint.sh"]


