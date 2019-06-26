'''The main idea is to count all the occuring characters(UTF-8) in string. If you have string like this aba then the result should be { 'a': 2, 'b': 1 }

What if the string is empty ? Then the result should be empty object literal { }

For C#: Use a Dictionary<char, int> for this kata!
'''

#Solution 1
def count(string):
    dict = {}
    for i in set(string):
        dict[i] = string.count(i)
    return dict
assert count('aba') == {'a': 2, 'b': 1}

#Solution 2
def count(string):
    return {i: string.count(i) for i in string}
assert count('aba') == {'a': 2, 'b': 1}