"""Your job is to write a function which increments a string, to create a new string.

If the string already ends with a number, the number should be incremented by 1.
If the string does not end with a number. the number 1 should be appended to the new string.
Examples:

foo -> foo1

foobar23 -> foobar24

foo0042 -> foo0043

foo9 -> foo10

foo099 -> foo100"""

def increment_string(strng):
    import pdb; pdb.set_trace()

    head = strng.rstrip('0123456789')
    tail = strng[len(head):]
    if tail == "": return strng+"1"
    return head + str(int(tail) + 1).zfill(len(tail))

assert (increment_string("foo") == "foo1")
assert (increment_string("123") == "124")
assert(increment_string("foobar001") == "foobar002")
assert(increment_string("foobar1") == "foobar2")
assert(increment_string("foobar00") == "foobar01")
assert(increment_string("foobar99") == "foobar100")
assert(increment_string(".f)z37131038w7AK=D8-83|%>967X4729184746235080") == "foobar100")
assert(increment_string("") == "1")

