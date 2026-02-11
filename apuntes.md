APUNTES DOCKER

Def máquina virtual: es un ordenador dentro de un ordenador. Más ineficientes que los contenedores. 

Def docker: ejecutar aplicaciones dentro de contenedores. Solo incluyo lo que necesito. Consigo estar en la misma versión, mismo entorno etc. 

Docker: es una plantilla en la que se incluye todo lo necesario para ejecutar una aplicacion. Tiene todo los necesario y los pasos, pero todavía no se ha creado. 

ej. imagen: python 3.10, el cual incluye un entorno python ya configurado.

def contenedor: es la imagen puesta en marcha, es decir es la imagen puesta en marcha con un sistema de archivos procesos y recursos aislados.

FASES:
Dockerfile: archivo que cuenta con instrucciones para crear una imagen. 
Hacemos build
Dockerimage: instantánea de 
Hacemos run
Container: imagen cuando empieza a funcionar


COMANDOS
docker ps : para mostrar el contenedor
docker ps -a
docker ps -a | grep pepe: grep es como un finder, queme ayuda a buscar. 
docker ps -a | grep Carla hello-world: grep me esta buscando dentro de carla hello world

Este contenedor se mantiene, no es efímero como puede ser el ejemplo que hemos hecho anteriormente. Sin el 80 no me va, pero tambien podria poner cualquier número. 

docker run --name-sever - 80:80 ngin
% docker run --name Carla hello-world: hello world es el nombre de la imagen. Asi creo un contenedor

DOCKER HUB: como el git pero de docker, para subir cosas.


DOCKER 2 (17 DE OCTUBRE)


## DOCKERFILE
ejemplo construccion dockerfile 
FROM python:3.11-slim       con from instalo la versión de python que queramos. Con slim significa que es una versión ligera. 

WORKDIR /app         Define donde se harán todas las operaciones dentro del contenedor. Con la barra me sitúo donde estoy


COPY . .             copiamos el resto del código de la aplicación. Paso del host al contenedor. El primer punto marca el host y el segundo el contenedor en el que estamos, siguiendo el ejemplo, estoy en el contenedor app. 

CMD ["python", "main.py"]  definimos el comando que arranca la aplicación (comando) El primero es el intérprete y el segundo es el archivo. 

## CONSTRUCCIÓN IMAGEN
1º docker build -t carla:latest .
2º docker run -d carla #tomando a carla como el nombre del archivo, me arranca el contenedor 
3ª docker images #para ver las imagenes y que tengo la que he creado 
4ºdocker logs + (número de identificación)        #me permite ver los logs o pegando el número largo
5ºdocker exec + (número de identificación )       #correr un contenedor que ya esta en marcha
6º docker run --rm #para borrar e incluimos el nombre
7º docker ps #para ver que comtenedores activos hay
-it :iteractivo
-p : para poner puertos
8080:80 es ------> host:container

# COPIAR COMANDOS HASTA LA DIAPO DE ANTES DEL VOLUMEN

## QUE ES EL VOLUMEN??? ---> PARA CONECTAR NUESTRO PORTATIL CON EL DOCKER
Un volumen es una carpeta (o disco) que Docker usa para guardar datos de forma permanente, fuera del contenedor.


CMD (te da una versión)= ENTRYPOINT (me obliga a hacer python), cuando quiero establecer la conexión a la base de datos. 

## INSTALACIÓN DE LIBRERIAS EN DOCKER
pip install: descargo libreria, puedo utilizarla en python para lo que quiera, reutilizarlo.

La libreria es un conjunto de módulos que se sube a internet y que puedo utilizar.

me llevo la libreria a main.py desde from (nombre de la libreria) con import* me las lleva todas. 

api: nos trae informacion ej. catfact

## DOCKER COMPOSE
Puedo ejecutar varios servicios en contenedores

















