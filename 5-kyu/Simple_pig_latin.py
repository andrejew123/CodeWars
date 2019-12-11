"""Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.

Examples
pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')     # elloHay orldway !

"""
from string import punctuation


def pig_it(text):
    return " ".join([i[1:] + i[0] + "ay" if i not in punctuation else i for i in text.split()])


assert pig_it('This is my string') == 'hisTay siay ymay tringsay'
assert pig_it('Hello world !') == 'elloHay orldway !'
