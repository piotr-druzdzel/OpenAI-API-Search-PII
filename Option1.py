import PyPDF2
from openai import OpenAI

# OpenAI API key
client = OpenAI()

# Function to divide text into batches smaller than 16000 tokens
def split_text_into_batches(text):
    MAX_TOKENS = 16000
    pages = text.split('\n\n')  # Assuming pages are separated by double newline characters
    batches = []
    current_batch = ""
    for page in pages:
        if len(current_batch) + len(page) < MAX_TOKENS:
            current_batch += page + '\n\n'
        else:
            batches.append(current_batch)
            current_batch = page + '\n\n'
    if current_batch:
        batches.append(current_batch)
    return batches

# Function to identify PII using OpenAI API
def identify_pii(text_batch):
    prompt = "Identify, group and count PII information for each group in the following text:\n" + text_batch
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a legal assistant, skilled in counting PII occurrences."},
            {"role": "user", "content": prompt}
            ]
)
    return response.choices[0].message.content

# Function to process PDF and identify PII
def process_pdf(file_path):
    with open(file_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfFileReader(file)
        extracted_text = ""
        for page_num in range(pdf_reader.numPages):
            page = pdf_reader.getPage(page_num)
            extracted_text += page.extractText()
        batches = split_text_into_batches(extracted_text)
        identified_pii = []
        for batch in batches:
            identified_pii.append(identify_pii(batch))
        return identified_pii

# Main function
def main():
    pdf_file_path = 'Henkel.pdf'
    identified_pii = process_pdf(pdf_file_path)
    for idx, group in enumerate(identified_pii, start=1):
        pii_list = group.split('\n')
        pii_type = pii_list[0]
        pii_instances = pii_list[1:-1]
        count = len(pii_instances)
        print(f"PII type ({idx}): {pii_type}")
        print(f"List of identified PII instances: {pii_instances}")
        print(f"Count of all occurrences within a group: {count}")
        print("===")

if __name__ == "__main__":
    main()
