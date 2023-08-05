import xlsxwriter
import datetime
import pandas as pd
import os
from PIL import Image

date_str = input("podaj date pierwszego posta '%Y-%m-%d %H:%M': ")
sciezka = input("Podaj scieżke:")
ilosc_postow = int(input("ile postow chcesz zaplanować?"))

#TODO:Pobieranie opisu z innego arkusza



#rename pliki i convert na jpg
path = f"S:\\ARCHIWUM\\Marka osobista\\PL\\{sciezka}"





# Set up the input and output file paths
def tworzenie_pliku_excel():
    xlsx_file_path = "C:\\PROGRAMOWANIE\\PYTHON\\GotoweVistaBulk\\ProfilPL.xlsx"



    date = datetime.datetime.strptime(date_str, "%Y-%m-%d %H:%M")

    # Create a new XLSX file and add a worksheet
    workbook = xlsxwriter.Workbook(xlsx_file_path)
    worksheet = workbook.add_worksheet()

        
        

    # Set the column headers
    header_row = ["message", "type", "link", "time"]
    worksheet.write_row(0, 0, header_row)

    # Set up the CSV reader and read the column data

    # Write the column data and other data to the worksheet
    for i in range(ilosc_postow):
        
        # Write the message column data
        message = f"Clean Eating#{i+1}"
        worksheet.write(i + 1, 0, message)
        
        # Write the type column data
        worksheet.write(i + 1, 1, "video")
        
        # Write the link column data
        link_path = f"http://hosting2275851.online.pro/ARCHIWUM/Marka osobista/ENG/{sciezka}/{i+7}.jpg"
        worksheet.write(i + 1, 2, link_path)
        
        # Write the time column data
        
        
        worksheet.write(i + 1, 3, date.strftime("%Y-%m-%d %H:%M"))
        
        
        date += datetime.timedelta(days = 1)
        
        



    # Close the workbook
    workbook.close()



def convert_xlsx_to_csv():
    df = pd.read_excel("C:\\PROGRAMOWANIE\\PYTHON\\GotoweVistaBulk\\ProfilPL.xlsx")

    df.to_csv("C:\\PROGRAMOWANIE\\PYTHON\\GotoweVistaBulk\\ProfilPL.csv", index=False)

    exit()




tworzenie_pliku_excel()
convert_xlsx_to_csv()

