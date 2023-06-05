# Задача №21. Решение в группах
# Напишите программу для печати всех уникальных
# значений в словаре.
# Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
# {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII
# ":" S007 "}]
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}
some_dict = {"I": "S001", "II": "S002", "III": "S001", "IV": "S005", "VII": "S005", "V":"S009", " VIII":"S007"}
some_list = [v for (_,v) in some_dict.items()]
some_set = set(some_list)
print(some_set)