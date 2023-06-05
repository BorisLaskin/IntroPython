# Александр LyraX: 15. Иван Васильевич пришел на рынок и решил купить два арбуза: один для себя, а другой для тещи.
# Понятно, что для себя нужно выбрать арбуз потяжелей, а для тещи полегче. Но вот незадача:
# арбузов слишком много и он не знает как же выбрать самый легкий и самый тяжелый арбуз? Помогите ему!
from itertools import count

# Пользователь вводит одно число N – количество арбузов.
# Вторая строка содержит N чисел, записанных на новой строчке каждое.
# Здесь каждое число – это масса соответствующего арбуза. Все числа натуральные и не превышают 30000.

numer_berry = int(input("Введите количество арбузов: "))
ind = 0
berry_mass_limit = 30000
max_berry = 0
min_berry = berry_mass_limit
max_berry_ind = -1
min_berry_ind = -1
while ind < numer_berry:
    if (berry_mass := int(input("Введите массу арбуза: "))) > berry_mass_limit:
        print(f"Масса арбуза {berry_mass} не должна превышать {berry_mass_limit}")
        continue
    elif berry_mass > 0:
        if berry_mass > max_berry:
            max_berry = berry_mass
            max_berry_ind = ind
        if berry_mass < min_berry:
            min_berry = berry_mass
            min_berry_ind = ind
        ind += 1
else:
    print(f"Себе возьмем арбузов {max_berry_ind + 1}-й массой {max_berry} кг, а теще {min_berry_ind+1} -й массой {min_berry} кг")
