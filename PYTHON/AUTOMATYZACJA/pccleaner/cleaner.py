import os
import time

def remove_old_files(directory, days):
    current_time = time.time()
    expiry_time = days * 24 * 60 * 60  # 90 dni w sekundach

    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            if os.path.isfile(file_path):
                file_age = current_time - os.path.getmtime(file_path)
                if file_age > expiry_time:
                    os.remove(file_path)
                    print("Usunięto plik:", file_path)

directory = "ścieżka/do/katalogu"  # Podaj ścieżkę do katalogu, w którym chcesz usunąć pliki
days = 90  # Liczba dni, starsze pliki które mają zostać usunięte

remove_old_files(directory, days)
