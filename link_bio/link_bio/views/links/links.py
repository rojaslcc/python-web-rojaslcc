import reflex as rx
import link_bio.constants as const
from link_bio.components.link_button import link_button
from link_bio.components.title import title
from link_bio.styles.styles import Size
from link_bio.state.page_state import PageState
from link_bio.i18n import Trans


def links() -> rx.Component:
    return rx.vstack(
        title(PageState.i18n[Trans.TITLE_NEW]),
        link_button(
            PageState.i18n[Trans.LINK_ALTOS_WEB],
            PageState.i18n[Trans.LINK_ALTOS_BODY],
            "icons/web.svg",
            const.ALTOSINTERACTIVEWEB_URL
        ),
        title(PageState.i18n[Trans.TITLE_COMMUNITY]),
        link_button(
            PageState.i18n[Trans.LINK_ROJAS_FB],
            PageState.i18n[Trans.LINK_ROJAS_BODY],
            "icons/facebook.svg",
            const.FACEBOOK_URL
        ),
        link_button(
            PageState.i18n[Trans.LINK_BRUDDAS],
            PageState.i18n[Trans.LINK_BRUDDAS_BODY],
            "icons/facebook.svg",
            const.FACEBOOK_BTS_URL
        ),
        link_button(
            "Altos Interactive",
            "Co-fundador de startup para el desarrollo de software.",
            "icons/facebook.svg",
            const.FACEBOOK_ALTOS_URL
        ),
        link_button(
            "Twitch",
            PageState.i18n[Trans.LINK_TWITCH_BODY],
            "icons/twitch.svg",
            const.TWITCH_URL
        ),
        link_button(
            PageState.i18n[Trans.LINK_YT_PERSONAL],
            PageState.i18n[Trans.LINK_YT_PERSONAL_BODY],
            "icons/youtube.svg",
            const.YOUTUBE_SECONDARY_URL
        ),
        link_button(
            PageState.i18n[Trans.LINK_YT_TUTORIAL],
            PageState.i18n[Trans.LINK_YT_TUTORIAL_BODY],
            "icons/youtube.svg",
            const.YOUTUBE_URL
        ),
        link_button(
            "YouTube ⓘ canal Bruddas Tech&Solutions",
            "Hogar del pódcast BTS: Tecnología Hoy y más contenido sobre tecnología.",
            "icons/youtube.svg",
            const.YOUTUBE_BTS_URL
        ),

        title(PageState.i18n[Trans.TITLE_RESOURCES]),
        link_button(
            "Blog",
            PageState.i18n[Trans.LINK_BLOG_BODY],
            "icons/wordpress.svg",
            const.WORDPRESS_URL
        ),
        link_button(
            "Proyecto: App Android e-UANL Campus Digital",
            "Conoce la app nativa que desarrollé con Kotlin en sus primeras versiones para mi alma mater la U.A.N.L.",
            "icons/android.svg",
            const.EUANL_URL
        ),
        link_button(
            "Proyecto: App Web CLIPSI UANL",
            "Conoce la app web que desarrollé con ASP.NET Core en sus primeras versiones para la Facultad de Psicología mi alma mater la U.A.N.L.",
            "icons/microsoft.svg",
            const.CLIPSI_URL
        ),
        link_button(
            "In Development: POKÉDEX",
            "Un proyecto que hice en VueJS para el bootcamp LAUNCHX de Microsoft y que buscaré mejorar.",
            "icons/vuejs.svg",
            const.MYPOKEDEX_URL
        ),
        link_button(
            "Ejercicio: App Web MiPasteleria",
            "Un proyecto que hice en ASP.NET Core para el bootcamp LAUNCHX de Microsoft se buscaba practicar el HTML y CSS.",
            "icons/microsoft.svg",
            const.MIPASTELERIA_URL
        ),

        title(PageState.i18n[Trans.TITLE_CONTACT]),
        link_button(
            "e-Mail",
            const.EMAIL,
            "icons/email.svg",
            f"mailto:{const.EMAIL}"
        ),
        width="100%",
        gap=Size.DEFAULT.value,
    )
