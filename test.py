from openai import OpenAI
from pdfminer.high_level import extract_text

# OpenAI API Key - defaults to getting the key using os.environ.get("OPENAI_API_KEY")
client = OpenAI()

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


# Define the chunk size
chunk_size = len(text) // 100
# Initialize an empty list to store the chunks
chunks_list = []
# Divide the string into 30 pieces and save each chunk to the list
for i in range(0, len(text), chunk_size):
    chunk = text[i:i+chunk_size]
    chunks_list.append(chunk)


responses = []
for nr, text in enumerate(chunks_list):

    print(f"\nProcessing chunk: {nr}")

    prompt = f"""
    Identify, group and count the PII occurrences for each group in the following text:
    {text}

    Please report the results in the following format:
    
    Identified PII type:
    
        List of occurrences:

            Total sum of all found instances:

    """

    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a legal assistant, skilled in counting PII occurrences."},
        {"role": "user", "content": prompt}
    ]
    )

    chat_response = completion.choices[0].message.content
    responses.append(chat_response)
    print(chat_response)
    print()