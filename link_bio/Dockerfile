# Usar una imagen ligera de Python
FROM python:3.11-slim

# Establecer el directorio de trabajo
WORKDIR /app

# Instalar dependencias del sistema necesarias (unzip es requerido por Reflex)
RUN apt-get update && apt-get install -y \
    unzip \
    && rm -rf /var/lib/apt/lists/*

# Copiar dependencias e instalarlas
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el código de la aplicación
COPY . .

# Exponer el puerto 8000 para que Render sepa dónde escuchar
EXPOSE 8000

# Comando para iniciar solo el backend en producción
CMD ["reflex", "run", "--env", "prod", "--backend-only"]
