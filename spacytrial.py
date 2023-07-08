import spacy

def detect(text):
    nlp = spacy.load('en_core_web_sm')
    doc = nlp(text)

    ai_c = 0
    for entity in doc.ents:
        if entity.label_ == 'PERSON' or entity.label_ == 'ORG':
            ai_c += 1
    ai_p = (ai_c / len(doc.ents)) * 100

    return ai_p

input_text = "Basketball is a team sport played by two teams of five players each. The primary objective is to score points by shooting the basketball through the opponent's hoop, which is mounted on a backboard 10 feet (3.048 meters) above the ground. The team with the most points at the end of the game wins. Basketball is played on a rectangular court, typically indoors, with a surface made of wood or synthetic materials. The rules and regulations are governed by various organizations, such as FIBA (International Basketball Federation) and the NBA (National Basketball Association)."

percentage = detect(input_text)
print(f"AI {percentage:.2f}%")
