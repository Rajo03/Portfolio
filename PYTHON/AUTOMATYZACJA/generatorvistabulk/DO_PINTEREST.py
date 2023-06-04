import xlsxwriter
import csv
import datetime
import pandas as pd
import os
import time
from PIL import Image

date_str = input("podaj date pierwszego pina 'DD.MM.YYYY HH:MM': ")
sciezka = input("Podaj scieżke(kategorie pina):")






#rename pliki i convert na jpg
path = f"S:\\ARCHIWUM\\travelpinterest\\{sciezka}"

i = 1
for filename in os.listdir(path):
    old_path = os.path.join(path, filename)
    new_path = os.path.join(path, str(i) + os.path.splitext(filename)[1])
    os.rename(old_path, new_path)
    i += 1




# Set up the input and output file paths

xlsx_file_path = "C:\\PROGRAMOWANIE\\PYTHON\\GotoweVistaBulk\\ExplorerEye_Pinterest.xlsx"



date = datetime.datetime.strptime(date_str, "%d.%m.%Y %H:%M")

# Create a new XLSX file and add a worksheet
workbook = xlsxwriter.Workbook(xlsx_file_path)
worksheet = workbook.add_worksheet()

    
    

# Set the column headers
header_row = ["message", "type", "link", "time"]
worksheet.write_row(0, 0, header_row)

# Set up the CSV reader and read the column data

# Write the column data and other data to the worksheet
for i in range(50):
    
    # Write the message column data
    message = f"{sciezka}#{i+1}"
    worksheet.write(i + 1, 0, message)
    
    # Write the type column data
    worksheet.write(i + 1, 1, "image")
    
    # Write the link column data
    link_path = f"http://hosting2275851.online.pro/zdjecia/pinterest/travel/{i+1}.jpg"
    worksheet.write(i + 1, 2, link_path)
    
    # Write the time column data
    
    
    worksheet.write(i + 1, 3, date.strftime("%d.%m.%Y %H:%M"))
    
    if (i % 3 == 2):
        date -= datetime.timedelta(hours = 6)
        date += datetime.timedelta(days = 1)
    else:
        date += datetime.timedelta(hours = 3)



# Close the workbook
workbook.close()







# read the xlsx file
df = pd.read_excel("C:\\PROGRAMOWANIE\\PYTHON\\GotoweVistaBulk\\ExplorerEye_Pinterest.xlsx")

# save as csv file
df.to_csv("C:\\PROGRAMOWANIE\\PYTHON\\GotoweVistaBulk\\ExplorerEye_Pinterest.csv", index=False)

# end the program
exit()

    
