import pyttsx3
from PyPDF2 import PdfReader

pdf_file = 'input.pdf'
output_file = 'output.mp3'

speaker = pyttsx3.init()

speaker.save_to_file('', output_file)


pdfreader = PdfReader("C:\\Programowanie\\PYTHON\\AUTOMATYZACJA\\pdftoaudiobook\\pdf\\10Xrule po polsku.pdf")


# ilosc_stron = (len(pdfreader.pages))

page = pdfreader.pages[0]
speaker.say(page)
speaker.runAndWait()

for page_num in range(page):
    page = pdfreader.pages(len(pdfreader.pages))
    text = page.extractText()

    speaker.save_to_file(text, output_file)
speaker.runAndWait()



# for liczba_strony in range(len(pdfreader.pages)):
#     text = pdfreader.pages(liczba_strony).extractText()
#     speaker.say(text)
#     speaker.runAndWait()
# speaker.stop()