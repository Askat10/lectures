""" 1 """
# Создайте список name_of_friends с именами пяти друзей.
# Затем выведите эти имена по одному, обращаясь к каждому элементу списка.
""" 
name_of_friends = ['Jack', 'Hellboy', 'Joshua', 'Charlie', 'Kate']
for name in name_of_friends:
    print(name) 
"""



""" 2 """
# Выберите свой любимый вид транспорта (например, мотоциклы или машины) и создайте список labels с марками этого вида транспорта.
# Используя цикл for, выведите утверждения о каждом из элементов списка labels
""" 
labels = ['BMW', 'Mercedes', 'Lamborghini', 'Lexus']
for label in labels:
    print(f'I like brand {label}') 
"""



""" 3 """
# Дан список name_of_list в котором хранится строка.
# Разрежьте ее на две равные части.
# Если длина строки нечетная, то длина первой части должна быть на один символ больше.
# Переставьте эти две части местами, при этом каждый символ должен являться отдельной строкой.
# Результат запишите в новый список new_list и выведите на экран.
""" 
name_of_list = ['Alans']
name_string = name_of_list[0]
new_list = []
first_part =[]
for letter in name_string:
    new_list.append(letter)
for letter in range(len(new_list)//2):
    first_part.append(new_list[0])
    new_list.remove(new_list[0])

if len(first_part) < len(new_list):
    first_part.append(new_list[0])
    new_list = new_list[1:]
new_list += first_part
print(new_list) 
"""



""" 4 """
# Создайте список list_, состоящий ровно из двух строк.
# Переставьте эти строки местами.
# Результат запишите в новый список new_list и выведите в консоль получившийся результат
""" 
list_ = ['Bye', 'good']
new_list = list_[::-1]
print(new_list)
"""



""" 5 """
# Вы собираетесь на Иссык-Куль. Пока ваш чемодан пуст: suitcase = []. Однако он может вместить всего 5 вещей.
# Положите 5 вещей в чемодан с помощью метода append()
# Вы передумали, и решили убрать последнюю вещь. Вспомните, какой метод помогает удалить последний элемент.
# Вы решили положить в чемодан другую вещь, только в первое место (т.е. по индексу 0). Вспомните метод, который ставит элементы по индексу.
# Распечатать чемодан
""" 
suitcase = []
suitcase.append('ball')
suitcase.append('sunglasses')
suitcase.append('shirt')
suitcase.append('shorts')
suitcase.append('sunscreen')
suitcase.pop()
suitcase.insert(0, 'trunks')
print(suitcase) 
"""



""" 6 """
# Создать список чисел nums.
# Используя цикл и метод списка, запишите все числа меньше 5 в новый список.
# Результат запишите в переменную res и выведите в терминал.
""" 
nums = [i for i in range(20)]
new_nums = []
for num in nums:
    if num <5:
        new_nums.append(num)
print(new_nums) 
"""



""" 7 """
# Вы принимаете от пользователя последовательность чисел, разделенных запятой в переменную.
# Создайте список list_ и кортеж tuple_ с этими числами и распечатайте их.
# Для проверки, введите числа через запятую(без пробелов) в поле во вкладке INPUT.
""" 
nums = input('enter nums divided by comma: ')
list_ = nums.split(',')
tuple_ = tuple(num for num in nums if num.isdigit())                                 # or tuple_ = tuple(list_)
print(list_)
print(tuple_) 
"""



""" 8 """
# Создайте список чисел list_.
# Пройдитесь по элементам списка и преобразуйте все числа в строку.
# Результат запишите в новый список new_list и выведите в терминал.
""" 
list_ = [i for i in range(20)]
new_list = [str(num) for num in list_]
print(new_list) 
"""



""" 9 """
# Создайте список чисел list_.
# Переберите элементы циклом и вместо четных чисел, поставьте строку четное, а вместо нечетных нечетное.
# Результат записать в новый список new_list и вывести в терминал.
""" 
list_ = [i for i in range(0, 20)]
new_list = ['четное' if i%2==0 else 'нечетное' for i in list_]
print(new_list) 
"""



""" 10 """
# Используя функцию range() создайте список list_ из 20 произвольных чисел.
# Распечатайте результат
""" 
list_ = [i for i in range(20)]
print(list_) 
"""



""" 11 """
# При помощи функции range() создайте список list_ из чётных чисел от 0 до 100 (включительно).
# Распечатайте результат.
""" 
list_ = [i for i in range(101) if i%2==0]
print(list_) 
"""



""" 12 """
# Создайте два списка list1, list2 со случайным набором чисел.
# Объедините эти списки.
# Затем, выведите сумму всех чисел в консоль
""" 
list1 = [23, 45, 246, 6]
list2 = [1, 2, 54, 468, 53, 356]
list1.extend(list2)
print(sum(list1)) 
"""



""" 13 """
# Написать программу, которая будет принимать от пользователя числа через запятую, без пробелов.
# числа поместить в список list_ и вывести в отсортированном виде.
# Числа переданные во вкладке INPUT сохраняются в строковом типе данных.
""" 
nums = input('enter the numbers by comma: ')
nums = nums.split(',')
list_ = [int(num) for num in nums]
list_.sort()
list_ =[str(num) for num in list_]
print(list_) 
"""



""" 14 """
# Создать три числа в списке list_.
# Вывести на экран yes, если среди них есть одинаковые, иначе вывести ERROR.
""" 
list_ =[1, 2, 1]
for i in list_:
    if list_.count(i) >1:
        print('yes')
        break
else:
    print('ERROR') 
"""



""" 15 """
# Записать в список list_ все числа в промежутке от 54 до 9184 делящиеся на 5 без остатка.
# Распечатайте результат.
""" 
list_ = [i for i in range(54, 9185) if i % 5 ==0]
print(list_) 
"""



""" 16 """
# Дан список целых чисел, найдите минимальное значение, не используя встренную функцию min().
""" 
list_ = [2, 4, 1, 67, -1]
min_number = list_[0]
for num in list_[1:]:
    if num < min_number:
        min_number = num
        list_.remove(num)

print(min_number)
"""



""" 17 """
# Дан список с кортежами, выведите список без пустых кортежей
""" 
tuples = [(), ('ram','15','8'), (), ('laxman', 'sita')]
cleared_tuples = []
for tuple_ in tuples:
    if bool(tuple_) != False:
        cleared_tuples.append(tuple_)

print(cleared_tuples) 
"""



""" 18 """
# Запросите у пользователей 5 раз их имя и фамилию, но в списке сохраните лишь фамилию, также учтите, что у человека ФИО может состоять не только из 2 слов.
# При выводе должен выходить отсортированный в алфавитном порядке список
""" 
name1 = input('enter here: ').split(' ')
name2 = input('enter here: ').split(' ')
name3 = input('enter here: ').split(' ')
name4 = input('enter here: ').split(' ')
name5 = input('enter here: ').split(' ')
list_of_last_names = []
list_of_last_names.append(name1[-1])
list_of_last_names.append(name2[-1])
list_of_last_names.append(name3[-1])
list_of_last_names.append(name4[-1])
list_of_last_names.append(name5[-1])
print(sorted(list_of_last_names)) 
"""



""" 19 """
# Вам дан список из чисел, и переменная x в которой хранится число, посчитайте сколько вхождений этого числа в этом списке
""" 
list_ = [8, 6, 8, 10, 8, 20, 10, 8, 8]
number = 4
print(list_.count(number)) 
"""



""" 20 """
# Вам дан список с числами и строками, найдите сумму чисел в этом списке не используя функцию sum()
# Числа могут быть в виде строки
# Все числа положительные
# Все числа целые
""" 
list_ = [1, 'abcd', 3, '1', 4, 'xyz', 5, 'pqr', 7, 5, 12]
total = 0
for i in list_:
    if str(i).isdigit():
        total += int(i)

print(total) 
"""



""" 21 """
# Вам дан список из строк, в которых длина строки равна 2 или более, в новый список запишите индексы тех строк, у которых первый и последний символы совпадают.
""" 
str_list = ['abc', 'xyz', 'aba', '1221']
new_list = [str_list.index(i) for i in str_list if i[0] == i[-1]]
print(new_list) 
"""



""" 22 """
# У вас есть список со вложенными списками, выведите самый длинный список и самый короткий
""" 
lists = [[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
max_list = max(lists, key=len)
lists.remove(max_list)
if len(lists) > 0:
    min_list = min(lists, key=len)
else:
    min_list = None
if max_list == min_list:
    min_list = None
print(f'max_list {max_list}')
print(f'min_list {min_list}') 
"""



""" 23 """
# Вам дан список, напишите код, который будет соединять в новый список элементы по n-ному шагу
""" 
step = 3
list_ = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
new_list =[]
num = 0
for i in range(step):
    total = []
    for l in list_[num::step]:
        total.append(l)
    new_list.append(total)
    num +=1
print(new_list) 
"""



""" 24 """
# Напишите код для создания матрицы с размером sizexsize
""" 
size = 3
list_ =[]
for i in range(size):
    new_list = [i for i in range(1, size+1)]
    list_.append(new_list)

print(list_) 
"""



""" 25 """
# Вам дан список со словами, пользователь вводит первую букву слова, которое он ищет, ваш код должен вывести список со всеми словами начинающимися на эту букву
""" 
list_ = ['sun', 'flowers', 'rumor', 'stranger', 'adventure', 'architect', 'accompany', 'abandon', 'cartoon']
letter = input('enter one letter: ')
new_list = []
for i in list_:
    if i[0] == letter:
        new_list.append(i)
print(new_list) 
"""



""" 26 """
# Вам даны 2 списка, напишите код, который будет выводить разницу первого списка от второго и наоборот
""" 
colors1 = ["red", "orange", "green", "blue", "white"]
colors2 = ["black", "yellow", "green", "blue"]
total1 = []
total2 = []
for i in colors1:
    if i not in colors2:
        total1.append(i)

for i in colors2:
    if i not in colors1:
        total2.append(i)

print(total1,total2) 
"""



""" 27 """
# Вам даны 2 списка из чисел, нужно написать код, который будет выводить True, если есть хотя бы один общий элемент, в ином случае False
""" 
list1 = [1,2,3,4,5]
list2 = [5,6,7,8,9]
a = False
for i in list1:
    if i in list2:
        a = True

print(a) 
"""



""" 28 """
# Ван дан список, выведите числа, частота повторений которых больше или равно repeats
""" 
list_ = [4, 6, 4, 3, 3, 8, 4, 3, 4, 3, 8, 8]
repeats = 3
res = []
for i in list_:
    if list_.count(i) >= repeats:
        if i not in res:
            res.append(i)

print(res) 
"""



""" 29 """
# Вам дан список из 3 чисел, выведите все возможные комбинации с этими числами
""" 
from itertools import permutations 
list_ = [1, 2, 3] 
comb = permutations(list_) 
for i in comb: print(i) 
"""



""" 30 """
# Создайте список с 3 вложенными списками, где внутри должно быть три 0 K = 3 (количество списков и элементов)
""" 
K = 3
result = []
for i in range(K):
    res = [0 for i in range(K)]
    result.append(res)

print(result) 
"""



""" 31 """
# Вам дан список со строками, необходимо перевернуть эти строки, а также отсортировать по длине
""" 
colors = ["Red", "Green", "Blue", "White", "Black", "Yellow", "Orange"]
result = []
for i in colors:
    result.append(i[::-1])



result.sort(key=len)
print(result) 
"""



""" 32 """
# Вам дан список с элементами, добавьте элемент, который хранится в переменной element в этот список после каждого n-ого шага
""" 
list_ = [1,2,3,4,5,6,7,8,9,0]
step = 2
element = 'A'
mul = 1
add = 0
for i in range(len(list_)//step):
    list_.insert(mul*step+add, element)
    add += 1
    mul += 1

print(list_) 
"""



""" 33 """
# Вам дан список со вложенными списками, выведите тот список, у которого самая большая сумма
""" 
lists = [[1, 2, 3], [4, 5, 6], [10, 11, 12], [7, 8, 9]]
max_ = max(lists, key=sum)
print(max_) 
"""



""" 34 """
# Дан список целых чисел с повторяющимися элементами. Вам надо создать еще один список, содержащий только повторяющиеся элементы. 
# Проще говоря, новый список должен содержать элементы, которых больше одного.
""" 
list_ = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]
repeated = []
for i in list_:
    if list_.count(i) > 1 and i not in repeated:
        repeated.append(i)

print(repeated) 
"""



""" 35 """
# Вам дан список из букв, пользователь вводит 2 буквы, от какой и до какой буквы нужно соединить в одну строку, ваш код должен соединить эти буквы
""" 
chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g'] 
chars_list = [] 
chars_new = [] 
merge_from = input('Type letter for start: ') 
merge_to = input('Type letter for end: ') 
for i in chars: 
    if chars.index(i) >= chars.index(merge_from) and chars.index(i) <= chars.index(merge_to): 
        chars_list.append(i) 
    else: 
        chars_new.append(i) 
str_ = ''.join(chars_list) 
chars_new.insert(chars.index(merge_from), str_) 
print(chars_new) 
"""


#done