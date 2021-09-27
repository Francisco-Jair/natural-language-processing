from nltk.book import text6


# a
ending_ise = [w for w in text6 if w.endswith('ise')]
print(ending_ise)

#b
containing_letter_z = [w for w in text6 if str(w).count('z') > 0]
print(containing_letter_z)

#c
containing_letter_pt = [w for w in text6 if str(w).count('pt') > 0]
print(containing_letter_pt)

#d
containing_capitalize = [w for w in text6 if w.title() == w > 0]
print(containing_capitalize)

