<div align="center">

# 🌐 LinkBio • H.R. Rangel (@rojaslcc)
### *Amigable Developer • Hub de Enlaces, Proyectos y Contenido*

[![Deploy to Netlify](https://github.com/rojaslcc/linkbio-rojaslcc/actions/workflows/deploy_netlify.yml/badge.svg)](https://github.com/rojaslcc/linkbio-rojaslcc/actions/workflows/deploy_netlify.yml)
[![Netlify](https://img.shields.io/badge/Netlify-Deployed-00C7B7?style=flat-square&logo=netlify&logoColor=white)](https://rojaslcc.netlify.app/)
![Version](https://img.shields.io/badge/version-2.0.0-3AB6A8.svg?style=flat-square)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=flat-square&logo=css3&logoColor=white)
![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-38B2AC?style=flat-square&logo=tailwind-css&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black)
![License](https://img.shields.io/badge/license-GPL--3.0-blue.svg?style=flat-square)

**[Visitar Sitio en Producción 🚀](https://rojaslcc.netlify.app/)**

</div>

---

## 📖 Descripción del Proyecto

**LinkBio RojasLCC v2.0** es una plataforma web interactiva y moderna de tipo *"Link in Bio"* (similar a Linktree) diseñada a medida para **H.R. Rangel (@rojaslcc)**, Licenciado en Ciencias Computacionales, Analista Programador Sr. en Banregio, creador de contenido tecnológico y co-host del pódcast *"Bruddas Tech&Solutions: Tecnología Hoy"*.

Esta aplicación centraliza todos sus perfiles sociales, canales de difusión, proyectos de software destacados, pódcast, repositorios, playlist de código y datos de contacto en una experiencia visual premium, fluida y accesible.

---

## 🚀 Novedades de la Versión 2.0

La versión 2.0 representa una evolución arquitectónica y de diseño completa respecto a la versión anterior:

| Característica | Versión 1.0 (Legacy) | Versión 2.0 (Actual) |
| :--- | :--- | :--- |
| **Arquitectura** | Python + Reflex (Requiere backend activo & WebSocket) | **Sitio Web Estático Puro** (HTML5, Tailwind, Vanilla JS) |
| **Velocidad de Carga** | ~2.5s (Carga de bundle Next.js + WS connect) | **< 250ms (Carga instantánea, 0 TTFB overhead)** |
| **Idiomas** | Solo Español | **Bilingüe (Español / Inglés)** con switch y persistencia |
| **Búsqueda & Filtros** | No disponible | **Búsqueda en tiempo real** y filtros por categorías |
| **Acciones Rápidas** | Enlaces estáticos | **Web Share API, Modal de Código QR, Generador vCard (.vcf) y Copiado rápido** |
| **Diseño Visual** | Componentes estándar Reflex | **Glassmorphism, orbes de luz ambiental, micro-animaciones CSS y paleta de colores de marca** |
| **Infraestructura** | Netlify + Backend Docker en Render | **100% Serverless / Static Hosting en Netlify** |

---

## ✨ Características Principales

- 🌐 **Soporte Bilingüe Completo (ES / EN):** Alterna fluidamente entre Español e Inglés en tiempo real con guardado automático de preferencia en `localStorage`.
- 🔍 **Búsqueda Dinámica & Filtrado por Categorías:** Encuentra proyectos, pódcast, redes o tecnologías rápidamente mediante filtrado instantáneo por texto y chips (*Todos, Destacados, Comunidad, Proyectos, Stack*).
- 📱 **Acciones Rápidas Inteligentes:**
  - **Compartir Perfil:** Integración nativa con la *Web Share API* (y fallback automático al portapapeles).
  - **Código QR:** Generador y visualizador modal de código QR para escanear desde cualquier smartphone.
  - **Guardar Contacto (vCard):** Genera y descarga al instante un archivo de contacto estándar `.vcf` para la agenda telefónica.
  - **Copiar Enlace:** Copiado con un clic acompañado de un toast notification animado.
- 🎨 **Diseño Moderno & Glassmorphism:**
  - Iluminación ambiental interactiva con orbes de luz difuminados animados por CSS.
  - Efectos de desenfoque de fondo (*backdrop-filter*) y tarjetas con elevación sutil al hacer hover.
  - Anillo de pulsación dinámica en el avatar oficial.
- 🛠️ **Showcase de Stack Tecnológico:** Sección interactiva con iconos vectoriales de tecnologías dominadas (Kotlin, Android, ASP.NET Core, Java, C#, Swift, iOS, PostgreSQL, SQL Server, Oracle, Python, Vue.js, etc.).
- 🎵 **Playlist para Desarrolladores:** Integración de acceso directo a la playlist *"Rolas pa programar chidori"* en Apple Music.
- ♿ **Accesibilidad & SEO Optimizado:**
  - Metadatos Open Graph y Twitter Cards completos para previsualizaciones ricas al compartir en redes.
  - Tipografía moderna con fuentes de Google (*Comfortaa* para títulos y *Poppins* para lectura).
  - Estructura semántica HTML5 y soporte completo de navegación responsiva.

---

## 📂 Estructura del Repositorio

```text
linkbio-rojaslcc/
├── .github/
│   └── workflows/
│       └── deploy_netlify.yml   # Pipeline CI/CD automático para Netlify
├── assets/
│   ├── icons/                   # Iconos vectoriales SVG de plataformas y redes
│   ├── stack/                   # Logos vectoriales SVG del stack de tecnologías
│   ├── avatar.jpg               # Fotografía de perfil oficial
│   ├── cover.png                # Imagen de portada / banner
│   ├── favicon.ico              # Favicon del sitio web
│   └── logo.png                 # Logo de marca
├── css/
│   └── styles.css               # Estilos personalizados, keyframes y glassmorphism
├── js/
│   └── app.js                   # Lógica del cliente: i18n, búsqueda, filtros, modales y vCard
├── index.html                   # Documento HTML5 principal estructurado y semántico
├── LICENSE                      # Licencia del proyecto (GPL-3.0)
└── README.md                    # Documentación detallada del proyecto
```

---

## 💻 Desarrollo Local

Para ejecutar y probar el proyecto en tu máquina local:

### Opción 1: Con `npx serve` (Recomendada con Node.js)
```bash
# Clonar el repositorio
git clone https://github.com/rojaslcc/linkbio-rojaslcc.git
cd linkbio-rojaslcc

# Iniciar servidor estático local
npx serve .
```

### Opción 2: Con Python
```bash
python3 -m http.server 3000
```
Abre tu navegador en `http://localhost:3000`.

### Opción 3: Con VS Code
Instala la extensión **Live Server** en Visual Studio Code, abre `index.html` y haz clic en **"Go Live"** en la barra inferior.

---

## 🚀 Despliegue Continuo (CI/CD en Netlify)

El proyecto incluye un flujo de trabajo automatizado con **GitHub Actions** en [`.github/workflows/deploy_netlify.yml`](.github/workflows/deploy_netlify.yml).

### Flujo de Despliegue:
1. Al realizar un `push` a la rama `main` o abrir un `pull_request`, el pipeline de GitHub Actions se activa automáticamente.
2. Descarga el repositorio y publica la carpeta raíz (`.`) en Netlify mediante la acción oficial `nwtgck/actions-netlify@v3`.
3. El sitio web se actualiza en producción en cuestión de segundos.

### Secretos de GitHub Requeridos:
Para configurar este flujo en tu propio fork o repositorio:
- `NETLIFY_AUTH_TOKEN`: Token de acceso personal generado en Netlify (*User Settings > Applications > Personal access tokens*).
- `NETLIFY_SITE_ID`: ID único del sitio en Netlify (*Site configuration > General > Site details > API ID*).

---

## 🛠️ Guía de Personalización

### 1. Agregar o Modificar Enlaces
En [index.html](index.html), localiza las secciones `<section>` dentro de `<main>` y agrega una nueva tarjeta con la clase `glass-card`:

```html
<a href="https://tu-enlace.com" target="_blank" rel="noopener noreferrer"
   class="glass-card flex items-center justify-between p-4 rounded-2xl group"
   data-category="projects" data-keywords="mi nuevo proyecto app kotlin">
  <div class="flex items-center gap-3.5">
    <div class="link-icon-container w-11 h-11 rounded-xl bg-white/5 flex items-center justify-center">
      <img src="assets/icons/web.svg" alt="Icono" class="w-6 h-6">
    </div>
    <div>
      <h3 class="font-semibold text-white text-sm sm:text-base">Nombre del Enlace</h3>
      <p class="text-xs sm:text-sm text-[#C3C7CB]">Descripción breve del recurso</p>
    </div>
  </div>
  <svg class="w-5 h-5 text-[#3AB6A8] link-arrow" ...></svg>
</a>
```

### 2. Actualizar Textos y Traducciones (i18n)
En [js/app.js](js/app.js), edita el objeto `translations` para sincronizar los textos en español (`es`) e inglés (`en`):
```javascript
const translations = {
  es: {
    bio: "Tu biografía en español...",
    // ...
  },
  en: {
    bio: "Your bio in English...",
    // ...
  }
};
```

### 3. Personalizar Colores y Temas
La paleta se encuentra configurada en el script de Tailwind en [index.html](index.html) y como variables CSS en [css/styles.css](css/styles.css):
- `brand.bg`: `#301A4C` (Fondo púrpura profundo)
- `brand.card`: `#472673` (Superficie de tarjetas)
- `brand.teal`: `#3AB6A8` (Color de acento teal)
- `brand.tealDark`: `#236860` (Teal de contraste y hover)

---

## 👨‍💻 Autor

**H.R. Rangel (@rojaslcc)**
- 💼 **LinkedIn:** [H.R. Rangel](https://www.linkedin.com/in/rojaslcc/)
- 💻 **GitHub:** [@rojaslcc](https://github.com/rojaslcc)
- 🎙️ **Pódcast:** [BTS: Tecnología Hoy](https://www.youtube.com/@bts_tecnologiahoy)
- 🐦 **X (Twitter):** [@rojaslcc](https://x.com/rojaslcc)
- 🌐 **Sitio Web:** [rojaslcc.netlify.app](https://rojaslcc.netlify.app/)
- ✉️ **Contacto:** [rojaslcc@outlook.com](mailto:rojaslcc@outlook.com)

---

## 📄 Licencia

Este proyecto está distribuido bajo la licencia **GNU General Public License v3.0**. Consulta el archivo [LICENSE](LICENSE) para más detalles.