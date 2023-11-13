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

prompt = "Identify, group and count PII information for each group in the following text:\n" + text
completion = client.chat.completions.create(
model="gpt-3.5-turbo",
messages=[
    {"role": "system", "content": "You are a legal assistant, skilled in counting PII occurrences."},
    {"role": "user", "content": prompt}
]
)

chat_response = completion.choices[0].message.content

print(chat_response)