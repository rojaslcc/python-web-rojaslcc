import reflex as rx
import link_bio.styles.styles as styles
from link_bio.components.navbar import navbar
from link_bio.components.cover import cover
from link_bio.components.footer import footer
from link_bio.views.header.header import header
from link_bio.views.links.links import links
from link_bio.views.sponsors.sponsors import sponsors
from link_bio.state.page_state import PageState
from link_bio.styles.styles import Size


# class State(rx.State):
#     pass


def index() -> rx.Component:
    return rx.box(
        rx.script("document.documentElement.lang='es'"),
        navbar(),
        rx.center(
            rx.vstack(
                cover("cover.png"),
                header(),
                links(),
                sponsors(),
                max_width=styles.MAX_WIDTH,
                width="100%",
                margin_y=Size.BIG.value,
                padding=Size.BIG.value
            )
        ),
        footer(),
        width="100%",
        min_height="100vh", # Asegura que cubra al menos toda la altura de la ventana
        padding="0",
        overflow_x="hidden"
    )

# Configuración de estilos globales para eliminar márgenes por defecto
style = styles.BASE_STYLE
style.setdefault("html", {}).update({"margin": "0", "padding": "0"})
style.setdefault("body", {}).update({"margin": "0", "padding": "0"})
style.setdefault("*", {}).update({"box_sizing": "border-box"})

app = rx.App(
    style=style,
    head_components=[
        rx.el.link(
            rel="shortcut icon",
            href="favicon.ico"
        ),
        rx.el.link(
            rel="stylesheet",
            href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;500&display=swap"
        ),
        rx.el.link(
            rel="stylesheet",
            href="https://fonts.googleapis.com/css2?family=Comfortaa:wght@500&display=swap"
        ),
        rx.script(src="https://www.googletagmanager.com/gtag/js?id=G-3YGHT3XJFS"),
        rx.script(
            """
window.dataLayer = window.dataLayer || [];
function gtag(){dataLayer.push(arguments);}
gtag('js', new Date());
gtag('config', 'G-3YGHT3XJFS');
"""
        ),
    ],
)

app.add_page(
    index,
    title="Amigable Developer H.R.",
    description="Hola, mi nombre es H.R. Rangel, soy Lic. en Ciencias Computacionales y hago contenido de programación.",
    image="avatar.jpg"
)
