import os
import sys
import datetime



sciezka = input("podaj lokalizacje: ")
if not os.path.exists(sciezka):
    print("Wprowadz dobra lokalizacje: ")
    sys.exit(1)
if os.path.isfile(sciezka):
    print("podaj sciezke pliku: ")
    sys.exit(2)
data = int(input("podaj date starsze niż (w dniach): "))

dzisiaj = datetime.datetime.now()

for each_file in os.listdir(sciezka):
    each_file_path = os.path.join(sciezka,each_file)
    if os.path.isfile(each_file_path):
        file_create_date = datetime.datetime.fromtimestamp(os.path.getctime(each_file_path))
        #print(dir(dzisiaj-file_create_date))
        dif_days = (dzisiaj-file_create_date).days
        if dif_days > data:
          print(each_file_path,(dzisiaj-file_create_date).days)
          os.remove(each_file_path)
          print("Usuniete pliki starsze niż:",data,each_file_path)