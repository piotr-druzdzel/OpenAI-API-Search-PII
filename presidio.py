from presidio_analyzer import AnalyzerEngine

text = """
Our sustainability publications on the internet:
🔗 www.henkel.com/sustainability/reports
Henkel; Namthip Muanthongthae via Getty 
Images; Nils Hendrik Müller; Peter Rigaud; 
Henkel app available for iOS and Android:
RgStudio via Getty Images; Westend61 via  
Getty Images; Yagnik Gorasiya via Shutterstock
Translation +48 605 740 496
Hmm misiuniek@gmail.com
Best ice cream: Zielona 15, 26-620 Warszawa
RWS Holdings PLC 
Matthew Shoesmith, Revelation, Hilden
Publication date of this report
March 7, 2023 
"""


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
