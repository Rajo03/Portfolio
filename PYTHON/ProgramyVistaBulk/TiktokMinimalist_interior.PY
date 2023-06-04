import xlsxwriter
import datetime
import pandas as pd
import os
import random


xlsx_file_path = "C:\\PROGRAMOWANIE\\PYTHON\\GotoweVistaBulk\\tiktokminimalist.xlsx"
date_str = input("Enter date and time in the format '%Y-%m-%d %H:%M': ")



path = "S:\\ARCHIWUM\\MinimalistInterior\\tiktok"

def numbering_name():
    i = 1
    for filename in os.listdir(path):
        old_path = os.path.join(path, filename)
        new_path = os.path.join(path, str(i) + os.path.splitext(filename)[1])
        os.rename(old_path, new_path)
        i += 1


def tworzenie_pliku_excel():
    workbook = xlsxwriter.Workbook(xlsx_file_path)
    worksheet = workbook.add_worksheet()

    date = datetime.datetime.strptime(date_str, "%Y-%m-%d %H:%M")
        

    # Set the column headers
    header_row = ["message", "type", "link", "time"]
    worksheet.write_row(0, 0, header_row)

    # Set up the CSV reader and read the column data

    # Write the column data and other data to the worksheet
    for i in range(50):
        
        # Write the message column data
        hastagi = ["#interiordesign", "#designchoices", "#foryourpage", "#interiortiktok", "#designtok", "#decortips", "#aesthetic", "#minimalistic", "#minimalist"]
        
        message = f"{random.choices(hastagi, k=5)}"
        worksheet.write(i + 1, 0, message)
        
        # Write the type column data
        worksheet.write(i + 1, 1, "video")
        
        # Write the link column data
        link_path = f"http://hosting2275851.online.pro/ARCHIWUM/MinimalistInterior/tiktok/{i+1}.mp4"
        worksheet.write(i + 1, 2, link_path)
        
        # Write the time column data
        
        
        worksheet.write(i + 1, 3, date.strftime("%Y-%m-%d %H:%M"))
        date += datetime.timedelta(hours=24)
        



    # Close the workbook
    workbook.close()




def convert_xlsx_to_csv():
    df = pd.read_excel("C:\\PROGRAMOWANIE\\PYTHON\\GotoweVistaBulk\\tiktokminimalist.xlsx")

    df.to_csv("C:\\PROGRAMOWANIE\\PYTHON\\GotoweVistaBulk\\tiktokminimalist.csv", index=False)

    exit()



tworzenie_pliku_excel()
convert_xlsx_to_csv()