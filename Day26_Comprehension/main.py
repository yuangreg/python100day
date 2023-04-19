import pandas

df = pandas.read_csv("nato_phonetic_alphabet.csv")

dictionary = {val.letter:val.code for (key, val) in df.iterrows()}

word = "yuangreg"

output = [dictionary[letter.upper()] for letter in word]

print(output)