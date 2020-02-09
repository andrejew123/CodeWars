"""
Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.

move_zeros([false,1,0,1,2,0,1,3,"a"]) # returns[false,1,1,2,1,3,"a",0,0]
"""


def move_zeros(array):
    if array.count(0) > 0:
        x = array.count(0) + array.count(0.0)
        lista_bez_zer = list(filter(lambda a: str(a) != "0", array))
        for i in range(x):
            lista_bez_zer.append(0)
        return lista_bez_zer
    else:
        return array

# describe("Basic tests")


assert move_zeros([1, 2, 0, 1, 0, 1, 0, 3, 0, 1]) == ([1, 2, 1, 1, 3, 1, 0, 0, 0, 0])
assert move_zeros([9, 0.0, 0, 9, 1, 2, 0, 1, 0, 1, 0.0, 3, 0, 1, 9, 0, 0, 0, 0, 9]) == ([9, 9, 1, 2, 1, 1, 3, 1, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
assert move_zeros(["a", 0, 0, "b", "c", "d", 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]) == (["a", "b", "c", "d", 1, 1, 3, 1, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
assert move_zeros(["a", 0, 0, "b", None, "c", "d", 0, 1, False, 0, 1, 0, 3, [], 0, 1, 9, 0, 0, {}, 0, 0, 9]) == (["a", "b", None, "c", "d", 1, False, 1, 3, [], 1, 9, {}, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
assert move_zeros([0, 1, None, 2, False, 1, 0]) == ([1, None, 2, False, 1, 0, 0])
assert move_zeros(["a", "b"]) == (["a", "b"])
assert move_zeros(["a"]) == (["a"])
assert move_zeros([0, 0])== ([0, 0])
assert move_zeros([0]) == ([0])
assert move_zeros([False]) == ([False])
# assert move_zeros[] == []


move_zeros([1, 2, 0, 1, 0, 1, 0, 3, 0, 1])