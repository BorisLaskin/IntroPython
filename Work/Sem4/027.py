# Пользователь вводит текст(строка).
# Словом считается последовательность непробельных символов идущих подряд,
# слова разделены одним или большим числом пробелов
# или символами конца строки. Определите, сколько различных
# слов содержится в этом тексте.
# Александр LyraX: без метода split()

some_set = {' ', '\n', '\t'}
some_string = input("Введите текст: ")
flag = 0
old_flag = 0
counter = 0
for i in range(0, len(some_string)):
    if some_string[i] not in some_set:
        flag = 1
    else:
        flag = 0
    if flag == 1 and old_flag == 0:
        counter += 1
    old_flag = flag
print(f"Сколько различных слов содержится в этом тексте: {counter}")
import re
# print(len(some_string.split()))
print(len(re.split(" ", some_string)))
print(re.split(" ", some_string))