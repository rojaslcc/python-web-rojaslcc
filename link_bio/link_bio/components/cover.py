import reflex as rx
from link_bio.styles.styles import Size
from link_bio.styles.colors import Color


def cover(image: str) -> rx.Component:
    return rx.box(
        rx.image(
            src=image,
            width="100%",
            height="auto",
            aspect_ratio="820 / 312",
            object_fit="cover",
            alt="Imagen de portada"
        ),
        rx.box(
            position="absolute",
            width="100%",
            height="100%",
            bottom="0",
            background=f"linear-gradient(transparent 10%, {Color.BACKGROUND.value})",
        ),
        width="100%",
        border_radius=Size.DEFAULT.value,
        overflow="hidden",
        position="relative"
    )