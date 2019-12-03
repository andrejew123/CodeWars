"""The function will be given a variable amount of arguments, each one being a letter to add.

Notes:
Letters will always be lowercase.
Letters can overflow (see second to last example of the description)
If no letters are given, the function should return 'z'
Examples:
add_letters('a', 'b', 'c') = 'f'
add_letters('a', 'b') = 'c'
add_letters('z') = 'z'
add_letters('z', 'a') = 'a'
add_letters('y', 'c', 'b') = 'd' # notice the letters overflowing
add_letters() = 'z'"""

def add_letters(*letters):
    alpha_dict = {'a': 1, 'c': 3, 'b': 2, 'e': 5, 'd': 4,
                  'g': 7, 'f': 6, 'i': 9, 'h': 8, 'k': 11,
                  'j': 10, 'm': 13, 'l': 12, 'o': 15, 'n': 14,
                  'q': 17, 'p': 16, 's': 19, 'r': 18, 'u': 21,
                  't': 20, 'w': 23, 'v': 22, 'y': 25, 'x': 24,
                  'z': 26}

    result = 0
    if len(letters) == 0:
        return 'z'
    for letter in letters:
        result += alpha_dict[letter]
        if result > 26:
            result = result - 26

    return [letter for letter, number in alpha_dict.items() if result == number][0]

assert add_letters('y', 'c', 'b') == 'd'
assert add_letters('z', 'a') == 'a'
assert add_letters('a', 'b', 'c') == 'f'