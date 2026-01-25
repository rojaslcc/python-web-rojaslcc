import reflex as rx

config = rx.Config(
    app_name="link_bio",
    cors_allowed_origins=["*"],
    disable_plugins=["reflex.plugins.sitemap.SitemapPlugin"],
    strict_mode=False,
    api_url="https://rojaslcc.onrender.com"
)
