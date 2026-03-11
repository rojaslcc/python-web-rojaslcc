import requests
from bs4 import BeautifulSoup
import json

# Este script asume que se ejecuta desde el directorio `link_bio`
DATA_FILE = "data.json"

def get_instagram_followers(username: str) -> str:
    """Intenta obtener los seguidores de Instagram mediante scraping."""
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

if __name__ == "__main__":
    print("Actualizando contador de seguidores de Instagram...")
    
    try:
        with open(DATA_FILE, "r") as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        data = {"instagram_followers": "N/A"}

    new_followers = get_instagram_followers("rojaslcc")
    
    if new_followers:
        print(f"Seguidores obtenidos: {new_followers}")
        data["instagram_followers"] = new_followers
        with open(DATA_FILE, "w") as f:
            json.dump(data, f, indent=4)
        print(f"Datos guardados en '{DATA_FILE}'")
    else:
        print("No se pudo obtener los seguidores. El archivo no fue modificado.")