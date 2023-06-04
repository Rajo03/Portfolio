import os
import pandas as pd
from tkinter import Tk, Button, Label, filedialog

def convert_files():
    folder_path = filedialog.askdirectory()  # Wybór folderu
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        file_ext = os.path.splitext(filename)[1].lower()
        if file_ext == '.xlsx':
            df = pd.read_excel(file_path)
            new_filename = os.path.splitext(filename)[0] + '.csv'
            new_file_path = os.path.join(folder_path, new_filename)
            df.to_csv(new_file_path, index=False)
            os.remove(file_path)
    result_label.config(text="Konwersja zakończona!")

# Tworzenie głównego okna
root = Tk()
root.title("Konwersja plików XLSX na CSV")
root.geometry("400x200")

# Etykieta z instrukcjami
instructions_label = Label(root, text="Wybierz folder zawierający pliki XLSX do konwersji:")
instructions_label.pack(pady=20)

# Przycisk do wywołania okna wyboru folderu
select_button = Button(root, text="Wybierz folder", command=convert_files)
select_button.pack()

# Etykieta z rezultatem konwersji
result_label = Label(root, text="")
result_label.pack(pady=10)

# Uruchomienie głównej pętli aplikacji
root.mainloop()