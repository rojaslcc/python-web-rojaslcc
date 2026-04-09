import reflex as rx
import link_bio.constants as const
from link_bio.styles.styles import Size
from link_bio.components.title import title
from link_bio.components.link_sponsor import link_sponsor
from link_bio.state.page_state import PageState
from link_bio.i18n import Trans


def sponsors() -> rx.Component:
    return rx.vstack(
        title(PageState.i18n[Trans.TITLE_MY_TECH_STACK]),
        rx.flex(
            link_sponsor(
                "/stack/android.svg",
                const.SIN_URL,
                "Logotipo de Android"
            ),
            link_sponsor(
                "/stack/java.svg",
                const.SIN_URL,
                "Logotipo de Java"
            ),
            link_sponsor(
                "/stack/kotlin.svg",
                const.SIN_URL,
                "Logotipo de Kotlin"
            ),
            link_sponsor(
                "/stack/csharp.svg",
                const.SIN_URL,
                "Logotipo de C#"
            ),
            link_sponsor(
                "/stack/python.svg",
                const.SIN_URL,
                "Logotipo de Python"
            ),
            link_sponsor(
                "/stack/sqlserver.svg",
                const.SIN_URL,
                "Logotipo de SQL Server"
            ),
            wrap="wrap",
            gap=Size.DEFAULT.value,
        ),
        width="100%",
        align_items="start",
        gap=Size.DEFAULT.value
    )
