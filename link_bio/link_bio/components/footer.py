import reflex as rx
import datetime
import link_bio.constants as const
from link_bio.styles.styles import Size
from link_bio.styles.colors import Color, TextColor
from link_bio.state.page_state import PageState
from link_bio.i18n import Trans


def footer() -> rx.Component:
    return rx.vstack(
        rx.image(
            src="logo.png",
            height=Size.VERY_BIG.value,
            width=Size.VERY_BIG.value,
            alt="Logotipo de RojasLCC. Una \"erre\"."
        ),
        rx.text(
            f"{PageState.i18n[Trans.FOOTER_RIGHTS]}{datetime.date.today().year}",
            font_size=Size.MEDIUM.value
        ),
        rx.link(
            rx.box(
                rx.text(PageState.i18n[Trans.FOOTER_SUBTITLE], as_="span", color=Color.PRIMARY.value),
                " v1.0.0",
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
            rx.text("|", as_="span", color=Color.PRIMARY.value),
            " NEVER WASTE GOOD TECH.",
            font_size=Size.SMEDIUM.value,
            margin_top=Size.ZERO.value
        ),
        width="100%",
        align_items="center",
        padding_bottom=Size.BIG.value,
        padding_x=Size.BIG.value,
        gap=Size.DEFAULT.value,
        color=TextColor.FOOTER.value
    )
