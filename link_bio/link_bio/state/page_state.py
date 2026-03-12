import reflex as rx
from link_bio.i18n import translations

class PageState(rx.State):
    lang: str = "es"
    i18n: dict = translations["es"]

    def set_language_es(self):
        self.lang = "es"
        self.i18n = translations["es"]
        print(f"Idioma cambiado a: {self.lang} (Español)", flush=True)
    
    def set_language_en(self):
        self.lang = "en"
        self.i18n = translations["en"]
        print(f"Idioma cambiado a: {self.lang} (Inglés)", flush=True)