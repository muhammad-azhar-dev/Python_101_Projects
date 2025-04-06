import PyPDF2

# This function will return the number of pages from a pdf file
def get_page_count(pdf_path):
    """
    Returns the number of pages in a PDF file.
    
    :param pdf_path: Path to the PDF file.
    :return: Number of pages in the PDF file.
    """
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        num_pages = len(reader.pages)
        return num_pages
    
if __name__ == "__main__":
    pdf_path = 'sample.pdf' # Replace with your PDF file path
    page_count = get_page_count(pdf_path) # Get the number of pages
    print(f'The PDF file has {page_count} pages.')