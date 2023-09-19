""" Функции """

# nums = [1, 2, 3, 4, 5]
# for num in nums:
#     print(num *2)

# nums2 = ...
# nums3 = ...
# nums4 = ...

""" функция - именованный блок кода, который принимает значения, производит над ними какие-то действия и возвращает результат"""

'определение.создание функции'
# def имя_функции(принимаемые значения/параметры) -> None:
    # тело функции

'вызов функции'
# имя_функции(значения/аргументы)

# параметры - локальные переменные, объявляются при создании функции

# аргументы - значения для функции, передаются при вызове функции. Аргументов может быть столько, сколько у функции параметров

# nums1 = range(1, 10)
# nums2 = range(5, 15)

# def iterate_and_mul(x):
#     for num in x:
#         print(num *2)

# iterate_and_mul(nums1)
# iterate_and_mul(nums2)

# def hello():
#     print('Hello World')

# hello()

""" DRY - Don't Repeat Yourself """
# a =10
# print(10) # Not Good

# def add(x, y):
#     print(x + y)

# add(40, 50)
# add(40) # TypeError (do not have one argument)

""" return - ключевое слово для возвращения результата функции. Является точкой выхода из функции """

# def add(num, num1):
#     return num + num1

# result = add(49, 1)
# print(result)
# res2 = add(3, 5)
# print(res2 + 5)
# print(res2 + result)

# def iterate(nums):
#     for num in nums:
#         print(num)
#     return num *2

# print(iterate([2, 4, 6]))

# def div(x, y):
#     return x / y
#     print('hello world')
#     a = 10
#     print(a)

# print(div(10, 2))

# def iterate_nums(nums):
#     result = []
#     for n in nums:
#         result.append(n * 2)
#     return result

# print(iterate_nums([2, 3, 4, 5]))


""" аннотация типов """

""" # python - динамически типизированный """
# a = 10
# str(10)

""" # python - строго типизированный """
# 10 + 'string' # TypeError

""" # python - неявно типизированный """
# a = 10
# c = []


# def add(a: int, b: int):
    # """ эта функция нужна для сложения чисел """
#     return a + b

# print(add(5, 6))
# print(add('dlfjdlkj', 'sldjfh'))


# def add(a, b=20):
#     """ эта функция нужна для сложения чисел """
#     return a + b

# add(10) # 30
# add(20, 30) # 50


# def func(a, b=10, c): # SyntaxError - параметры со значениями по умолчанию должны быть в конце
#     return a + b + c

# def add_3_nums(a, b, c):
#     return a + b + c
""" 1. Позиционные аргументы """
# add_3_nums(10, 20, 30)
""" 2. Именованные аргументы """
# add_3_nums(a=10, b=40, c=20)
# add_3_nums(b=40, a=10, c=47)
""" 3. Смешанные аргументы """
# add_3_nums(20, 10, c=40) # Ok
# add_3_nums(20, 10, b=40) # Error
# add_3_nums(20, и=10, c=40) # Ok
# add_3_nums(a=20, 10, 40) # Error


""" args, kwargs - arguments, keyword arguments"""
# *args - кортеж позиционных аргументов
# **kwargs - словарь именнованных аргументов

# def func(*args, **kwargs):
#     print(args, 'ARGS')
#     print(kwargs, 'KWARGS')

# func(1, 2, 'hello', 'epta', 30, 'schitayu do tryoh', a1 = 200, b1 = 'heyheyepta')

# def sum_(*nums):
#     counter = 0
#     for i in nums:
#         try:
#             counter += i
#         except TypeError:
#             continue
#     return counter
# print(sum_(1, 3, 4, 5, 'string', 6, 8))


# def func():
#     pass
# # print(dir(func))
# print(type(func))

def is_even(num: int) -> bool:
    return num % 2 ==0

def is_positive(num: int) -> bool:
    return num > 0

from typing import Callable
def operation(*nums, criteria:Callable) -> list:
    result = []
    for num in nums:
        if criteria(num):
            result.append(num)
    return result

print(operation(1, 2, 3, 4, 5, criteria = is_even))
print(operation(1, -7, -3, 4, 2, 7, criteria = is_positive))


# Написать 3 функции, каждая из которых печатает строки вида "Welcome admin/user/moderator"(hello_admin, hello_user, hello_moderator).
# Написать 4 функцию, которая принимает 1 значение (role). 
# Ролей может быть 3 - admin/user/moderator. 4 функция должна вызывать соответствующую роли функцию.
# def hello_user():
#         return 'Welcome user'

# def hello_admin():
#         return 'Welcome admin'

# def hello_moderator():
#         return 'Welcome moderator'

# def role(name):
#     if name == 'user':
#         return hello_user()
#     if name == 'admin':
#         return hello_admin()
#     if name == 'moderator':
#         return hello_moderator()
#     else:
#         return 'no'

# print(role('admin'))

def role_get(role):
    roles = {
        'user': 'hello user',
        'admin': 'hello admin',
        'moderator': 'hello moderator'
    }
    if role in roles:
        return roles.get(role)
    else:
        return 'kiss my ass, goodbye'
    
print(role_get(input('YOUR ROLE: ')))