#Establecer el Sistema Operativo
FROM alpine:3.10

#Instalar Python3
RUN apk add --no-cache python3-dev \
    && pip3 install --upgrade pip

#Preparando el Directorio de Trabajo
WORKDIR /app

#Copiando la Aplicación al Contenedor
COPY . /app/

#Cargando los Requerimientos de la Aplicación
RUN pip3 --no-cache-dir install -r requeriments.txt

#Ejecutando la Aplicación Web e indicando cual es el Programa de Inicio
CMD ["python3","src/index.py"]

