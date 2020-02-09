from cmath import sqrt


# def comp(array1, array2):
#     for i in array2:
#         print(i)
#         if sqrt(i) not in array1:
#             print(i)
#     return False sqrt(i) not in array2 for i in array2 else True
#
#
#
# a1 = [121, 144, 19, 161, 19, 144, 19, 11]
# a2 = [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]
# comp(a1, a2)


def maskify(cc):
    a =""
    if len(cc) <=4:
        return cc
    else:
        for i in cc[:-4]:
            a += "#"
    return print(a+cc[:4])

maskify("SF$SDfgsd2eA")