# def sum_str_My(*args):
#     res = ''
#     for item in args:
#         res += item
#     return res

# print(sum_str_My('q','e','r'))
# print(sum_str_My('q','w','e','r'))


# from modul import *
import modul

# print(myabs([-1,3,4,5,-4]))
# print(modul.myabs([-1,3,4,5,-4]))

# print(mymin([2,4,1]))

def fib(n):
    if n in [1,2]:
        return 1
    return fib(n-1) + fib(n-2)

for i in range(1,10):
    print(fib(i))

from sortmodul import *

arrayMy = [1, 7, 9, -1, 8, -4]
print(arrayMy)
print(*quicksortMy(arrayMy))
# print(arrayMy)
# print(*vstavkaMy(arrayMy))
print(arrayMy)
merge_sort(arrayMy)
print(arrayMy)
