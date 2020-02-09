"""Complete the function scramble(str1, str2) that returns true if a portion of str1 characters can be rearranged to match str2, otherwise returns false.

Notes:

Only lower case letters will be used (a-z). No punctuation or digits will be included.
Performance needs to be considered
Input strings s1 and s2 are null terminated.
Examples
scramble('rkqodlw', 'world') ==> True
scramble('cedewaraaossoqqyt', 'codewars') ==> True
scramble('katas', 'steak') ==> False
"""


def scramble(s1,s2):
    for c in set(s2):
        if s1.count(c) < s2.count(c):
            return False
    return True


assert scramble('rkqodlw', 'world') == True
assert scramble('cedewaraaossoqqyt', 'codewars') == True
assert scramble('katas', 'steak') == False
assert scramble('scriptjava', 'javascript') == True
assert scramble('scriptingjava', 'javascript') == True
