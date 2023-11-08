from pdfminer.high_level import extract_text


def extract_text_from_pdf(pdf_file):
    """Extracts text from a PDF file.

    Args:
        pdf_file: The path to the PDF file.

    Returns:
        A string containing the text from the PDF file.
    """

    with open(pdf_file, "rb") as f:
        text = extract_text(pdf_file)
        return text
    

if __name__ == "__main__":
    
    pdf_file = "Henkel.pdf"

    # Extract text from the PDF file
    text = extract_text_from_pdf(pdf_file)

    print(text)