""" Условные выражения """
# if условие : 
#     действие, если условие1 Истина
# else:
#     действие, если if не сработал

    # bool() - неизменяемый, имеет всего 2 значения - True/False

    # num1 = 10
    # num2 = 5
    # num1 > num2 # True
    # num1 < num2 # False
    # num1 == num2 # False
    # num1 != num2 # True
    # num1 >= num2 # True
    # num1 <= num2 # False

    # print(bool(1)) # True
    # print(bool(0)) # False

    # if bool()

    # print(bool('hello')) # True
    # print(bool('')) # False
    # bool([])
    # bool({})
    # bool(0)
    # bool(None)

""" if """
# temp = 20
# if temp > 15:
#     print('Warm')

# temp = 20
# if temp < 15:
#     print('Cold')
# else:
#     print('Warm')


# temp = 25
# if temp < 15:
#     print('Cold')
# elif temp == 25:
#     print('Perfect')
# else:
#     print('Hot!')

# num2 = 10
# if num == 10:
#     print('ok')
# if num > 5:
#     print('ok2')

# if 'hello':
#     print('it works')

# if bool('hello') == True:
#     print('it works')

""" and, or, not """
# age = 20
# if age >18 and age <40:
#     print('Доступ разрешен')
# else:
#     print('Доступ запрещен')

False # False
True # True
False and False # False
True and True # True
True and False # False
False and True # False
# условие and условие2 - оператор and требует, чтобы оба условия были True, иначе False




# условие or условие2 - or требует, чтобы хотя бы одно условие было True
False or False # False
True or True # True
False or True # True
True or False # True



not True # false
not False # True

(True and False) or (False or True) # True
(True and False) and (False or True) #False

""" ==, is """
# a = 1000
# b = 1000
# print(a == b)
# print(a is b)

# print(id(a))
# print(id(b))

""" in """
# коллекции: списки, словари, кортежи, строки, множества
# string = 'potato'
# print('t' in string) # True

# in - проверка на вхождение какого либо элемента на какие либо данные

""" Тернарный оператор """
# # действие if условие else действие2
# num = 10
# result = 'num >10' if num >=10 else 'num < 10'
# print(result)

# login = 'my_username123'
# password = 'mySuperPassword123'
# if input('Введите логин ') == login and input('Введите пароль ') == password:
#     print('Welcome')
# else:
#     print('Неправильный логин или пароль')

""" Сравнение строк, таблица ASCII """
# print('Hello' > 'hello')   # сравнивает с ASCII
# print(ord('A'))   # Порядковый номер в ASCII
# print(chr(72))   # Cимвол находящееся под 72 номером в ASCII








# num = int(input())
# meaning = chr(num)
# l = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'Y', 'W', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
# if chr(num) in l:
#     print('это буква', meaning)
# else:
#     print('это не буква, а символ', meaning )






#     num = chr(int(input()))
#     if num.isalpha():
#          print(f'Это буква "{num}"') 
#     else:
#          print(f'Это не буква, а символ "{num}"')










# count = 1
# number = int(input())
# count = count + number
# if number is int():
#     print(count)
# else:
#     pass




# count = 0
# number = input()

# if number.isdigit():
#     number = int(number)
#     count = number
# print(count)


# lang = 'en'
# if lang == 'en':
#     print('This is english')
# elif lang == 'ru':
#     print('Это русский')
# elif lang == 'de':
#     print('Das ist Deutsch')
# elif lang == 'kg':
#     print('Бул кыргыз тили')



# string = str(123456)
# start = int(string[1] + string[2] + string[0])
# last = int(string[-1] + string[-2] + string[-3])
# if start == last:
#     print('да')
# else:
#     print('нет')





# a = int(input())
# b = int(input())
# c = int(input())
# if a >= b and a >= b and b >= c:
#     print(c, b, a)
# elif a<=b and a>=c:
#     print(c, a, b)
# elif a <= b and a <= c and b <= c:
#     print(a, b, c)
# elif c >= a and a >= b:
#     print(b, a, c)
# elif a >= c and c >= b:
#     print(b, c, a)
# else:
#     print(a, c, b)






# month = int(input('type month'))
# if month > 12 or month == 0:
#     print('Такого месяца нет')
# elif month == 2 or month ==1  or (month == 12):
#     print('зима')
# elif month > 2 and month < 6:
#     print('весна')
# elif month > 5 and month <9:
#     print('лето')
# elif month > 8 and month < 12:
#     print('осень')

