set -e
if [ ! -d "venv" ]; then
    python3 -m venv venv
fi
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

# Ejecuta el script para actualizar los seguidores
echo "--- Ejecutando script para actualizar seguidores ---"
python update_followers.py
echo "--- Script de seguidores finalizado ---"

rm -rf .web
rm -f frontend.zip
reflex export --frontend-only
rm -rf public
unzip frontend.zip -d public
rm -f frontend.zip
deactivate