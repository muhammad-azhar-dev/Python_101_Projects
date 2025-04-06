import PyPDF2

"""
This function will rotate the pages of a PDF file by a specified angle
and save the rotated PDF to a new file.
"""
def rotate_pdf(input_pdf_path, output_pdf_path, rotation_angle):
    """
    Rotates the pages of a PDF file by a specified angle.
    
    :param input_pdf_path: Path to the input PDF file.
    :param output_pdf_path: Path to save the rotated PDF file.
    :param rotation_angle: Angle to rotate the pages (90, 180, or 270 degrees).
    """
    with open(input_pdf_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        # Create a PDF writer object
        pdf_writer = PyPDF2.PdfWriter() 
        
        # Rotate each page by the specified angle
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            page.rotate(rotation_angle)
            pdf_writer.add_page(page) 

        # Save the rotated PDF to a new file
        with open(output_pdf_path, 'wb') as output_file:
            pdf_writer.write(output_file)
            print(f"Successfully Rotated PDF saved as {output_pdf_path}")

if __name__ == "__main__":
    pdf_path = 'sample.pdf' # Replace with your PDF file path

    # Rotate the PDF by 270 degrees and save it as 'rotated_sample.pdf'
    rotate_pdf(pdf_path, 'rotated_sample.pdf', 270) 