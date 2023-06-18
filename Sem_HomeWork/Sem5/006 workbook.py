# Дана строка (возможно, пустая), состоящая
# из букв A-Z:
# AAAABBBCCXYZDDDDEEEFFFAAAAAABBBB
# BBBBBBBBBBBBBBBBBBBBBBBB
# Нужно написать функцию RLE,
# которая на выходе даст строку вида:
# A4B3C2XYZD4E3F3A6B28
def rle(s_list):
    flag_list = [1 if s_list[i] == (s_list[i + 1]) else 0 for i in range(len(s_list) - 1)]
    counter2 = 1
    some_string = str()
    print(s_list)
    print(flag_list)
    for i in range(len(flag_list)):
        if flag_list[i]:
            counter2 += 1
        else:
            some_string += s_list[i] + str(counter2) if counter2 != 1 else ''
            counter2 = 1
    else:
        if counter2 != 1:
            some_string += str(counter2)
        else:
            some_string += s_list[-1]

    return some_string


string = 'AAAABBBCCXYZDDDDEEEFFFAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBBC'
print(rle(string))
