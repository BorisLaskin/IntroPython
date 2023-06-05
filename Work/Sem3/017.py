# Дан список чисел. Определите, сколько в нем
# встречается различных чисел.

# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6

import random
length = random.randint(10,20)
some_list = [random.randint(0, 10) for _ in range(length)]
some_set = set(some_list)
print(len(some_list))
print(*some_list)
print(len(some_set))