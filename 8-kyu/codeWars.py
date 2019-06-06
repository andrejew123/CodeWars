
#  Create a function (or write a script in Shell) that takes an integer as an argument and returns "Even" for even numbers or "Odd" for odd numbers.takes an


#  solution no 1
from symbol import test


def even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"


#  solution no 2
def even_or_odd(number):
    return "Even" if number % 2 == 0 else "Odd"

print(even_or_odd(9))
# test.expect(even_or_odd(0) == "Even")
# test.expect(even_or_odd(7) == "Odd")
# test.expect(even_or_odd(1) == "Odd")
# test.expect(even_or_odd(-1) == "Odd")