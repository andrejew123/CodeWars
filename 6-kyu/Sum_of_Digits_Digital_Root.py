'''In this kata, you must create a digital root function.

A digital root is the recursive sum of all the digits in a number. Given n, take the sum of the digits of n. If that value has more than one digit, continue reducing in this way until a single-digit number is produced. This is only applicable to the natural numbers.

Here's how it works:

digital_root(16)
=> 1 + 6
=> 7

digital_root(942)
=> 9 + 4 + 2
=> 15 ...
=> 1 + 5
=> 6

digital_root(132189)
=> 1 + 3 + 2 + 1 + 8 + 9
=> 24 ...
=> 2 + 4
=> 6

digital_root(493193)
=> 4 + 9 + 3 + 1 + 9 + 3
=> 29 ...
=> 2 + 9
=> 11 ...
=> 1 + 1
=> 2'''

#Solution_1
def digital_root_1(n):
    wynik = 0
    if len(str(n)) ==1:
        return n
    else:
        for i in str(n):
            wynik += int(i)
    return digital_root_1(wynik)

assert digital_root_1(456) == 6

#Solution_2
def digital_root_2(n):
    return n if n < 10 else digital_root_2(sum(map(int,str(n))))

assert digital_root_2(456) == 6
