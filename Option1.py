import PyPDF2
import openai

# OpenAI API key
openai.api_key = 'your_openai_api_key'

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
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=text_batch,
        max_tokens=100,
        temperature=0,
        top_p=1,
        n=1
    )
    return response.choices[0].text.strip()

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
    pdf_file_path = 'path/to/your/pdf/file.pdf'
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
