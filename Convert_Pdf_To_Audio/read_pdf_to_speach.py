import pyttsx3
import PyPDF2

def read_pdf_to_speach(file_path):
    pdf_reeader = PyPDF2.PdfReader(open(file_path, 'rb'))
    text_to_speach = pyttsx3.init()

    # loop through each page of the PDF
    for page in range(len(pdf_reeader.pages)):
        # extract text from the page
        text = pdf_reeader.pages[page].extract_text()
        # clean the text
        legible_text = text.strip().replace('\n', ' ')
        # speak the text
        text_to_speach.say(legible_text)
        text_to_speach.runAndWait()
    text_to_speach.stop()