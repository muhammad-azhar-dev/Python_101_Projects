import PyPDF2



# This function will return all extracted text from a pdf file    
def get_pdf_text(pdf_path):
    """
    Extracts text from the all pages of a PDF file.
    
    :param pdf_path: Path to the PDF file.
    :return: Text from the all pages of the PDF file.
    """
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ''
        for page in range(len(reader.pages)):
            text += reader.pages[page].extract_text()
        return text
    



if __name__ == "__main__":
    pdf_path = 'sample.pdf' # Replace with your PDF file path
    page_text = get_pdf_text(pdf_path) # Extract text from the PDF
    print(page_text)