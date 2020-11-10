glossary = {
    "syntax": "The arrangement of words, phrases, and numbers to create code in a coding language.",
    "string": "In coding, any characters inside of quotation marks",
    "whitespace": "In coding, any non printing character, such as spaces or new lines.",
    "for loop": "A loop in coding used to repeat sections of code as many times as indicated by the statement.",
    "dictionary": "A series of key value pairs used in python code."
    }

for key, value in glossary.items():
    if key == "for loop":
        print("For loop:")
        print(f"{value}\n")
    else:
        print(f"{key.title()}:")
        print(f"{value}\n")