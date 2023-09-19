""" 1 """
# Создайте список list_ из целых чисел от 1 до 100 (включительно). Нужно использовать comprehension.
""" 
list_ = [i for i in range(1, 101)]
print(list_) 
"""



""" 2 """
# Создайте список list_ из нечётных целых чисел в промежутке от 1 до 50. Нужно использовать comprehension
""" 
list_ = [i for i in range(1, 50) if i%2!=0]
print(list_) 
"""



""" 3 """
# Создайте список используя list_ = [-4, -3, -2, -1, 0, 1, 2, 3, 4]
# и запишите в новый список int_list только четные числа, которые больше нуля. Нужно использовать comprehension.
""" 
list_ = [-4, -3, -2, -1, 0, 1, 2, 3, 4]
int_list = [i for i in list_ if i>0 and i%2==0]
print(int_list) 
"""



""" 4 """
# Создайте список list_ из квадратов всех чисел от 1 до 25 (включительно).
""" 
list_ = [i**2 for i in range(1, 26)]
print(list_)
"""



""" 5 """
# Используя данный список: str_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
# создайте новый список int_list, где все элементы, строки старого списка str_list, будут преобразованы в числовой тип данных
""" 
str_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
int_list = [int(i) for i in str_list]
print(int_list) 
"""



""" 6 """
# Создайте список list_ из чисел от 1 до 10 (включительно), заменяя четные числа - квадратом числа(число умноженное само на себя), нечетные добавьте без изменений.
""" 
list_ = [i if i%2!=0 else i**2 for i in range(1, 11)]
print(list_) 
"""



""" 7 """
# Пройдитесь по промежутку чисел от 1 до 10 и запишите в список list_ True вместо числа, если число чётное и False вместо числа, если число нечетное.
""" 
list_ = [ True if i%2==0 else False for i in range(1, 11)]
print(list_) 
"""



""" 8 """
# Создайте список из 10 произвольных имён list_name.
# Затем пройдитесь по данному списку и если длина имени меньше или равна 4 буквам создайте список new_list имя на shorter, а если больше на longer.
""" 
list_name = ['paul', 'john', 'george', 'ringo', 'eric', 'patty', 'yoko', 'cynthia', 'linda', 'jude' ] 
new_list = ['shorter' if len(name)<=4 else 'longer' for name in list_name]
print(new_list) 
"""



""" 9 """
# Создайте словарь dict_ из чисел от 1 до 10, где ключами будут сами числа, а значениями их квадраты. Нужно использовать comprehension.
""" 
dict_ = {num: num**2 for num in range(1, 11)}
print(dict_) 
"""



""" 10 """
# Запросите у пользователя число от 1 до 10 в переменную n. Затем пройдитесь по промежутку чисел от 1 до 500(включительно) и запишите в словарь dict_, 
# только те числа, которые кратны числу n (делятся на число n без остатка), введенное пользователем. Ключом будет само число, а значением его квадрат.
""" 
n = int(input('enter the num in range 1 to 10: '))
dict_ = {num : num**2 for num in range(1, 501) if num%n==0}
print(dict_) 
"""



""" 11 """
# Дан словарь a в котором значениями являются целые числа. Пройдитесь по элементам и запишите в dict_ значения на список чисел от 1 до числа,
# которое является значением. Нужно использовать comprehension.
""" 
a = {'a': 1, 'b': 5, 'c': 4, 'd': 3}
dict_ = {k:[i for i in range(1, v+1)] for k, v in a.items()}
print(dict_) 
"""



""" 12 """
# Создайте словарь dict_ где ключами будут строки, а значениями произвольные числа. 
# Затем пройдитесь по элементам и запишите в a вместо значения строку 'even', если значение четное, а если нет то 'odd'.
""" 
dict_ = {'first': 1, 'second': 2, 'third': 3}
a = {k: 'odd' if v%2!=0 else 'even' for k, v in dict_.items()}
print(a) 
"""



""" 13 """
# Дано предложение Получите список чисел list_ из этого предложения.
""" 
string_ = 'In 1984 there were 13 instances of a protest with over 1000 people attending'
list_ = [num for num in string_.split() if num.isdigit()]
print(list_) 
"""



""" 14 """
# Дан вложенный словарь dict_ (словарь состоящий из других словарей) в котором ключом является имя студента, а значением словарь с его оценками по 3 предметам.
# Распечатайте новый словарь, где вместо оценкок будет название предмета, по которому студент имеет высший балл. Нужно использовать comprehension.
""" 
dict_ = {'Timur': {'history': 90, 'math': 95, 'literature': 91}, 
         'Olga': {'history': 92, 'math': 96, 'literature': 81},
         'Nik': {'history': 84, 'math': 85, 'literature': 87}}
new_dict = {k:i for k,v in dict_.items() for i,j in v.items() if j == max(v.values()) } 
print(new_dict) 
"""



""" 15 """
# Дан словарь my_dict значениями в котором являются другие словари. Создайте новый словарь dict_, оставив те же ключи, но заменив значения, значениями внутренних словарей.
""" 
my_dict = {'first': {'a': 1}, 'second': {'b': 2}} 
dict_ = {key: v for key, value in my_dict.items() for v in value.values()}
print(dict_) 
"""



""" 16 """
# Создайте список list_ из чётных целых чисел в промежутке от 1 до 25. Нужно использовать comprehension.
""" 
list_ = [i for i in range(2, 26, 2)]
print(list_) 
"""



""" 17 """
# Создайте список используя list_ = [-4, -3, -2, -1, 0, 1, 2, 3, 4] и запишите в новый список int_list числа, которые меньше нуля, замените на 1.
""" 
list_ = [-4, -3, -2, -1, 0, 1, 2, 3, 4]
int_list = [1 if i<0 else i for i in list_]
print(int_list) 
"""



""" 18 """
# Из списка list1 = [1, 2, 'hello', 3, 'world', 4, 5, 'book', 'code', 6, 'Makers', 7, 8, 9, 10] Создайте новый list2 и внесите туда только строки из list1.
""" 
list1 = [1, 2, 'hello', 3, 'world', 4, 5, 'book', 'code', 6, 'Makers', 7, 8, 9, 10]
list2 = [i for i in list1 if type(i)==str]
print(list2) 
"""



""" 19 """
# Создайте список используя list_ = [0, 3, 9, 7, 5, 2, 18, 4] И запишите в новый список list1 только те числа, которые больше 5.
""" 
list_ = [0, 3, 9, 7, 5, 2, 18, 4]
list1 = [i for i in list_ if i>5]
print(list1) 
"""



""" 20 """
# list_ = [False, True, False, True, False, True, False, True, False, True] Создайте новый. Значение True замените на 1, а False на 0.
""" 
list_ = [False, True, False, True, False, True, False, True, False, True]
binary_list = [1 if i else 0 for i in list_]
print(binary_list) 
"""



""" 21 """
# Создайте список из 10 произвольных имён list_name.
# Затем создайте список new_list, вместо имени вписав туда его длину.
""" 
list_name = ['paul', 'john', 'george', 'ringo', 'eric', 'patty', 'yoko', 'cynthia', 'linda', 'jude' ] 
new_list = [len(i) for i in list_name]
print(new_list) 
"""



""" 22 """
# Создайте список из четных чисел в диапазоне от 1 до 1000 с шагом 125
""" 
new_list = [i for i in range(1, 1000, 125) if i % 2 == 0]
print(new_list) 
"""



""" 23 """
# Из списка list1 = [44,54,64,74,104] Создайте новый list2, прибавив к каждому числу 6
""" 
list1 = [44,54,64,74,104]
list2 = [i+6 for i in list1]
print(list2) 
"""



""" 24 """
# Из списка list1 = [2, 4, 6, 8, 10, 12, 14] Создайте новый, внеся туда только те числа квадрат которых больше 50
""" 
list1 = [2, 4, 6, 8, 10, 12, 14]
new_list = [i for i in list1 if i**2>50]
print(new_list) 
"""



""" 25 """
# Из сторки string = "happy birthday!" Создайте список list_, внесите туда все символы из строки кроме пробела и '!'
""" 
string = "happy birthday!"
list_ = [i for i in string if i.isalpha()]
print(list_) 
"""



""" 26 """
# Дан словарь: dict_ = {'a': {'d': 3, 'e': 45}, 'b': {'f': 23, 'j': 9}, 'c': {'h': 12, 'i': 89}} Используйте его чтобы создать список, из значений внутренних словарей
""" 
dict_ = {'a': {'d': 3, 'e': 45}, 'b': {'f': 23, 'j': 9}, 'c': {'h': 12, 'i': 89}}
list_ = [i for v in dict_.values() for i in v.values()]
print(list_) 
"""



""" 27 """
# Из списка: list_name = ['paul', 'john', 'george', 'ringo', 'eric', 'patty', 'yoko', 'cynthia', 'linda', 'jude' ] 
# Создайте словарь, занесите только те имена, длина которых больше 4. Ключами будут имена, а значениями их длины, возведенные в квадрат.
""" 
list_name = ['paul', 'john', 'george', 'ringo', 'eric', 'patty', 'yoko', 'cynthia', 'linda', 'jude' ]
dict_ = {name : len(name)**2 for name in list_name if len(name)>4}
print(dict_) 
"""



""" 28 """
# Дан словарь dict_ = {"Sedan": 1500, "SUV": 2000, "Pickup": 2500, "Miivan": 1600, "Vann": 2400, "Semi": 13600, "Bicycle": 7, "Motorcycle": 110}
# Пройдитесь по словарю и добавьте в список только те ключи, значение, которых в диапазоне от 200 до 5000, добавленные в список ключи должны быть в верхнем регистре.
""" 
dict_ = {"Sedan": 1500, "SUV": 2000, "Pickup": 2500, "Miivan": 1600, "Vann": 2400, "Semi": 13600, "Bicycle": 7, "Motorcycle": 110}
new_list = [k.upper() for k, v in dict_.items() if v in range(200, 5001)]
print(new_list) 
"""



""" 29 """
# Дан словарь: dict1 = {"Sedan": 1500, "SUV": 2000, "Pickup": 2500, "Miivan": 1600, "Vann": 2400, "Semi": 13600, "Bicycle": 7, "Motorcycle": 110}
# Создайте словарь dict2:
# Ключи должны быть те же, что и в первом словаре, но каждый символ 'i' замените на '' Значением должно быть количество повторений символа 'i' в этом ключе
""" 
dict1 = {"Sedan": 1500, "SUV": 2000, "Pickup": 2500, "Miivan": 1600, "Vann": 2400, "Semi": 13600, "Bicycle": 7, "Motorcycle": 110}
dict2 = {k.replace('i', ''): k.count('i') for k in dict1.keys()}
print(dict2) 
"""



""" 30 """
# Из списка list1 = [1, 2, 3, 0, None, 'a', 'abc', [], 23, [1, 2, 3, 4], '', {'a': 1, 'b': 2}, 'drf', []]
# Создайте новый list2, не добавляя все пустые значения (0, None, [], {}, '')
""" 
list1 = [1, 2, 3, 0, None, 'a', 'abc', [], 23, [1, 2, 3, 4], '', {'a': 1, 'b': 2}, 'drf', []]
list2 = [i for i in list1 if i]
print(list2) 
"""



""" 31 """
# Дан список SPL_Patrons. Каждый его подсписок содержит две части информации о посетителях библиотеки:имя посетителя
# количество книг, которые они одолжили за последний год Используйте list comprehension, чтобы создать список readers имен меценатов, 
# которые в прошлом году одолжили более 100 книг
""" 
SPL_Patrons = [
['Kim Tremblay', 134],
['Emily Wilson', 42],
['Jessica Smith', 215],
['Alex Roy', 151],
['Sarah Khan', 105],
['Samuel Lee', 220],
['William Brown', 24],
['Ayesha Qureshi', 199],
['David Martin', 56],
['Ajeet Patel',69]
]
readers = [i[0]for i in SPL_Patrons if i[-1]>100]
print(readers) 
"""



""" 32 """
# Из предыдущего списка SPL_Patrons: предположим, что посетитель экономит в среднем 11,95 доллара, одалживая книгу вместо того, чтобы покупать ее. 
# Используйте list comprehension, чтобы создать список saved_amount сэкономленной суммы для каждого клиента
""" 
SPL_Patrons = [
['Kim Tremblay', 134],
['Emily Wilson', 42],
['Jessica Smith', 215],
['Alex Roy', 151],
['Sarah Khan', 105],
['Samuel Lee', 220],
['William Brown', 24],
['Ayesha Qureshi', 199],
['David Martin', 56],
['Ajeet Patel',69]
]
saved_amount = [round(11.95*i[-1], 2) for i in SPL_Patrons]
print(saved_amount) 
"""



""" 33 """
# Используйте comprehensions для создания списка из списков, где каждый подсписок состоит из имени пирата и стоимости его / ее награбленных мешков с зерном 
# (рассчитайте стоимость зерна, предположим, что средняя рыночная стоимость мешка зерна составляет 42 доллара, но включите только тех пиратов, которые любят попугаев)
""" 
prairie_pirates = [
['Tractor Jack', 1000, True],
['Plowshare Pete', 950, False],
['Prairie Lily', 245, True],
['Red River Rosie', 350, True],
['Mad Athabasca McArthur', 842, False],
['Assiniboine Sally', 620, True],
['Thresher Tom', 150, True],
['Cranky Canola Carl', 499, False]
]
a = [[i[0], i[1]*42] for i in prairie_pirates if i[-1]]
print(a) 
"""



""" 34 """
# По данному ниже словарю, пройдитесь циклом Найдите сумму лайков всех пользователей, рейтинг которых выше 3. используйте list comprehension
""" 
dict_ = {
    'Sasha': {
        'likes': 23,
        'comments': 2,
        'rating': 4
    },
    'Aliya': {
        'likes': 34,
        'comments': 5,
        'rating': 5
    },
    'Dasha': {
        'likes': 15,
        'comments': 3,
        'rating': 2
    },
    'Luna': {
        'likes': 12,
        'comments': 2,
        'rating': 1
    },
    'Rena': {
        'likes': 26,
        'comments': 7,
        'rating': 2
    }
}
total = [v['likes'] for k,v in dict_.items() if v['rating']>3]
print(sum(total)) 
"""



""" 35 """
# Используя приведенный словарь dict_, создайте список из id, которые хранятся под ключом comments. Берите только те комментарии, количество которых больше 3
""" 
dict_ = {
    'Dasha': {
        'likes': 15,
        'comments': [
            {'id': 1, 'text': 'some text'},
            {'id': 2, 'text': 'some text'},
        ],
        'rating': 2
    },
    'Luna': {
        'likes': 12,
        'comments': [
            {'id': 1, 'text': 'some text'},
            {'id': 2, 'text': 'some text'},
            {'id': 3, 'text': 'some text'},
        ],
        'rating': 1
    },
    'Rena': {
        'likes': 26,
        'comments': [
            {'id': 1, 'text': 'some text'},
            {'id': 2, 'text': 'some text'},
            {'id': 3, 'text': 'some text'},
            {'id': 4, 'text': 'some text'},
            {'id': 5, 'text': 'some text'},
            {'id': 6, 'text': 'some text'},
        ],
        'rating': 2
    }
}
dict1 = [b['id'] for value in dict_.values() for b in value['comments'] if len(value['comments']) > 3] 
print(dict1) 
"""



""" 36 """
# Создайте список list_ от 0 до 10 включительно c помощью специальной функции которая генерирует последовательно чисел,
# отфильтруйте список оставив в нем только четные элементы,
# затем разделите каждый элемент на 2 и выведите результат,
# нужно работать только с одним списком, нельзя создавать доп. списки.
# Необходимо использовать list comprehension
# Распечатайте результат
""" 
list_ = [i/2 for i in range(0, 11, 2)]
print(list_) 
"""



""" 37 """
# Создайте словарь dict_ в котором ключами будут числа, а значениями строки. Перебирите словарь циклом:
# если ключ четный, нужно заменить его значение на длину этого значения
# если ключ нечетный то возвести длинну его значения в 3 степень Распечатайте dict_
""" 
dict_ = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five'}
dict_ = {k: len(v) if k%2==0 else len(v)**3 for k, v in dict_.items()}
print(dict_) 
"""



""" 38 """
# Создайте 2 сета set1 и set2 из 10 рандомных элементов
# Затем объедините их (специальным методом) в переменную full_set,
# И если их длина меньше 20, то вы должны вывести сообщение:
# "В этом сете было 3 повторения, его длина составляет 17",
# 3 это количество элементов, которые были не уникальны,
# Если же длина равна 20 то выведите сообщение "Ваш объединенный сет полностью уникальный!"
# Необходимо использовать set comprehension, на этапе создания сетов.
# Так же используйте генератор последовательности в comprehension чтобы создать множества из 10 элементов.
# Необходимо использовать set comprehension, на этапе создания сетов.
# Например после использования set comprehension в set1 храниться множество: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
# B set2: {8, 9, 10, 11, 12, 13, 14, 15, 16, 17}
# Результат работы программы будет следующий:
# "В этом сете было 2 повторения, его длинна составляет 18"
""" 
set1 = {i for i in range(0, 10)}
set2 = {i for i in range(6, 16)}
full_set = set1 | set2
if len(full_set) == 20:
    print("Ваш объединенный сет полностью уникальный!")
else:
    print(f"В этом сете было {20-len(full_set)} повторения, его длина составляет {len(full_set)}") 
"""


