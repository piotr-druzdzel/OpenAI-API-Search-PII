import os
import re
import openai
from openai import OpenAI
from pdfminer.high_level import extract_text


# OpenAI API Key - defaults to getting the key using os.environ.get("OPENAI_API_KEY")
client = OpenAI()
openai.api_key = os.getenv("OPENAI_API_KEY")


text = """
Our sustainability publications on the internet:
🔗 www.henkel.com/sustainability/reports
Henkel; Namthip Muanthongthae via Getty 
Images; Nils Hendrik Müller; Peter Rigaud; 
Henkel app available for iOS and Android:
RgStudio via Getty Images; Westend61 via  
Getty Images; Yagnik Gorasiya via Shutterstock
Translation
RWS Holdings PLC 
Matthew Shoesmith, Revelation, Hilden
Publication date of this report
March 7, 2023 
"""


# def extract_text_from_pdf(pdf_file):
#     """Extracts text from a PDF file.

#     Args:
#         pdf_file: The path to the PDF file.

#     Returns:
#         A string containing the text from the PDF file.
#     """

#     print(f"\nProcessing: {pdf_file}")

#     with open(pdf_file, "rb") as f:
#         text = extract_text(pdf_file)
#         return text


def identify_pii(text, chunk_size=2000):
    """Identifies PII information in a text.

    Args:
        text: The text to be processed.

    Returns:
        A list of strings containing the PII information in the text.
    """

    print(f"\nIdentifying PIIs...")

    

    # Extract the PII information from the OpenAI response
    pii_occurrences = []

    for i in range(0, len(text), chunk_size):

        chunk_text = text[i:i+chunk_size]
        prompt = "Identify PII information in the following text:\n\n" + chunk_text
        # Use the OpenAI API to identify PII information in the document
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo", 
            messages=[
                {"role": "user", "content": "Identify PII information in the following text:\n\n" + text}
                ]
            )
        
        for choice in response['choices'][0]['message']['content']:
            pii_occurrences.extend(re.findall(r"\b[^\s]+\b", choice["text"]))

    return pii_occurrences


# def count_pii(pii_occurrences):
#     """Counts the number of occurrences of each PII type.

#     Args:
#         pii_occurrences: A list of strings containing the PII information.

#     Returns:
#         A dictionary mapping PII types to counts.
#     """

#     print(f"\Counting the PIIs...")

#     pii_counts = {}
#     for pii_occurrence in pii_occurrences:
#         pii_type = re.search(r"\b(\w+)\b", pii_occurrence).group(1)
#         if pii_type not in pii_counts:
#             pii_counts[pii_type] = 1
#         else:
#             pii_counts[pii_type] += 1

#     return pii_counts


if __name__ == '__main__':

    # pdf_file = "Henkel.pdf"

    # # Extract text from the PDF file
    # text = extract_text_from_pdf(pdf_file)

    # Print extracted PDF to console for inspection
    print(text)

    # Identify PII information in the extracted text
    pii_occurrences = identify_pii(text)

    # # Count the number of occurrences of each PII type
    # pii_counts = count_pii(pii_occurrences)

    # # Print the PII occurrences
    # for pii_type, count in pii_counts.items():
    #     print(f"{pii_type}: {count}")

    