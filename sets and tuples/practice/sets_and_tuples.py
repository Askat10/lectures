""" 1 """
# Создайте множество в переменной a и распечатайте его.
""" 
a = {1, 2, 'a', 'b', (1, 'a')}
print(a) 
"""



""" 2 """
# Создайте множество a и выведите его длину.
""" 
a = {1, 2, 'a', 'b', (1, 'a')}
print(len(a)) 
"""



""" 3 """
# Создайте множество a. Добавьте в него строку 'Hello world!'. Распечатайте результат
""" 
a = {1, 2, 'a', 'b', (1, 'a')}
a.add('Hello world!')
print(a) 
"""



""" 4 """
# Создайте два множества a и b. Добавьте к множеству a множество b. Распечатайте результат.
""" 
a = {1, 2, 'a', 'b', (1, 'a')}
b =  {1, 2, 3}
a.update(b)
print(a) 
"""



""" 5 """
# Создайте множество a и попробуйте удалить один из элементов. Используйте такой метод, который не будет выдавать ошибку, если такого элемента нет. Распечатайте результат
""" 
a = {1, 2, 'a', 'b', (1, 'a')}
a.discard('asldfkjfjjf')
print(a) 
"""



""" 6 """
# Создайте множество a и попробуйте удалить один из элементов. Используйте такой метод, который будет выдавать ошибку KeyError, если такого элемента нет. Распечатайте результат.
""" 
a = {1, 2, 'a', 'b', (1, 'a')}
a.remove('asldfkjfjjf')
print(a)  
"""



""" 7 """
# Создайте множество a и удалите все элементы определённым методом. Распечатайте результат.
""" 
a = {1, 2, 'a', 'b', (1, 'a')}
a.clear()
print(a)   
"""



""" 8 """
# Даны два множества a и b. С помощью определенного метода или оператора, найдите пересечение множеств. Распечатайте результат
""" 
a = {1, 2, 'a', 'b', (1, 'a')}
b = {1, 2, 3, 4, 5, (1, 'a,'), (1, 2)}
intersection_set = a.intersection(b)  #  &
print(intersection_set) 
"""



""" 9 """
# Создайте два множества a, b. С помощью определенного метода или оператора найдите разницу множеств. Распечатайте результат.
""" 
a = {1, 2, 'a', 'b', (1, 'a')}
b = {1, 2, 3, 4, 5, (1, 'a,'), (1, 2)}
differenced_set = a.difference(b)  #  -
print(differenced_set) 
"""



""" 10 """
# Создайте два множества в переменных a, b. С помощью определенного метода или оператора объедините множества. Распечатайте результат.
""" 
a = {1, 2, 'a', 'b', (1, 'a')}
b = {1, 2, 3, 4, 5, (1, 'a,'), (1, 2)}

c = a.union(b)   # |
print(c) 
"""



""" 11 """
# Создайте два множества a и b. Если первое множество является подмножеством второго, распечатайте строку 'Подмножество!'.
""" 
a = {1, 2, 'a', 'b', (1, 'a')}
b = {1, 2, 3, 4, 5, (1, 'a,'), (1, 2)}
if a.issubset(b):
    print('Подмножество!') 
"""



""" 12 """
# Создайте два множества a и b. Если первое множество является надмножеством второго, распечатайте строку 'Надмножество!'.
""" 
a = {1, 2, 'a', 'b', (1, 'a')}
b = {1, 2, 3, 4, 5, (1, 'a,'), (1, 2)}
if a.issuperset(b):
    print('Надмножество!') 
"""



""" 13 """
# Роберт загадал пять чисел. Используя методы множеств, напишите код определяющий, кто из перечисленных ниже людей угадал хотя бы одно число из загаданных Робертом.
# Если есть хотя бы одно число, которое угадал kail и хотя бы одно число, которое угадала merri, вывод должен быть: "kail merri"
# Если же только один из них угадал, то запринтите имя того, кто угадал. Если же никто не угадал заданное число, выведите строку: no one
""" 
robert = {5, 7, 11, 10, 28} 
kail = {1, 14, 8, 22} 
merri = {19, 20, 3}
if robert & kail != set() and robert & merri != set():
    print("kail merri")
elif robert & kail != set():
    print('kail')
elif robert & merri != set():
    print('merri')
else:
    print('no one') 
"""



""" 14 """
# Четверо коллег tilek, timur, alexander, elina собрались на обед.
# Но они не могут решить, где им пообедать, так как у каждого свои вкусовые предпочтения. Помогите найти им выход в данной ситуации.
# Данные:
#     Тилек хочет покушать в "Dodo" или в "ImperiaPizza", ну или в крайнем случае "FreshBox".
#     Тимур хочет покушать шашлык в "OchakKebab" или рамен в "FreshBox".
#     Александр очень хочет вафли с "FreshBox" либо "KFC".
#     Элину устраивает любой из вариантов.
""" 
tilek = {"Dodo", "ImperiaPizza", "FreshBox"}
timur = {"OchakKebab", "FreshBox"}
alexander = {"FreshBox", "KFC"}
elina = {"Dodo", "ImperiaPizza", "FreshBox", "OchakKebab", "KFC"}
a = tilek & timur & alexander & elina
print(a) 
"""



""" 15 """
# Имеется пицца, ингредиенты которой помещены во множество ingredients.
# Используйте методы множеств, чтобы проделать все действия.
# Ингредиенты:
# ingredients = {"cыр чеддар","грибы", "соус","шпинат"} 
# Действия:
#     Добавьте "помидор" в данное множество.
#     Уберите ингредиент "колбаса" (если она есть!).
#     Уберите ингредиент "шпинат" (методом который вызовет ошибку если его нет).
#     Вместо шпината добавьте "базилик".
#     Замените "сыр чеддар" на "сыр моцарелла".
#     Распечатайте множество ingredients.
""" 
ingredients = {"cыр чеддар","грибы", "соус","шпинат"} 
ingredients.add('помидор')
ingredients.discard('колбаса')
ingredients.remove('шпинат')
ingredients.add('базилик')
ingredients.discard('сыр чеддар')
ingredients.add('сыр моцарелла')
print(ingredients) 
"""



""" 16 """
# Создайте переменную a в которой будет хранится список из 3 пустых множеств. От пользователя, вы получаете строку Hello world, которую надо сохранить в переменной inp1.
# Также, вы получаете число, от 1 до 3, которое нужно сохранить в переменную inp2. Число 1 соответствует первому множеству в списке a, число 2 второму, а 3 третьему.
# В зависимости от переданного числа, сохраните строку в inp1, в одно из пустых множеств внутри списка a. В остальные множества добавьте строку "default value".
# В конце, выведите получившийся список. Например, если пользователь ввел Hello world и 1, то вывод:
# [{'Hello world'}, {'default value'}, {'default value'}]
# Для проверки кода, введите строку Hello world и число в поля во вкладке INPUT.
""" 
a = [set(), set(), set()]
inp1 = input()
inp2 = int(input())

if inp2 ==1:
    a[0].add(inp1)
    a[1].add('default value')
    a[2].add('default value')
elif inp2 ==2:
    a[1].add(inp1)
    a[0].add('default value')
    a[2].add('default value')
elif inp2 ==3:
    a[2].add(inp1)
    a[1].add('default value')
    a[0].add('default value')
else:
    a[2].add('default value')
    a[1].add('default value')
    a[0].add('default value')

print(a) 
"""



""" 17 """
# Создайте два множества set1 и set2 используя comprehensions. В set1 должны хранится четные значения (в диапазоне от 0 до 10) В set2 нечетные (в диапазоне от 0 до 10)
# Так же необходимо проверить с помощью специального метода пересекаюся они или нет. Если пересекаюся вывести Множества пересекаются!, если же нет Множества не пересекаются!
""" 
set1 = {i for i in range(10) if i%2==0}
set2 = {i for i in range(10) if i%2!=0}
if set1 & set2:
    print('Множества пересекаются!')
else:
    print('Множества не пересекаются!') 
"""