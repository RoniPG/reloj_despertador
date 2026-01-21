import random
import time
import webbrowser

from datetime import datetime 
from pathlib import Path


alarm_time = input("Introduce la hora de la alarma (HH:MM) ")

ruta_links = Path("data/youtube_links.txt")
links = ruta_links.read_text().splitlines()

print(f"Alarma configurada para las {alarm_time}")

while True:
    now = datetime.now().strftime("%H:%M")
    if now == alarm_time:
        url = random.choice(links)
        webbrowser.open(url)
        print("¡Despertador activado! Abriendo enlace...")
        break
    time.sleep(30)




























