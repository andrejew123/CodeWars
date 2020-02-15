"""Write a program that will calculate the number of trailing zeros in a factorial of a given number.

N! = 1 * 2 * 3 * ... * N

Be careful 1000! has 2568 digits...

For more info, see: http://mathworld.wolfram.com/Factorial.html

Examples
zeros(6) = 1
# 6! = 1 * 2 * 3 * 4 * 5 * 6 = 720 --> 1 trailing zero

zeros(12) = 2
# 12! = 479001600 --> 2 trailing zeros"""


def zeros_recursivle(n):
    if n == 0:
        return 1
    else:
        return zeros_recursivle(n-1)*n


def zeros2(n):
    result =1
    for i in range(n):
        result *= (i+1)
    return result


def zeros(n):
    result = 0
    for i in str(zeros_recursivle(n)):
        if i == "0":
            result += 1
            continue

def cos(n):   # Initialize result
    count = 0

    # Keep dividing n by
    # powers of 5 and
    # update Count
    i = 5
    while (n / i >= 1):
        count += int(n / i)
        i *= 5

    return int(count)


print(zeros_recursivle(30))
print(cos(30))