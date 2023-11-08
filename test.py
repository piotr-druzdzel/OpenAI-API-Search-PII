import re
from openai import OpenAI

# OpenAI API Key - defaults to getting the key using os.environ.get("OPENAI_API_KEY")
client = OpenAI()

text = """
Our sustainability publications on the internet:
🔗 www.henkel.com/sustainability/reports
Henkel; Namthip Muanthongthae via Getty 
Images; Nils Hendrik Müller; Peter Rigaud; 
Henkel app available for iOS and Android:
RgStudio via Getty Images; Westend61 via  
Getty Images; Yagnik Gorasiya via Shutterstock
Translation +49 605 740 496
Hmm misiuniek@gmail.com
Best ice cream: Zielona 15, 26-620 Warszawa
RWS Holdings PLC 
Matthew Shoesmith, Revelation, Hilden
Publication date of this report
March 7, 2023 
"""

# replies=[]
# chunk_size=20
# chunks = text.splitlines()

# for chunk in chunks:
#     if len(chunk.split()) > chunk_size:
#         subchunks = re.split(r"\s+", chunk)
#         i = 0
#         while i < len(subchunks):
#             current_chunk = " ".join(subchunks[i:i+20])
#             chunks.append(current_chunk)
#             i += 20

# print(chunks)

# for number, chunk in enumerate(chunks):

#     print(f"\nProcessing chunk text: {number, chunk}")

#     prompt = "Identify, group and count PII information for each group in the following text:\n" + chunk
#     completion = client.chat.completions.create(
#     model="gpt-3.5-turbo",
#     messages=[
#         {"role": "system", "content": "You are a legal assistant, skilled in counting PII occurrences."},
#         {"role": "user", "content": prompt}
#     ]
#     )

#     chat_response = completion.choices[0].message.content

#     replies.append(chat_response)

replies=['To identify and count PII information in the following text, we first need the text itself. Please provide the text that needs to be analyzed.', 'As an AI language model, I can assist you in identifying and counting personally identifiable information (PII) in the given text. However, please note that without the actual text, it is not possible for me to analyze and accurately identify PII information. If you provide the actual text, I will be able to assist you further in identifying and counting PII occurrences.', 'As an AI language model, I can assist you in identifying and categorizing Personally Identifiable Information (PII) in the given text. However, since the text you provided is a website URL, it does not contain any PII information itself. PII generally refers to personal data such as names, addresses, phone numbers, social security numbers, and other identifiable details. If you provide me with a different text or specific information, I can help you identify and count PII occurrences within it.', "Based on the given text, there is no specific PII (Personally Identifiable Information) information present. The text only mentions a company name (Henkel) and a person's name (Namthip Muanthipthongthae). However, without additional details or specific PII elements such as addresses, phone numbers, social security numbers, etc., it is not possible to identify and count PII occurrences.", 'Based on the provided text, the PII information can be identified, grouped, and counted as follows:\n\nGroup 1:\n- Name: Nils Hendrik Müller (1 occurrence)\n\nGroup 2:\n- Name: Peter Rigaud (1 occurrence)\n\nTotal PII occurrences: 2', 'There is not enough text provided to identify and group PII (Personally Identifiable Information) information. Please provide more information or a specific paragraph or sentence from the text so that I can assist you better.', 'Unfortunately, without any text provided, I am unable to identify and group PII information. Please provide the text you would like me to analyze.', 'Based on the given text, it is not possible to identify and group PII (Personally Identifiable Information) information. The text contains the names of two companies, Getty Images and Shutterstock, along with a name, Yagnik Gorasiya. However, these names alone do not represent any specific PII information like Social Security numbers, addresses, phone numbers, etc. \n\nPlease provide a text that includes specific PII information in order to identify, group, and count it.', 'Based on the given text, there is only one group that contains PII (Personally Identifiable Information).\n\nGroup 1:\n- PII: +49 605 740 496 (phone number)\n\nTotal PII occurrences: 1', 'In the provided text, there is one occurrence of PII (Personally Identifiable Information) for the group "Email Address", which is "misiuniek@gmail.com".', 'Group 1:\n- Name: Zielona\n\nGroup 2:\n- Address: 15, 26-620 Warszawa\n\nThe count of PII occurrences is as follows:\n- Name: 1 occurrence\n- Address: 2 occurrences', 'Based on the provided text, it does not contain any personally identifiable information (PII) such as names, addresses, social security numbers, or any other identifiable information related to individuals. Therefore, there is no PII to identify, group, or count in this text.', 'In the given text, the following PII information can be identified and grouped:\n\nGroup 1:\n- Matthew Shoesmith\n\nGroup 2:\n- Revelation\n\nGroup 3:\n- Hilden\n\nNote: PII (Personally Identifiable Information) refers to any data that can potentially identify an individual. In this case, the PII information includes the name "Matthew Shoesmith" and the location "Hilden". The term "Revelation" is uncertain whether it represents PII or not, as it can refer to a personal identifier or be part of a business or organization name.', 'There is no PII information present in the text "Publication date of this report." PII (Personally Identifiable Information) typically refers to specific personal details such as names, addresses, social security numbers, email addresses, phone numbers, etc.', 'As an AI text-based model, I cannot see or analyze the actual content of the text you provided: "March 7, 2023." In order to identify, group, and count PII (Personally Identifiable Information) in a text, you need to provide actual text that may contain personal information such as names, addresses, social security numbers, etc. Once you provide the text, I will be able to assist you in identifying and counting PII occurrences.']

for reply in replies:
    print()
    lines = reply.splitlines()
    print()
    for line in lines:
        print(line)