import PyPDF2
from gtts import gTTS
from PyPDF2 import PdfReader
import IPython

# path of the PDF file
# path = open('out.pdf', 'rb')
with open("C:\\Programowanie\\PYTHON\\AUTOMATYZACJA\\pdftoaudiobook\\pdf\\A Random Walk Down Wall Street_ The Time-Tested Strategy for Successful Investing (Eleventh Edition) ( PDFDrive )-300-370.pdf", "rb") as in_f:
    input1 = PdfReader(in_f)

    numPages = len(input1.pages)
    print ("document has %s pages." % numPages)
    text = ""

    for i in range(50,numPages):
        page = input1.pages[10]
        text += page.extract_text().replace("\n"," ")
    pytts = gTTS(text)
    #pytts = gTTS(text, lang= "pl")
    pytts.save('audioBook2.mp3')