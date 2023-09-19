""" 1 """
# Создайте функцию add, которая будет принимать 2 числа, складывать их и возвращать результат сложения.
"""
def add(x, y):
    return x + y
"""



""" 2 """
# Создайте функцию get_string_length() которая будет принимать строку. Функция должна возвращать длину этой строки.
"""
def get_string_length(x: str):
    return len(x)
print(get_string_length('hello')) 
"""



""" 3 """
# Создайте функцию: get_type() которая принимает два обязательных параметра. Задача этой функции выводить тип принятых аргументов.
"""
def get_type(num1, num2):
     print(type(num1)) 
     print(type(num2))
get_type(5, 's') 
"""



""" 4 """
# Создайте функцию divide() которая должна принимать 2 числа и возвращать результат их деления.
"""
def divide(x, y):
    return(x / y)
print(divide(5, 10))
"""



""" 5 """
# Создайте переменную dict_ в котором будет хранится словарь. Затем создайте функцию def dictionary()
# которая принимает этот словарь. Пройдитесь по dict_ циклом и распечатайте все его ключи внутри функции.
"""
dict_ = {'first': 1, 'second': 2, 'third': 3}
def dictionary(dict_):
    for x in dict_:
        print(x)

dictionary(dict_)
"""



""" 6 """
# Создайте переменную num = 6. Затем создайте функцию check() которая принимает переменную num в качестве аргумента
# check(num) и возвращает "It is odd number", если это число нечетное и "It is even number" если переданное число четное.
"""
num = 6
def check(x):
    if x % 2 ==0:
        return'It is even number'
    else:
        return 'It is odd number'
print(check(num))
"""



""" 7 """
# Создайте функцию: is_palindrome() которая будет принимать строку и проверить является ли она палиндромом.
# Функция должна возвращать True или False. Пробелы и регистр учитывать не нужно.
"""
def is_palindrome(str):
    if str.upper() == str[::-1].upper().strip(' '):
        return True
    else:
        return False
print(is_palindrome('Kok'))
"""



""" 8 """
# Создайте функцию max_num() которая принимает от пользователя два числа. Она должна сравнить эти числа между собой и вернуть максимальное значение.
"""
def max_num(x, y):
    return max(x, y)
print(max_num(10, 12))
"""



""" 9 """
# Создайте функцию: multiply_list() которая принимает список чисел и возвращает их произведение.
"""
def multiply_list(x):
    multiplied = 1
    for i in x:
        multiplied *= i
    return multiplied
print(multiply_list([1, 2, 3, 4, 5]))
"""



""" 10 """
# Создайте функцию sum_digits() которая принимает целое число и возвращает сумму всех его цифр.
"""
def sum_digits(x):
    num = str(x).strip()
    sum = 0
    for i in num:
        sum += int(i)
    return sum
print((sum_digits(100)))
"""
#or
"""def sum_digits(digit):
    sum_of_digits = 0
    for i in str(digit):
        sum_of_digits += int(i)
    return sum_of_digits
print(sum_digits(5648))"""



""" 11 """
# Создать функцию func11, которая будет принимать 3 числа в качестве аргументов, функция должна возвращать сумму первых двух чисел разделенную на третье число
# нужно реализовать проверку на то, что третье число не является нулем, если это ноль, то просто возвратить результат сложения первого и второго числа
"""
def func11(x, y, z):
    if z != 0: 
        return (x + y) / z
    if z == 0:
        return (x + y)
print(func11(1, 2, 5))
"""



""" 12 """
# Создать функцию func12, которая принимает в качестве аргумента список со строками и в каком регистре нужно вернуть данные, 
# строки могут быть записаны в любом регистре, задача: на основе выбора регистра, возвращать либо список со строками в верхнем регистре, либо в нижнем регистре
"""
def func12(x, y):
    list2 = []
    for i in x:
        if y == 'lower':
            list2.append(i.lower())
        elif y == 'upper':
            list2.append(i.upper())
    return list2
print(func12(['WORD', 'SHELL'], 'lower'))
"""



""" 13 """
# Создать функцию func13, которая будет принимать в качестве аргумента строку, а затем говорить сколько в ней и каких символов, результат вернуть в виде словаря
"""
def func13(str):
    list_ = list(str)
    dict_ = {}
    for i in str:
        dict_.update({i: list_.count(i)})
    return dict_
print(func13('hello'))
"""
#or
"""def func13(string):
    return {i: string.count(i) for i in string}
print(func13('hello'))"""



""" 14 """
# Создайте функцию-менеджер calc, которая будет принимать в себя два числа и операцию. Должны быть доступны операции(+, -, /, *).Создайте также 4 доп.функции -
# add_, sub_, div_, mult_, которые будут принимать в себя два числа. Затем в зависимости от операции calc будет вызывать одну из доп.функций.
# Соответственно, если операция '+', то вызывается функция add_ и т.д.
"""
from typing import Callable
def add_(x, y):
    return x + y

def sub_(x, y):
    return x - y

def div_(x, y):
    return x / y

def mult_(x, y):
    return x * y

def calc(x, y, c):
    
    if c =='+':
        return add_(x, y)
    elif c =='-':
        return sub_(x, y)
    elif c =='*':
        return mult_(x, y)
    elif c =='/':
        return div_(x, y)
print(calc(6, 7, c = '+'))
"""



""" 15 """
# Создайте функцию func15, которая будет рассылать сообщения пользователям, сообщая о акции в магазине компьютерной техники ("name, скидки в магазине компьютерной техники!"), 
# отправлять сообщения нужно только тем людям, которые тем или иным образом относятся к IT-сфере
"""
users = [
     { 'name': 'Jack', 'age': 35, 'work': 'IT-backend developer'},
     { 'name': 'Helen', 'age': 35, 'work': 'Nurse'}, 
     { 'name': 'Bob', 'age': 35, 'work': 'Driver'},
     { 'name': 'Jessica', 'age': 35, 'work': 'IT-frontend developer'},
     { 'name': 'Helga', 'age': 35, 'work': 'IT-HR'}
       ]
def func15(users):
    r=[] 
    for i in users:
         if i['work'].startswith('IT'):
             r.append(f"{i['name']}, скидки в магазине компьютерной техники!\n")
             
    h=''.join(i for i in r) 
    return h 

print(func15(users))
"""
#or
"""def func15(list_):
    string = ''
    for i in list_:
        if i['work'][0:2] == 'IT':
            string +=(f"{i['name']}, скидки в магазине компьютерной техники!\n")
    return string


users = [
  { 'name': 'Jack', 'age': 35, 'work': 'IT-backend developer' },
  { 'name': 'Helen', 'age': 35, 'work': 'Nurse' },
  { 'name': 'Bob', 'age': 35, 'work': 'Driver' },
  { 'name': 'Jessica', 'age': 35, 'work': 'IT-frontend developer' },
  { 'name': 'Helga', 'age': 35, 'work': 'IT-HR' }
]

func15(users)"""



""" 16 """
# Создать функцию func16, которая будет рассчитывать расход топлива автомобиля. Функция будет принимать 2 аргумента: 
# сколько всего километров проехали
# сколько понадобилось топлива на это 
# Затем функция должна рассчитать сколько ушло топлива на 100 км и вернуть результат вида:
# 'На 100км было расходовано n-л горючего' Формула: топливо / расстояние затем функция должна рассчитать сколько ушло топлива на 100 км и вернуть результат вида:
# 'На 100км было расходовано 10л горючего'
"""
def func16(km, fuel):
    tot = (fuel / km)
    res = tot * 100
    return(f'На 100км было расходовано {round(res)}л горючего')

print(func16(100, 50))
"""
#or
"""def func16(total_distance, fuel):
    return f'На 100км было расходовано {round(fuel / total_distance * 100)}л горючего'
print(func16(200, 5))"""



""" 17 """
# Расчет премии сотрудникам salary - это заработная плата в месяц, overTime - количество часов, которое сотрудник взял сверхурочно,
# задача: создать функцию func17, которая будет принимать и добавлять к основной зарплате сверхурочное время(1час=200$),
# функция должна принимать список со словарями и возвращать также список, но уже с измененными данными
"""
def func17(list_: list) -> list:
    new_list = []
    for i in list_:
        i['salary'] = i['salary'] + i['overTime'] *200
        del(i['overTime'])
        new_list.append(i)
    return new_list
employees = [
  {'name': 'Jack', 'salary': 10000, 'overTime': 4},
  {'name': 'Tom', 'salary': 15000, 'overTime': 3},
  {'name': 'Jessica', 'salary': 20000, 'overTime': 9},
  {'name': 'Helen', 'salary': 25000, 'overTime': 2},
  {'name': 'Peter', 'salary': 30000, 'overTime': 7}
]
print(func17(employees))
"""
#or
"""
def func17(list_):
    new_list = []
    for i in list_:
        new_dict = {}
        new_dict.update(i)
        new_dict['salary']= new_dict['salary'] +(new_dict['overTime']*200)
        del new_dict['overTime']
        new_list.append(new_dict)
    return new_list


employees = [
  {'name': 'Jack', 'salary': 10000, 'overTime': 4},
  {'name': 'Tom', 'salary': 15000, 'overTime': 3},
  {'name': 'Jessica', 'salary': 20000, 'overTime': 9},
  {'name': 'Helen', 'salary': 25000, 'overTime': 2},
  {'name': 'Peter', 'salary': 30000, 'overTime': 7}
]

print(func17(employees))
"""



""" 18 """
# Создать функцию func18, которая в качестве аргумента будет принимать список со строками и числами, задача, отсортировать числа в отдельный список,
# а строки в отдельный и распечатать оба списка
"""
def func18(list_: list) -> list:
    int_list = []
    str_list = []
    for i in list_:
        if type(i) is int:
            int_list.append(i)
        elif type(i) is str:
            str_list.append(i)
    return int_list, str_list

print(func18(['hello', 18, 'my', -20, 20, 'dear']))
"""
#or
"""def func18(list_):
    int_list = [i for i in list_ if type(i) is int]
    str_list = [i for i in list_ if type(i) is str]
    return  int_list, str_list

print(func18(['hello', 5, 6, 'dfh4']))
"""



""" 19 """
# Создайте функцию func19, которая будет в качестве аргумента принимать список такого вида как указан ниже,
# и будет возвращать отсортированный список (сортировать по убыванию оценок, используйте sort())
"""
students = [
    {'student': 'Jack', 'marks': 43},
    {'student': 'Tom', 'marks': 92}, 
    {'student': 'Helen', 'marks': 85}, 
    {'student': 'Peter', 'marks': 58}, 
    {'student': 'Jessica', 'marks': 78} 
    ] 
def func19(list_:list): 
    list_.sort(key=lambda x:x['marks'],reverse=True) 
    return list_ 
print(func19(students))
"""



""" 20 """
# Создайте функцию func20, которая будет принимать список и строку, а затем будет смотреть на все товары и возвращать список с теми словарями, 
# у которых в названии(title) есть данная строка. Регистр учитывать не нужно
products = [
  {
    'title': 'Samsung S10', 
    'price': 800, 
    'count': 6, 
    'category': 'samsung'},
  {
    'title': 'iPhone 13 Pro', 
    'price': 1200, 
    'count': 9, 
    'category': 'apple'},
  {
    'title': 'Xiaomi Mi 10', 
    'price': 500, 
    'count': 2, 
    'category': 'xiaomi'},
  {
    'title': 'Samsung S9', 
    'price': 600, 
    'count': 4, 
    'category': 'samsung'},
  {
    'title': 'iPhone 11', 
    'price': 850, 
    'count': 1, 
    'category': 'apple'}
]

"""
def func20(list_, word):
    list1 = []
    for i in list_:
        # for k, v in i.items():
            if word.lower() in i['title'].lower():
                list1.append(i)
    return list1

print(func20(products, 'iph'))
"""
"""def func20(list_, letters):
    new_list = []
    for i in list_:
        if letters.lower()  in i['title'].lower():
            new_list.append(i)
    return new_list
"""
# Используя
products = [
  {
    'title': 'Samsung S10', 
    'price': 800, 
    'count': 6, 
    'category': 'samsung'},
  {
    'title': 'iPhone 13 Pro', 
    'price': 1200, 
    'count': 9, 
    'category': 'apple'},
  {
    'title': 'Xiaomi Mi 10', 
    'price': 500, 
    'count': 2, 
    'category': 'xiaomi'},
  {
    'title': 'Samsung S9', 
    'price': 600, 
    'count': 4, 
    'category': 'samsung'},
  {
    'title': 'iPhone 11', 
    'price': 850, 
    'count': 1, 
    'category': 'apple'}
]



""" 21 """
# Реализовать фильтрацию по категориям Создайте функцию func21, которая в качестве аргумента принимает список и строку с 
# названием категории и возвращает список со словарями, где категория полностью совпадает с переданной
"""
def func21(list_, string_):
    list1 = []
    for i in list_:
            if string_ == i['category']:
                list1.append(i)
    return list1
print(func21(products, 'samsung'))
"""



""" 22 """
# Создать счетчик расходов. Есть некая переменная balance, которая будет хранить данные о вашем балансе, создать две функции, первая spent будет записывать расходы,
# вторая deposit просто пополнять баланс. Первая функция: ее основная задача получать 2 аргумента: на что потрачено, сколько потрачено и текущий баланс,
# дальше формировать словарь типа: {'target': 'Products', 'spend': 400}
# также необходимо реализовать проверку, достаточно ли средств на балансе для совершения расходов и соответственно вычитать из баланса сумму трат.
# Вторая функция просто получает в качестве аргумента сумму, которую нужно добавить на баланс и сам баланс
"""
balance=9_999_999 
def spent(a,b,c): 
    if c-b>=0: 
        c-=b 
        return ({'target':a,'spend':b},c) 
    else: return 'Недостаточно средств' 
print(spent('neger',20000,balance))
def deposit(a,b): 
    b+=a 
    return b
"""



""" 23 """
#     Дан пустой список database, необходимо использовать его в качестве базы данных для словарей типа
# {title: 'str', price: num, category: 'str'}
#     задача реализовать полный CRUD(
#     create(должна быть возможность создавать данные, в нашем случае объекты)
# create(database, title, price, category)
#     read(возможность получения/чтения данных),
# read(database)
#     update(изменение данных(можно использовать индекс)),
# update(database, index, title, price, category)
#     delete(удаление данных(можно использовать индекс))),
# delete(database, index)
#     за каждое действие должна отвечать отдельная функция
"""
database=list() 
def create(db:list,title:str,price:int,category:str)->list: 
    db.append({'title':title,'price':price,'category':category}) 
    return db 

def read(db:list)->list: 
    print(db) 
    return db 

def update(db:list,index:int,title:str,price:int,category:str)->list: 
    db[index]['title']=title 
    db[index]['price']=price 
    db[index]['category']=category 
    return db 

def delete(db,index): 
    db.pop(index) 
    return db
    
"""