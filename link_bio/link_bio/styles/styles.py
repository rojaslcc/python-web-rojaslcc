import reflex as rx
from enum import Enum
from .colors import Color, TextColor
from .fonts import Font, FontWeight

# Constants
MAX_WIDTH = "560px"


# Sizes


class Size(Enum):
    ZERO = "0px !important"
    SMALL = "0.5em"
    SMEDIUM = "0.65em"
    MEDIUM = "0.8em"
    DEFAULT = "1em"
    LARGE = "1.5em"
    VERY_LARGE = "1.8em"
    BIG = "2em"
    VERY_BIG = "4em"
    HUGE = "8em"

# Styles


BASE_STYLE = {
    "body": {
        "margin": "0",
        "padding": "0",
    },
    # Selecciona cualquier enlace que contenga reflex.dev en su URL
    "a[href*='reflex.dev']": {
        "display": "none !important",
        "visibility": "hidden !important",
        "opacity": "0 !important",
        "pointer-events": "none !important",
    },
    # Selector adicional para el contenedor flotante típico de la 0.8.x
    ".rt-Box[style*='position: fixed']": {
            "display": "none !important" if "Reflex" in str(rx.fragment()) else "block", 
    },
    "font_family": Font.DEFAULT.value,
    "font_weight": FontWeight.LIGHT.value,
    "background_color": Color.BACKGROUND.value,
    rx.heading: {
        "color": TextColor.HEADER.value,
        "font_family": Font.TITLE.value,
        "font_weight": FontWeight.MEDIUM.value
    },
    rx.button: {
        "width": "100%",
        "height": "100%",
        "padding": Size.SMALL.value,
        "border_radius": Size.DEFAULT.value,
        "color": TextColor.HEADER.value,
        "background_color": Color.CONTENT.value,
        "white_space": "normal",
        "text_align": "start",
        "_hover": {
            "background_color": Color.SECONDARY.value
        }
    },
    rx.link: {
        "text_decoration": "none",
        "_hover": {}
    }
}

navbar_title_style = dict(
    font_family=Font.LOGO.value,
    font_weight=FontWeight.MEDIUM.value,
    font_size=Size.LARGE.value
)

title_style = dict(
    width="100%",
    padding_top=Size.DEFAULT.value,
    font_size=Size.LARGE.value
)

button_title_style = dict(
    font_family=Font.TITLE.value,
    font_weight=FontWeight.MEDIUM.value,
    font_size=Size.DEFAULT.value,
    color=TextColor.HEADER.value
)

button_body_style = dict(
    font_weight=FontWeight.LIGHT.value,
    font_size=Size.MEDIUM.value,
    color=TextColor.BODY.value
)
