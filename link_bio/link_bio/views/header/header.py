import reflex as rx
import datetime
import link_bio.constants as const
from link_bio.styles.styles import Size
from link_bio.styles.colors import Color, TextColor
from link_bio.components.link_icon import link_icon
from link_bio.components.info_text import info_text
import requests
from bs4 import BeautifulSoup


def get_instagram_followers(username: str) -> str:
    try:
        url = f"https://www.instagram.com/{username}/"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
            "Accept-Language": "es-ES,es;q=0.9",
            "Sec-Fetch-Dest": "document",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Site": "none",
            "Sec-Fetch-User": "?1",
            "Upgrade-Insecure-Requests": "1",
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')

        meta_tag = soup.find('meta', property="og:description")

        if meta_tag and 'content' in meta_tag.attrs:
            content = meta_tag.attrs['content']
            followers = content.split(' ')[0]  # Extrae el número de seguidores
            return followers

    except Exception as e:
        print(f"Error al obtener seguidores de Instagram: {e}")

    return "N/A"


def experience() -> int:
    return datetime.date.today().year - 2014


def header() -> rx.Component:
    instagram_followers = get_instagram_followers("rojaslcc")

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
                f"{instagram_followers}", "seguidores en instagram"
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
