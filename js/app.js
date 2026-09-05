/**
 * Amigable Developer H.R. (rojaslcc) - Link in Bio Application Logic
 * Modern, accessible, bilingual, and interactive link hub.
 */

// --- Content Translations Dictionary ---
const translations = {
  es: {
    role: "@rojaslcc",
    bio: "Soy licenciado en ciencias computacionales y actualmente trabajo para Banregio como analista programador Sr. Además, creo contenido sobre programación y tecnología en general en redes sociales. Aquí podrás encontrar todos mis enlaces de interés ¡Bienvenid@!",
    statusText: "Disponible para colaboraciones y proyectos",
    statExp: "12+ años de experiencia",
    statApps: "2+ apps públicas creadas",
    statFollowers: "17K+ seguidores en redes",
    
    // Quick Actions
    actionShare: "Compartir Perfil",
    actionQr: "Código QR",
    actionVcard: "Guardar Contacto",
    actionCopy: "Copiar Enlace",

    // Search & Filter
    searchPlaceholder: "Buscar proyectos, podcasts, redes...",
    filterAll: "Todos",
    filterFeatured: "Destacados",
    filterCommunity: "Comunidad",
    filterProjects: "Proyectos",
    filterStack: "Stack Tech",
    noResults: "No se encontraron enlaces con ese criterio de búsqueda.",

    // Section Titles
    secFeatured: "Lo nuevo & Destacado",
    secCommunity: "Comunidad & Contenido",
    secProjects: "Proyectos & Recursos",
    secContact: "Contacto Directo",
    secStack: "Mi Stack Tecnológico",
    secMusic: "Playlist de Código",

    // Card Translations
    altosTitle: "Sitio web de Altos Interactive",
    altosDesc: "Desarrollo de software y soluciones digitales a medida.",
    podcastTitle: "Pódcast 'Bruddas Tech&Solutions: Tecnología Hoy'",
    podcastBadge: "Nuevo capítulo cada semana",
    podcastDesc: "Acompáñanos a desmenuzar la tecnología con un nuevo episodio cada domingo 12:00 PM (Hora CDMX).",
    
    fbMainTitle: "RojasLCC Tutoriales y más",
    fbMainDesc: "Mi página de Facebook principal sobre código y tecnología.",
    fbBtsTitle: "Bruddas Tech&Solutions",
    fbBtsDesc: "Proyecto de creación de contenido digital sobre software.",
    fbAltosTitle: "Altos Interactive en Facebook",
    fbAltosDesc: "Co-fundador de startup para el desarrollo de software.",
    twitchTitle: "Canal de Twitch",
    twitchDesc: "Transmisiones en vivo sobre programación, software y tech.",
    ytPersonalTitle: "YouTube • Canal Personal",
    ytPersonalDesc: "Vlogs, reflexiones y experiencias de desarrollo.",
    ytTutorialsTitle: "YouTube • Canal de Tutoriales",
    ytTutorialsDesc: "Tutoriales sobre desarrollo de software y guías técnicas.",
    ytBtsTitle: "YouTube • Canal BTS Pódcast",
    ytBtsDesc: "Hogar oficial del pódcast BTS: Tecnología Hoy.",

    blogTitle: "Blog Personal",
    blogDesc: "Artículos, reflexiones y notas sobre desarrollo y tecnología.",
    appAndroidTitle: "App Android e-UANL Campus Digital",
    appAndroidDesc: "App móvil nativa en Kotlin para mi alma mater U.A.N.L.",
    appClipsiTitle: "App Web CLIPSI UANL",
    appClipsiDesc: "Sistema web desarrollado en ASP.NET Core para la Fac. de Psicología UANL.",
    appPokedexTitle: "In Development: POKÉDEX",
    appPokedexDesc: "Proyecto interactivo en Vue.js desarrollado para Microsoft LaunchX.",
    appPasteleriaTitle: "App Web MiPasteleria",
    appPasteleriaDesc: "Proyecto de práctica en ASP.NET Core, HTML5 y CSS3.",

    emailTitle: "Correo Electrónico",
    emailDesc: "rojaslcc@outlook.com",

    musicTitle: "Rolas pa programar chidori",
    musicDesc: "Mi playlist seleccionada en Apple Music para entrar en modo flow.",
    listenBtn: "Escuchar en Apple Music",

    footerQuote1: "SOME SEE SELF-DOUBT AS AN INVITATION TO BE GREATER.",
    footerQuote2: "LIFE IS GOOD, BUT IT CAN BE. | NEVER WASTE GOOD TECH.",
    footerAppVer: "Amigable Developer H.R. v2.0.0",

    // Modals & Toast
    qrModalTitle: "Código QR del Perfil",
    qrModalDesc: "Escanea para abrir este perfil en cualquier smartphone o tablet.",
    closeBtn: "Cerrar",
    copySuccessToast: "¡Enlace copiado al portapapeles con éxito! 🚀",
    vcardSuccessToast: "¡Contacto de H.R. Rangel generado y descargado! 📇"
  },
  en: {
    role: "@rojaslcc",
    bio: "I have a degree in computer science and currently work for Banregio as a Sr. Programmer Analyst. In addition, I create content about software engineering and technology across social media. Here you can find all my featured links. Welcome!",
    statusText: "Open for collaborations and projects",
    statExp: "12+ years of experience",
    statApps: "2+ public apps created",
    statFollowers: "17K+ social followers",

    // Quick Actions
    actionShare: "Share Profile",
    actionQr: "QR Code",
    actionVcard: "Save Contact",
    actionCopy: "Copy Link",

    // Search & Filter
    searchPlaceholder: "Search projects, podcast, socials...",
    filterAll: "All",
    filterFeatured: "Featured",
    filterCommunity: "Community",
    filterProjects: "Projects",
    filterStack: "Tech Stack",
    noResults: "No matching links found with that query.",

    // Section Titles
    secFeatured: "What's New & Featured",
    secCommunity: "Community & Content",
    secProjects: "Projects & Resources",
    secContact: "Direct Contact",
    secStack: "My Tech Stack",
    secMusic: "Coding Playlist",

    // Card Translations
    altosTitle: "Altos Interactive Website",
    altosDesc: "Custom software development and digital engineering solutions.",
    podcastTitle: "Podcast 'Bruddas Tech&Solutions: Tech Today'",
    podcastBadge: "New episode every week",
    podcastDesc: "Join us as we break down modern tech with a new episode every Sunday at 12:00 PM (CDMX time).",

    fbMainTitle: "RojasLCC Tutorials & More",
    fbMainDesc: "My primary Facebook page focused on coding and technology.",
    fbBtsTitle: "Bruddas Tech&Solutions",
    fbBtsDesc: "Digital tech content and software discussions project.",
    fbAltosTitle: "Altos Interactive on Facebook",
    fbAltosDesc: "Co-founder of software development startup.",
    twitchTitle: "Twitch Channel",
    twitchDesc: "Live streaming sessions on programming, software, and tech.",
    ytPersonalTitle: "YouTube • Personal Channel",
    ytPersonalDesc: "Vlogs, dev life reflections, and tech journey insights.",
    ytTutorialsTitle: "YouTube • Coding Tutorials",
    ytTutorialsDesc: "Step-by-step programming tutorials and technical guides.",
    ytBtsTitle: "YouTube • BTS Podcast Channel",
    ytBtsDesc: "Official home of the BTS: Tech Today podcast series.",

    blogTitle: "Personal Blog",
    blogDesc: "Articles, reflections, and notes on programming and tech.",
    appAndroidTitle: "e-UANL Campus Digital Android App",
    appAndroidDesc: "Native Kotlin mobile app built for my alma mater U.A.N.L.",
    appClipsiTitle: "CLIPSI UANL Web Platform",
    appClipsiDesc: "ASP.NET Core web system built for the Psychology School at UANL.",
    appPokedexTitle: "In Development: POKÉDEX",
    appPokedexDesc: "Interactive Vue.js project built for Microsoft LaunchX Bootcamp.",
    appPasteleriaTitle: "MiPasteleria Web App",
    appPasteleriaDesc: "ASP.NET Core, HTML5, and CSS3 web application exercise.",

    emailTitle: "Email Address",
    emailDesc: "rojaslcc@outlook.com",

    musicTitle: "Rolas pa programar chidori",
    musicDesc: "My handpicked Apple Music playlist to get into deep coding flow.",
    listenBtn: "Listen on Apple Music",

    footerQuote1: "SOME SEE SELF-DOUBT AS AN INVITATION TO BE GREATER.",
    footerQuote2: "LIFE IS GOOD, BUT IT CAN BE. | NEVER WASTE GOOD TECH.",
    footerAppVer: "Amigable Developer H.R. v2.0.0",

    // Modals & Toast
    qrModalTitle: "Profile QR Code",
    qrModalDesc: "Scan to open this link-in-bio hub on any phone or device.",
    closeBtn: "Close",
    copySuccessToast: "Profile link copied to clipboard! 🚀",
    vcardSuccessToast: "H.R. Rangel contact vCard generated and downloaded! 📇"
  }
};

// --- Application State ---
let currentLang = localStorage.getItem('rojaslcc_lang') || 'es';
let currentCategory = 'all';

// --- Initialization ---
document.addEventListener('DOMContentLoaded', () => {
  initLanguage();
  initSearchAndFilters();
  initModals();
  initActions();
  initMusicEmbed();
});

// --- Language Controller ---
function initLanguage() {
  applyLanguage(currentLang);

  const btnEs = document.getElementById('lang-es');
  const btnEn = document.getElementById('lang-en');

  if (btnEs) {
    btnEs.addEventListener('click', () => setLanguage('es'));
  }
  if (btnEn) {
    btnEn.addEventListener('click', () => setLanguage('en'));
  }
}

function setLanguage(lang) {
  currentLang = lang;
  localStorage.setItem('rojaslcc_lang', lang);
  applyLanguage(lang);
}

function applyLanguage(lang) {
  const t = translations[lang];
  if (!t) return;

  // Update dynamic i18n DOM elements
  document.querySelectorAll('[data-i18n]').forEach((el) => {
    const key = el.getAttribute('data-i18n');
    if (t[key]) {
      el.textContent = t[key];
    }
  });

  // Update placeholders
  document.querySelectorAll('[data-i18n-placeholder]').forEach((el) => {
    const key = el.getAttribute('data-i18n-placeholder');
    if (t[key]) {
      el.placeholder = t[key];
    }
  });

  // Update title attributes
  document.querySelectorAll('[data-i18n-title]').forEach((el) => {
    const key = el.getAttribute('data-i18n-title');
    if (t[key]) {
      el.title = t[key];
    }
  });

  // Update HTML lang attribute
  document.documentElement.lang = lang;

  // Update active styling on flag buttons
  const btnEs = document.getElementById('lang-es');
  const btnEn = document.getElementById('lang-en');
  if (btnEs && btnEn) {
    if (lang === 'es') {
      btnEs.classList.remove('opacity-40', 'grayscale');
      btnEs.classList.add('opacity-100', 'scale-110');
      btnEn.classList.add('opacity-40', 'grayscale');
      btnEn.classList.remove('opacity-100', 'scale-110');
    } else {
      btnEn.classList.remove('opacity-40', 'grayscale');
      btnEn.classList.add('opacity-100', 'scale-110');
      btnEs.classList.add('opacity-40', 'grayscale');
      btnEs.classList.remove('opacity-100', 'scale-110');
    }
  }
}

// --- Search and Category Filter Controller ---
function initSearchAndFilters() {
  const searchInput = document.getElementById('link-search-input');
  const filterChips = document.querySelectorAll('.filter-chip');
  const linkCards = document.querySelectorAll('.link-card-item');
  const emptyState = document.getElementById('no-results-state');

  function filterLinks() {
    const query = (searchInput ? searchInput.value : '').toLowerCase().trim();
    let visibleCount = 0;

    linkCards.forEach((card) => {
      const category = card.getAttribute('data-category') || '';
      const textContent = card.textContent.toLowerCase();
      const matchesCategory = (currentCategory === 'all') || (category === currentCategory);
      const matchesSearch = query === '' || textContent.includes(query);

      if (matchesCategory && matchesSearch) {
        card.style.display = 'block';
        visibleCount++;
      } else {
        card.style.display = 'none';
      }
    });

    // Handle sections visibility
    document.querySelectorAll('.link-section').forEach((section) => {
      const visibleCardsInSection = section.querySelectorAll('.link-card-item[style="display: block;"]');
      if (visibleCardsInSection.length === 0 && query !== '') {
        section.style.display = 'none';
      } else {
        section.style.display = 'block';
      }
    });

    if (emptyState) {
      emptyState.classList.toggle('hidden', visibleCount > 0);
    }
  }

  if (searchInput) {
    searchInput.addEventListener('input', filterLinks);
    
    // Clear search button if clicked
    const clearBtn = document.getElementById('clear-search-btn');
    if (clearBtn) {
      clearBtn.addEventListener('click', () => {
        searchInput.value = '';
        filterLinks();
        searchInput.focus();
      });
    }
  }

  filterChips.forEach((chip) => {
    chip.addEventListener('click', () => {
      filterChips.forEach((c) => c.classList.remove('active'));
      chip.classList.add('active');
      currentCategory = chip.getAttribute('data-filter') || 'all';
      filterLinks();
    });
  });
}

// --- Quick Actions: Copy, Share, QR, vCard ---
function initActions() {
  // 1. Copy Link button
  const copyBtn = document.getElementById('btn-copy-profile');
  if (copyBtn) {
    copyBtn.addEventListener('click', () => {
      copyToClipboard(window.location.href);
    });
  }

  // 2. Share Profile button
  const shareBtn = document.getElementById('btn-share-profile');
  if (shareBtn) {
    shareBtn.addEventListener('click', async () => {
      if (navigator.share) {
        try {
          await navigator.share({
            title: 'H.R. Rangel (@rojaslcc) | Amigable Developer',
            text: 'Descubre los proyectos, podcast y redes de H.R. Rangel (@rojaslcc)',
            url: window.location.href
          });
        } catch (err) {
          // Fallback if user cancels or fails
          if (err.name !== 'AbortError') {
            copyToClipboard(window.location.href);
          }
        }
      } else {
        copyToClipboard(window.location.href);
      }
    });
  }

  // 3. QR Code button
  const qrBtn = document.getElementById('btn-qr-profile');
  if (qrBtn) {
    qrBtn.addEventListener('click', openQrModal);
  }

  // 4. Download vCard button
  const vcardBtn = document.getElementById('btn-vcard-profile');
  if (vcardBtn) {
    vcardBtn.addEventListener('click', downloadVCard);
  }
}

// Copy to clipboard helper with Toast
function copyToClipboard(text) {
  navigator.clipboard.writeText(text).then(() => {
    const t = translations[currentLang] || translations.es;
    showToast(t.copySuccessToast);
  }).catch(() => {
    // Fallback prompt
    prompt('Copia este enlace:', text);
  });
}

// Download vCard (.vcf)
function downloadVCard() {
  const vcardData = [
    'BEGIN:VCARD',
    'VERSION:3.0',
    'N:Rangel;H.R.;;;',
    'FN:H.R. Rangel (@rojaslcc)',
    'ORG:Banregio / Altos Interactive',
    'TITLE:Lic. Ciencias Computacionales & Analista Programador Sr.',
    'EMAIL;type=INTERNET;type=WORK:rojaslcc@outlook.com',
    'URL:https://rojaslcc.netlify.app/',
    'URL;type=GitHub:https://github.com/rojaslcc',
    'URL;type=Twitter:https://x.com/rojaslcc',
    'URL;type=Instagram:https://instagram.com/rojaslcc',
    'URL;type=LinkedIn:https://linkedin.com/in/rojaslcc',
    'NOTE:Creador de contenido y Analista Programador. Amigable Developer H.R.',
    'END:VCARD'
  ].join('\r\n');

  const blob = new Blob([vcardData], { type: 'text/vcard;charset=utf-8;' });
  const url = URL.createObjectURL(blob);
  const link = document.createElement('a');
  link.href = url;
  link.setAttribute('download', 'HR_Rangel_rojaslcc.vcf');
  document.body.appendChild(link);
  link.click();
  document.body.removeChild(link);
  URL.revokeObjectURL(url);

  const t = translations[currentLang] || translations.es;
  showToast(t.vcardSuccessToast);
}

// Toast notification
function showToast(message) {
  let toastContainer = document.getElementById('toast-container');
  if (!toastContainer) {
    toastContainer = document.createElement('div');
    toastContainer.id = 'toast-container';
    toastContainer.className = 'fixed bottom-6 right-6 z-50 flex flex-col gap-2 max-w-sm w-full pointer-events-none px-4';
    document.body.appendChild(toastContainer);
  }

  const toast = document.createElement('div');
  toast.className = 'toast-animate pointer-events-auto flex items-center gap-3 bg-[#472673] border border-[#3AB6A8]/70 text-[#F1F2F4] px-4 py-3 rounded-xl shadow-2xl backdrop-blur-lg';
  toast.innerHTML = `
    <div class="flex-shrink-0 w-8 h-8 rounded-full bg-[#3AB6A8]/20 flex items-center justify-center text-[#3AB6A8]">
      <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path>
      </svg>
    </div>
    <div class="flex-1 text-sm font-medium leading-snug">${message}</div>
  `;

  toastContainer.appendChild(toast);

  setTimeout(() => {
    toast.style.opacity = '0';
    toast.style.transform = 'translateY(15px)';
    toast.style.transition = 'all 0.3s ease';
    setTimeout(() => {
      if (toast.parentNode) {
        toast.parentNode.removeChild(toast);
      }
    }, 300);
  }, 3500);
}

// --- Modals Controller ---
function initModals() {
  const qrModal = document.getElementById('qr-modal');
  const closeQrBtns = document.querySelectorAll('.close-qr-modal');

  closeQrBtns.forEach((btn) => {
    btn.addEventListener('click', closeQrModal);
  });

  if (qrModal) {
    qrModal.addEventListener('click', (e) => {
      if (e.target === qrModal) {
        closeQrModal();
      }
    });
  }

  // Keyboard Escape
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') {
      closeQrModal();
    }
  });
}

function openQrModal() {
  const qrModal = document.getElementById('qr-modal');
  const qrImageContainer = document.getElementById('qr-code-img');
  const currentUrl = window.location.href.split('#')[0];

  if (qrImageContainer) {
    // Generate QR using high-resolution API with brand colors (#301A4C and #3AB6A8)
    const encodedUrl = encodeURIComponent(currentUrl);
    const qrSrc = `https://api.qrserver.com/v1/create-qr-code/?size=280x280&color=30-26-76&bgcolor=FFFFFF&data=${encodedUrl}`;
    qrImageContainer.src = qrSrc;
  }

  if (qrModal) {
    qrModal.classList.remove('hidden');
    qrModal.classList.add('flex');
    document.body.style.overflow = 'hidden';
  }
}

function closeQrModal() {
  const qrModal = document.getElementById('qr-modal');
  if (qrModal) {
    qrModal.classList.add('hidden');
    qrModal.classList.remove('flex');
    document.body.style.overflow = '';
  }
}

// --- Music Player Widget Interaction ---
function initMusicEmbed() {
  const musicCard = document.getElementById('apple-music-card');
  if (musicCard) {
    musicCard.addEventListener('mouseenter', () => {
      const icon = musicCard.querySelector('.music-note-icon');
      if (icon) icon.classList.add('animate-bounce');
    });
    musicCard.addEventListener('mouseleave', () => {
      const icon = musicCard.querySelector('.music-note-icon');
      if (icon) icon.classList.remove('animate-bounce');
    });
  }
}
