import time
import requests

URL = "https://discord-gg.onrender.com"  # Hier deine Render-URL eintragen

while True:
    try:
        res = requests.get(URL)
        print(f"Ping {URL}: {res.status_code}")
    except Exception as e:
        print("Fehler beim Pingen:", e)
    time.sleep(300)  # alle 5 Minuten
