import time
import random

s1 = time.perf_counter()
some_list = [random.randint(0, 100000) for i in range(10 ** 6)]
s2 = time.perf_counter()
some_set = set(some_list)
s3 = time.perf_counter()
some_tuple = list(some_set)
s4 = time.perf_counter()

print(s2 - s1)
print(s3 - s2)
print(s4 - s3)
num = random.randint(0, 100)
s5 = time.perf_counter()
flag1 = num in some_list
s6 = time.perf_counter()
flag2 = num in some_set
s7 = time.perf_counter()
d1 = s6 -s5
d2 = s7 - s6
print(d1/d2)
print(flag1)
print(flag2)