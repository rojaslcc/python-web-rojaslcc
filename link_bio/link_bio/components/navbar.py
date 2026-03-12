import reflex as rx
import link_bio.styles.styles as styles
from link_bio.styles.styles import Size
from link_bio.styles.colors import Color
from link_bio.state.page_state import PageState


def navbar() -> rx.Component:
    return rx.flex(
        rx.box(
            rx.text("rojas", as_="span", color=Color.PRIMARY.value),
            rx.text("lcc", as_="span", color=Color.SECONDARY.value),
            style=styles.navbar_title_style
        ),
        rx.hstack(
            rx.button(
                "🇲🇽",
                on_click=PageState.set_language_es,
                font_size=Size.BIG.value,
                variant="ghost",
                width="auto",
                height="auto",
                min_width="auto",
                padding="0",
                background_color="transparent",
                style={
                    "filter": rx.cond(PageState.lang == "es", "none", "grayscale(100%)"),
                    "position": "relative",
                },
                _hover={"background_color": "transparent", "transform": "scale(1.1)"},
                _focus={"background_color": "transparent"},
                _active={"background_color": "transparent"},
            ),
            rx.button(
                "🇺🇸",
                on_click=PageState.set_language_en,
                font_size=Size.BIG.value,
                variant="ghost",
                width="auto",
                height="auto",
                min_width="auto",
                padding="0",
                background_color="transparent",
                style={
                    "filter": rx.cond(PageState.lang == "en", "none", "grayscale(100%)"),
                    "position": "relative",
                },
                _hover={"background_color": "transparent", "transform": "scale(1.1)"},
                _focus={"background_color": "transparent"},
                _active={"background_color": "transparent"},
            ),
            gap=Size.LARGE.value
        ),
        position="sticky",
        bg=Color.CONTENT.value,
        padding_x=Size.BIG.value,
        padding_y=Size.DEFAULT.value,
        z_index="999",
        top="0",
        width="100%",
        justify="between",
        align="center",
        style={"box_sizing": "border-box"},
    )
