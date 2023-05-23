import pandas as p

#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}



phonetic_alphabet_df = p.read_csv("nato_phonetic_alphabet.csv")

phonetic_code = {row.letter:row.code for (index, row) in phonetic_alphabet_df.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

def generate_code():
    user_word = input("Write your word here: ").upper()

    try:
        code_list = [phonetic_code[letter] for letter in user_word]
    except KeyError:
        print("Only letters in the alphabet please.")
        generate_code()
    else:
        print(code_list)

generate_code()