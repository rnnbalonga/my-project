import pandas as p

#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}



phonetic_alphabet_df = p.read_csv("nato_phonetic_alphabet.csv")

phonetic_code = {row["letter"]:row["code"] for index, row in phonetic_alphabet_df.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

