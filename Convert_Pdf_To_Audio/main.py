import pyttsx3
import PyPDF2
from read_pdf_to_speach import read_pdf_to_speach
from convert_pdf_to_audio import save_pdf_to_audio


if __name__ == "__main__":
    # specify the path to your PDF file
    file_path = 'sample.pdf'

    # read the PDF file and convert it to speech
    # read_pdf_to_speach(file_path)

    # convert the PDF to audio and save it as an MP3 file
    # save_pdf_to_audio(file_path, "output.mp3")