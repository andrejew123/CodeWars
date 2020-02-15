'''The marketing team is spending way too much time typing in hashtags.
Let's help them with our own Hashtag Generator!

Here's the deal:

It must start with a hashtag (#).
All words must have their first letter capitalized.
If the final result is longer than 140 chars it must return false.
If the input or the result is an empty string it must return false.
Examples
" Hello there thanks for trying my Kata"  =>  "#HelloThereThanksForTryingMyKata"
"    Hello     World   "                  =>  "#HelloWorld"
""                                        =>  false'''


import re


def generate_hashtag(s):
    if len(s) == 0 or len(s) >= 140:
        return False
    else:
        return '#' + ''.join([i.capitalize() for i in re.sub(" +", " ", s).split()])


def generate_hashtag_2(s):
    output = "#"
    for word in s.split():
        output += word.capitalize()
    return False if (len(s) == 0 or len(output) > 140) else output


assert(generate_hashtag("    Hello     World   ")) == "#HelloWorld"
assert(generate_hashtag("")) == False

assert(generate_hashtag_2("    Hello     World   ")) == "#HelloWorld"
assert(generate_hashtag_2("")) == False