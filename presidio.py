import pprint
from presidio_analyzer import AnalyzerEngine
from pdfminer.high_level import extract_text



def extract_text_from_pdf(pdf_file):
    """Extracts text from a PDF file.

    Args:
        pdf_file: The path to the PDF file.

    Returns:
        A string containing the text from the PDF file.
    """

    print(f"\nProcessing: {pdf_file}")

    with open(pdf_file, "rb") as f:
        text = extract_text(pdf_file)
        return text

text = extract_text_from_pdf('Henkel.pdf')
print(text)


print(f"\nIdentifying PII from text...")
analyzer = AnalyzerEngine()
analyzer_results = analyzer.analyze(text=text, language="en")


def create_pii_dict(analyzer_results, text):

    # Create a dictionary with PII type as key and the identified text and its score as values
    pii_dict = {}

    for pii in analyzer_results:

        if pii.score > 0.3:

            pii_type = pii.entity_type
            pii_value = text[pii.start:pii.end]
            pii_score = pii.score
            
            if pii_type not in pii_dict:
                pii_dict[pii_type] = []

            pii_dict[pii_type].append({"text": pii_value, "score": pii_score})

    return pii_dict
    

dict1 = create_pii_dict(analyzer_results, text)

# Print the grouped PIIs
for key, value in dict1.items():
    print()
    print(key, value)

print()
# Count the number of occurrences for each PII type
for key, values in dict1.items():
    print(key, len(values))


# Pretty print the list of dictionaries
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(dict1)


print(f"\nSuccessfully completed.\n")