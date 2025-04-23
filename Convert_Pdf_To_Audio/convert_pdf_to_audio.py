import pyttsx3
import PyPDF2

def save_pdf_to_audio(file_path, output_file):
    pdf_reader = PyPDF2.PdfReader(open(file_path, 'rb'))
    text_to_speach = pyttsx3.init()
    full_text = ''

    # loop through each page of the PDF
    for page in range(len(pdf_reader.pages)):
        # extract text from the page
        text = pdf_reader.pages[page].extract_text()
        # clean the text
        legible_text = text.strip().replace('\n', ' ')
        full_text += legible_text
        
    # convert the full text to audio and save it to a file
    text_to_speach.save_to_file(full_text, output_file)
    text_to_speach.runAndWait()
    text_to_speach.stop()
    print(f"{file_path} Saved to {output_file}")