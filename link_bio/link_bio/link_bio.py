import reflex as rx
import link_bio.styles.styles as styles
from link_bio.components.navbar import navbar
from link_bio.components.footer import footer
from link_bio.views.header.header import header
from link_bio.views.links.links import links
from link_bio.views.sponsors.sponsors import sponsors
from link_bio.styles.styles import Size


# class State(rx.State):
#     pass


def index() -> rx.Component:
    return rx.box(
        rx.script("document.documentElement.lang='es'"),
        navbar(),
        rx.center(
            rx.vstack(
                header(),
                links(),
                #sponsors(),
                max_width=styles.MAX_WIDTH,
                width="100%",
                margin_y=Size.BIG.value,
                padding=Size.BIG.value
            )
        ),
        footer()
    )


app = rx.App(
    style=styles.BASE_STYLE,
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

app.compile()
