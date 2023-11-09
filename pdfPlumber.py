import os
import pdfplumber
import openai

openai.api_key = os.environ.get("OPENAI_API_KEY")

# Set the maximum number of OpenAI API tokens per batch
max_tokens_per_batch = 16000

def extract_text_and_split_into_batches(pdf_filename):
    # Load the PDF file using pdfplumber
    with pdfplumber.open(pdf_filename) as pdf:
        # Initialize an empty list to store the text batches
        text_batches = []

        # Initialize a variable to track the current token count
        current_token_count = 0

        # Extract text from each page and add it to the current batch
        for page in pdf.pages:
            page_text = page.extract_text()
            token_count = len(openai.ChatCompletion.tokenize(page_text))

            # Check if adding the current page's text would exceed the maximum token count
            if current_token_count + token_count <= max_tokens_per_batch:
                # Add the page's text to the current batch
                text_batches[-1].append(page_text)
                current_token_count += token_count
            else:
                # Start a new batch if the current batch is full
                text_batches.append([page_text])
                current_token_count = token_count

    return text_batches

# Example usage
text_batches = extract_text_and_split_into_batches("Henkel.pdf")
