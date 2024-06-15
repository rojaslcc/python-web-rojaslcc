import reflex as rx
import datetime
import link_bio.constants as const
import link_bio.styles.styles as styles
from link_bio.styles.styles import Size
from link_bio.styles.colors import Color, TextColor


def footer() -> rx.Component:
    return rx.vstack(
        rx.image(
            src="logo.png",
            height=Size.VERY_BIG.value,
            width=Size.VERY_BIG.value,
            alt="Logotipo de RojasLCC. Una \"erre\"."
        ),
        rx.text(
            f"© 2014-{datetime.date.today().year}",
            font_size=Size.MEDIUM.value
        ),
        rx.link(
            rx.box(
                rx.span("RojasLCC by Humberto Rojas", color=Color.PRIMARY.value),
                " v1."
            ),
            href=const.ROJASLCC_URL,
            is_external=True,
            font_size=Size.MEDIUM.value
        ),
        rx.text(
            "SOME SEE SELF-DOUBT AS AN INVITATION TO BE GREATER.",
            font_size=Size.SMEDIUM.value,
            margin_top=Size.ZERO.value
        ),
        rx.box(
            f"LIFE IS GOOD, BUT IT CAN BE. ",
            rx.span("|", color=Color.PRIMARY.value),
            " NEVER WASTE GOOD TECH.",
            font_size=Size.SMEDIUM.value,
            margin_top=Size.ZERO.value
        ),
        margin_bottom=Size.BIG.value,
        padding_bottom=Size.BIG.value,
        padding_x=Size.BIG.value,
        spacing=Size.DEFAULT.value,
        color=TextColor.FOOTER.value
    )
