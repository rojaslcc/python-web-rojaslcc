# Proyecto Link Bio RojasLCC

Este es un proyecto web creado en Python que funciona como una página de "link in bio", similar a Linktree, permitiendo a los usuarios mostrar múltiples enlaces en una sola página.

## Tecnologías Utilizadas

El proyecto está construido principalmente con las siguientes tecnologías:

-   **Python**: Lenguaje de programación principal para el backend.
-   **Reflex**: Un framework de desarrollo web para Python (versión 0.8.26) que permite construir aplicaciones web completas en Python puro, generando un frontend en **Next.js**.
-   **Pydantic**: Utilizado para la validación de datos.

## Estructura de Carpetas

La estructura del proyecto está organizada de la siguiente manera:

```
/
├── link_bio/               # Directorio raíz de la aplicación Reflex
│   ├── assets/             # Archivos estáticos (imágenes, CSS, etc.)
│   ├── link_bio/           # Lógica principal de la aplicación
│   │   ├── components/     # Componentes reutilizables de la UI
│   │   ├── pages/          # Vistas principales de la aplicación
│   │   ├── styles/         # Estilos y temas de la aplicación
│   │   └── constants.py    # Constantes utilizadas en el proyecto
│   ├── public/             # Contenido del frontend generado para producción
│   ├── venv/               # Entorno virtual de Python
│   ├── build.sh            # Script para construir el frontend
│   ├── requirements.txt    # Dependencias de Python
│   └── rxconfig.py         # Configuración de la aplicación Reflex
└── README.md               # Este archivo
```

## Proceso para Despliegue Local

Para ejecutar este proyecto en tu entorno local, sigue estos pasos:

1.  **Clona el repositorio (si no lo has hecho):**

    ```bash
    git clone https://github.com/rojaslcc/python-web-rojaslcc
    cd python-web-rojaslcc
    ```

2.  **Navega al directorio de la aplicación:**

    ```bash
    cd link_bio
    ```

3.  **Crea y activa un entorno virtual:**

    ```bash
    python -m venv venv
    source venv/bin/activate
    ```

    *En Windows, usa `venv\Scripts\activate`*

4.  **Instala las dependencias:**

    ```bash
    pip install --upgrade pip
    pip install -r requirements.txt
    ```

5.  **Inicializa la aplicación Reflex:**

    Este comando prepara la aplicación y las dependencias de frontend.

    ```bash
    reflex init
    ```

6.  **Ejecuta el servidor de desarrollo:**

    ```bash
    reflex run
    ```

    La aplicación estará disponible en `http://localhost:3000`. El servidor se recargará automáticamente al detectar cambios en el código.

## Proceso de Build para Producción

Si deseas generar los archivos estáticos del frontend para un despliegue en producción, puedes usar el script `build.sh`.

```bash
./build.sh
```

Este script realizará los siguientes pasos:
1.  Activa el entorno virtual.
2.  Instala las dependencias.
3.  Inicializa Reflex.
4.  Exporta el frontend (`reflex export --frontend-only`).
5.  Descomprime los archivos generados en la carpeta `public/`.

> **⚠️ Nota Importante:** Reflex no es un sitio estático puro. Requiere obligatoriamente un backend de Python en ejecución para gestionar la conexión WebSocket. Si solo subes el frontend a Netlify sin el backend, obtendrás errores de conexión.

## Guía de Despliegue (Frontend + Backend)

Para producción, la arquitectura se divide en dos partes:

### 1. Backend (Render)

El backend se encarga de la lógica y el estado. Se despliega usando **Docker**.

1.  Sube tu código a GitHub.
2.  En Render, crea un **Web Service**.
3.  Conecta tu repositorio y configura:
    *   **Root Directory:** `link_bio`
    *   **Runtime:** Docker
4.  Una vez desplegado, copia la URL asignada (ej: `https://rojaslcc.onrender.com`).

### 2. Frontend (Netlify)

El frontend es la parte visual que se conecta al backend.

1.  Asegúrate de configurar la `api_url` en `rxconfig.py` apuntando a tu backend de Render.
2.  Ejecuta `./build.sh` en tu máquina local.
3.  Sube el contenido de la carpeta `public/` generada a **Netlify**.
