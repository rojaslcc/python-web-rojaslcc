import reflex as rx
import datetime
import json
import link_bio.constants as const
from link_bio.styles.styles import Size
from link_bio.styles.colors import Color, TextColor
from link_bio.components.link_icon import link_icon
from link_bio.components.info_text import info_text


def get_cached_data() -> dict:
    """Lee los datos cacheados desde el archivo JSON."""
    try:
        # `reflex` se ejecuta desde el directorio raíz del proyecto (`link_bio/`)
        with open("data.json", "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {"instagram_followers": "N/A"}


def experience() -> int:
    """Calculates years of experience."""
    return datetime.date.today().year - 2014


def header() -> rx.Component:
    """The header component for the page."""
    cached_data = get_cached_data()
    instagram_followers = cached_data.get("instagram_followers", "N/A")

    return rx.vstack(
        rx.hstack(
            rx.image(
                src="avatar.jpg",
                alt="H.R. Rangel",
                width="6.5em",
                height="6.5em",
                border_radius="50%",
                padding="2px",
                border_width="4px",
                border_style="solid",
                border_color=Color.PRIMARY.value
            ),
            rx.vstack(
                rx.heading(
                    "H.R. Rangel",
                    size="7"
                ),
                rx.text(
                    "@rojaslcc",
                    margin_top=Size.ZERO.value,
                    color=Color.PRIMARY.value
                ),
                rx.hstack(
                    link_icon(
                        "icons/github.svg",
                        const.GITHUB_URL,
                        "GitHub"
                    ),
                    link_icon(
                        "icons/x.svg",
                        const.TWITTER_X_URL,
                        "Twitter/X"
                    ),
                    link_icon(
                        "icons/instagram.svg",
                        const.INSTAGRAM_URL,
                        "Instagram"
                    ),
                    link_icon(
                        "icons/tiktok.svg",
                        const.TIKTOK_URL,
                        "TikTok"
                    ),
                    link_icon(
                        "icons/apple_music.svg",
                        const.APPLEMUSIC_URL,
                        "Apple Music"
                    ),
                    link_icon(
                        "icons/linkedin.svg",
                        const.LINKEDIN_URL,
                        "LinkedIn"
                    ),
                    gap=Size.LARGE.value
                ),
                align_items="start"
            ),
            gap=Size.DEFAULT.value
        ),
        rx.flex(
            info_text(
                f"{experience()}+",
                "años de experiencia"
            ),
            rx.spacer(),
            info_text(
                "2+", "aplicaciones públicas creadas"
            ),
            rx.spacer(),
            info_text(
                instagram_followers, "seguidores en instagram"
            ),
            width="100%"
        ),
        rx.text(
            f"""
            Soy licenciado en ciencias computacionales y actualmente trabajo para Banregio como analista programador Sr. 
            Además, creo contenido sobre programación y tecnología en general en redes sociales. 
            Aquí podrás encontrar todos mis enlaces de interés ¡Bienvenid@!
            """,
            font_size=Size.DEFAULT.value,
            color=TextColor.BODY.value,
            text_align="justify"
        ),
        gap=Size.BIG.value,
        align_items="start"
    )
