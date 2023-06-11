import os
import pandas as pd
from tkinter import Tk, Button, Label, filedialog

def convert_file():
    file_path = filedialog.askopenfilename(filetypes=[('Excel Files', '*.xlsx')])
    if file_path:
        folder_path = os.path.dirname(file_path)
        filename = os.path.basename(file_path)
        df = pd.read_excel(file_path)
        new_filename = os.path.splitext(filename)[0] + '.csv'
        new_file_path = os.path.join(folder_path, new_filename)
        df.to_csv(new_file_path, index=False)
        os.remove(file_path)
        result_label.config(text="Konwersja zakończona!")
    else:
        result_label.config(text="Nie wybrano pliku.")

# Tworzenie głównego okna
root = Tk()
root.title("Konwersja pliku XLSX na CSV")
root.geometry("400x200")

# Etykieta z instrukcjami
instructions_label = Label(root, text="Wybierz plik XLSX do konwersji:")
instructions_label.pack(pady=20)

# Przycisk do wywołania okna wyboru pliku
select_button = Button(root, text="Wybierz plik", command=convert_file)
select_button.pack()

# Etykieta z rezultatem konwersji
result_label = Label(root, text="")
result_label.pack(pady=10)

# Uruchomienie głównej pętli aplikacji
root.mainloop()