""" Исключения и ошибки """

# исключение - проблема в логике работе кода
# ошибка - проблема в написании кода


# Exception - родитель исключений

# a = 10
# b = 30
# print(c)
NameError # исключение имени


# 10 / 0
ZeroDivisionError # деление на ноль


# nums = [1, 2, 3]
# nums[78]
IndexError # исключение индекса


# names = {'ben': 10, 'josh': 5}
# names['tom']
KeyError # исключение ключа


# num = 10
# num + 'string'
TypeError # исключение типов данных, когда тип данных не подходит для операции


# num = '10'
# int(num) # OK
# int(20) # OK
# int(10.05) # OK
# int('string') 

# from math import sqrt
# sgrt(25) # 5
# sqrt(-20) 
ValueError # когда тип данных подходит для операции, но значение - нет


# string = 'string'
# string.append('a')
AttributeError # исключение атрибута(метода) у объекта


# import math # OK
# import maz
ModuleNotFoundError 
# from math import wrong_func
ImportError


""" Ошибки """
SyntaxError # ошибка синтаксиса
# for i in range(10)
#     print(i)


IndentationError # ошибка отступов
# for i in range(10):
# print(i)


KeyboardInterrupt # Ctrl + C 
# while True:
#     print(12)



""" try except """
# contacts = {
#     'jane': 996704565575,
#     'john': 856987334498
# }
# print('contacts saved')
# contacts['ben']
# print('Hello World')
# print(2 + 2)

# contacts = {
#     'a': 99948,
#     'b': 4893490
# }
# try:
#     contacts['c']
# except:
#     print('нет такого ключа')
# print('hello world')
# print(2 + 2)

# try: # выполняет код с потенциальным исключением
#     print('some code')
#     10/ 0
# except: # отлавливает исключение из блока try
#     print('что-то пошло не так')
# else: # срабатывает, если try прошел без исключении
#     print('try прошел без ошибок')
# finally: # код, который сработает в любом случае
#     print('сработаю в любом случае')


"""
исключения обрабатываются с помощью try-except, а ошибки - нет
"""

# try:
#     ...
# except: # голое исключение
#     ...

nums = [1, 2, 3]
# try:
#     nums [10]
#     print(c)
# except:
#     print('что-то пошло не так')

# try:
#     print(c)
#     nums[10]
# except IndexError:
#     print('неверно указан индекс')
# except NameError:
#     print('неправильная переменная')

# try:
#     a = 10
#     a / 0
#     a.upper()
# except(ZeroDivisionError, AttributeError):
#     print('Деление на ноль или ошибка атрибута')



# try:
#     10 / 0
# except Exception as error:
#     print(error)

""" raise """
# raise - ключевое слово для поднятия/вызова исключении
# money = 0
# if money == 0:
#     raise ValueError('Недостаточно средств')

# try:
#     raise ValueError('ERROR!')
# except ValueError as e:
#     print(e)


# contacts = {'Aidai': 996705698349, 'Aliya': 996707247644}
# try:
#     name = input('Введите имя').title().strip()
#     print(f'Звоним {contacts[name]}')
# except KeyError:
#     print('Нет такого имени')
# finally:
#     print('Программа завершила работу')


# contacts = {'Aidai': 996705698349, 'Aliya': 996707247644}
# name = input('enter the name ').title()
# if name not in contacts:
#     print('Нет такого имени')
# else:
#     print(f'Звоним {contacts[name]}')


# count = 0
# while True:
#     try:
#         num = int(input('Enter the number'))
#         count += num
#     except ValueError:
#         print('enter just numbers')
#     finally:
#         print(count)
#         if count > 49:
#             raise Exception('Число достигло максимума')


