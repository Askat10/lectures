""" 1 """
# Присвойте переменной string любую строку.
# Распечатайте первый символ этой строки.
""" 
string = 'hello'
print(string[0]) 
"""



""" 2 """
# Присвойте переменной string любую строку.
# Выведите последний символ этой строки.
"""
string = 'bad boy'
print(string[-1]) 
"""



""" 3 """
# Задайте любую строку переменной string,
# Распечатайте последние 2 символа.
""" 
string = 'world'
print(string[-2:]) 
"""



""" 4 """
# Объявите переменную string со значением в виде любой строки.
# Затем переверните её и распечатайте результат.
""" 
string = 'game'
print(string[::-1]) 
"""



""" 5 """
# Объявите две переменные string1, string2 со значениями в виде любых строк.
# Затем склейте их в одну строку через пробел.
# Выведите получившуюся строку в терминал.
""" 
string1 = 'hello'
string2 = 'world'
print(string1 + ' ' + string2) 
"""



""" 6 """
# Объявите переменную string со значением в виде любой строки.
# Продублируйте ее 4 раза.
# Распечатайте результат.
""" 
string = 'jordan'
print(string * 4) 
"""



""" 7 """
# Объявите переменную string со значением в виде любой строки.
# Выведите её длину в консоль.
""" 
string = 'peace'
print(len(string)) 
"""



""" 8 """
# Создайте переменную string со значением 'The quick brown fox jumps over the lazy dog'.
# Замените все повторения буквы o символом * и сохраните результат в новой переменной.
# Распечатайте новую переменную.
""" 
string = 'The quick brown fox jumps over the lazy dog'
new = (string.replace('o', '*'))
print(new) 
"""



""" 9 """
# Создайте переменную string со значением в виде любой строки.
# Переведите все её символы в верхний регистр.
# Распечатайте результат.
""" 
string = 'lower'
print(string.upper()) 
"""



""" 10 """
# Объявите переменную string со значением в виде любой строки.
# Переведите все её символы в нижний регистр.
""" 
string = 'CAPSWORD'
print(string.lower()) 
"""



""" 11 """
# Создайте переменную string со значением в виде любой строки.
# Обменяйте местами первый и последний символы и выведите результат в консоль.(ваш код должен работать со строками любой длины)
""" 
string = 'change'
print(string[-1] + string[1:-1] + string[0]) 
"""



""" 12 """
# Создайте переменную hashtags в которой будет хранится строка из хештэгов, то есть слов разделенных символом #.
# Разделите их в отдельные строки.
""" 
hashtags = 'f#o#o#t#b#a#l#l'
print(hashtags.split('#')) 
"""



""" 13 """
# Создайте переменные name(имя), last_name(фамилия), age (возраст) и city(город), значения которых вы будете получать от пользователей из функции input().
# Во вкладке INPUT введите значения для переменных name(имя), last_name(фамилия), age (возраст) и city(город).
# С помощью f-строк выведите краткую информацию о человеке.
""" 
name = input('enter the name: ')
last_name = input('enter the last name: ')
age = input('enter the age :')
city = input('enter the city: ')
print(f'Вас зовут {name} {last_name}, Ваш возраст: {age}, Вы проживаете в городе {city}') 
"""



""" 14 """
# Создайте переменную string со значением в виде любой строки.
# Выведите только символы с нечётными индексами при помощи срезов.
""" 
string = 'any string'
print(string[1::2]) 
"""




""" 15 """
# Объявите переменную string со значением в виде любой строки.
# Поменяйте шестую букву на K.
""" 
string = 'some word'
string = string[:5] + 'K' + string[6:] 
print(string)
"""



""" 16 """
# Объявите переменную string со значением в виде любой строки.
# Переведите все её символы в противоположный регистр и распечатайте результат.
""" 
string = 'wHaTsUp'
print(string.swapcase()) 
"""



""" 17 """
# Объявите переменную string со значением в виде любой строки.
# Размножьте строку три раза, при этом каждое повторение должно быть на новой строке, необходимо использовать экранирование.
""" 
string = 'just word'
print((string + '\n') * 3) 
"""



""" 18 """
# Объявите переменную string со значением в виде любой строки.
# Необходимо найти индекс буквы 'e'.
""" 
string = 'hello world'
print(string.index('e')) 
"""



""" 19 """
# Объявите переменную string со значением в виде любой строки.
# Необходимо проверить начинается ли ваша строка с подстроки "Python" (Регистр должен учитываться). Вывод: True/False
""" 
string = 'hello USA'
print(string.startswith('Python')) 
"""



""" 20 """
# Объявите переменную string со значением в виде любой строки.
# Проверьте состоит ли ваша строка полностью из чисел. Вывод: True/False
""" 
string = 'hello guys'
print(string.isdigit()) 
"""



""" 21 """
# Объявите переменную string со значением в виде любой строки, используя пробел.
# Разделите строку по разделителю (пробелу) чтобы получился список.
""" 
string = 'hello world and my life'
print(string.split()) 
"""



""" 22 """
# Объявите переменную string значением которой будет input().
# Выведите ее значение используя интерполяцию строк 
""" 
string = input('enter the word: ')
print(f'Hello {string}') 
"""



""" 23 """
# Объявите переменные string1 и string2 со значением в виде любой строки.
# Выведите значение данных переменных используя интерполяцию строк.
""" 
string1 = 'hello'
string2 = 'my dear'
print(f'{string1} {string2}') 
"""



""" 24 """
# Даны две переменные string1 = "America" и string2 = "Japan".
# Выведите новую строку в который будут записаны первый, средний и последний элемент двух переменных.
# Необходимо использовать срезы.
""" 
string1 = "America" 
string2 = "Japan"
print(string1[0]+string2[0]+string1[len(string1)//2]+string2[len(string2)//2]+string1[-1]+string2[-1]) 
"""



""" 25 """
# Дана переменная string, содержащая пробелы в начале и в конце. Распечатайте строку без пробелов и выведите количество символов в строке без пробелов.
""" 
string = '    it is my life    '
a = (string.strip())
print(f'{a}\n{len(a)}') 
"""



""" 26 """
# Дана переменная string, с текстом "cow loves good milk".
# Замените в ней только первые две буквы o на e
""" 
string = "cow loves good milk"
print(string.replace('o', 'e', 2)) 
"""