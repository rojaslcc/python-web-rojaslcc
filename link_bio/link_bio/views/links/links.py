import reflex as rx
import link_bio.constants as const
from link_bio.components.link_button import link_button
from link_bio.components.title import title
from link_bio.styles.styles import Size


def links() -> rx.Component:
    return rx.vstack(
        title("Lo nuevo"),
        link_button(
            "Sitio web de Altos Interactive",
            "Desarrollo de software y soluciones digitales.",
            "icons/web.svg",
            const.ALTOSINTERACTIVEWEB_URL
        ),
        title("Comunidad"),
        link_button(
            "RojasLCC Tutoriales y más",
            "Mi pagina de facebook principal.",
            "icons/facebook.svg",
            const.FACEBOOK_URL
        ),
        link_button(
            "Bruddas Tech&Solutions",
            "Proyecto de creacion de contenido digital sobre software y tecnología.",
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
            "Pronto transmisiones sobre temas de programación/tecnología.",
            "icons/twitch.svg",
            const.TWITCH_URL
        ),
        link_button(
            "YouTube ⓘ canal personal",
            "Cuenta personal de contenido",
            "icons/youtube.svg",
            const.YOUTUBE_SECONDARY_URL
        ),
        link_button(
            "YouTube ⓘ canal tutoriales",
            "Tutoriales sobre programación y vídeos sobre tecnología.",
            "icons/youtube.svg",
            const.YOUTUBE_URL
        ),
        link_button(
            "YouTube ⓘ canal Bruddas Tech&Solutions",
            "Hogar del pódcast BTS: Tecnología Hoy y más contenido sobre tecnología.",
            "icons/youtube.svg",
            const.YOUTUBE_BTS_URL
        ),

        title("Recursos y más"),
        link_button(
            "Blog",
            "Blog personal donde publico de vez en cuando.",
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

        title("Contacto"),
        link_button(
            "e-Mail",
            const.EMAIL,
            "icons/email.svg",
            f"mailto:{const.EMAIL}"
        ),
        width="100%",
        gap=Size.DEFAULT.value,
    )
