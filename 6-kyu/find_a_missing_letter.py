"""#Find the missing letter

Write a method that takes an array of consecutive (increasing) letters as input and that returns the missing letter in the array.

You will always get an valid array. And it will be always exactly one letter be missing. The length of the array will always be at least 2.
The array will always contain letters in only one case.

Example:

['a','b','c','d','f'] -> 'e' ['O','Q','R','S'] -> 'P'

["a","b","c","d","f"] -> "e"
["O","Q","R","S"] -> "P"
(Use the English alphabet with 26 letters!)

Have fun coding it and please don't forget to vote and rank this kata! :-)

I have also created other katas. Take a look if you enjoyed this kata!
"""
import string


def find_missing_letter(chars):
    new_ascii_list = string.ascii_letters[string.ascii_letters.index(chars[0]):]
    for i in range(len(chars)):
        if chars[i] != new_ascii_list[i]:
            return new_ascii_list[i]


def find_missing_letter_with_ord(chars):
    n = 0
    while ord(chars[n]) == ord(chars[n + 1]) - 1:
        n += 1
    return chr(ord(chars[n]) + 1)


assert (find_missing_letter(['d', 'e', 'g', 'h'])) == 'f'

assert (find_missing_letter_with_ord(['d', 'e', 'g', 'h'])) == 'f'
