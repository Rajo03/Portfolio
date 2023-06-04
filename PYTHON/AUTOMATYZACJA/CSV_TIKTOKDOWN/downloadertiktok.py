import csv
import requests
import os

# nazwa pliku CSV z linkami do filmów
csv_file = "C:\\PROGRAMOWANIE\\PYTHON\\AUTOMATYZACJA\\CSV_TIKTOKDOWN\\links.csv"

# folder, w którym zostaną zapisane pobrane filmy
save_folder = "C:\\PROGRAMOWANIE\\PYTHON\\AUTOMATYZACJA\\CSV_TIKTOKDOWN\\export"

# utwórz folder, jeśli nie istnieje
if not os.path.exists(save_folder):
    os.makedirs(save_folder)

# otwórz plik CSV i przeczytaj linki do filmów
with open(csv_file, "r") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        video_url = row[0]
        video_id = video_url.split("/")[-1]
        # wysyłanie linku do witryny tiktokdownloader
        response = requests.get(f"https://tiktokdownloader.com/download?url={video_url}")
        open(f"{save_folder}/{video_id}.mp4", "wb").write(response.content)

print("Pobieranie zakończone.")
