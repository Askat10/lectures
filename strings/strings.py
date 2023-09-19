""" strings (строки) """

# str()

# string - неизменяемый, упорядоченный, индексируемый, итерируемый тип данных

# string = 'me string'
# string2 = "my string"

# # string = 'I'm student' #Error
# string4 = "I'm student"  #Ok
# string5 = 'I\'m student' #Ok
# string6 = 'Он сказал:"I\'m student"' #Ok
# \ - символ экранирования

doc_string = """
Очень длинный
супер длинный 
текст
"""
doc_string2 = '''
Длинная 
строка
документации
'''

# +, *
# print('Hello' + 'world') # Helloworld
# print('Hello' + ' ' + 'world') # Hello world
# print('Hello ' + 'world') # Hello world
# print('Hello' + ' world') # Hello world
# Конкатенация - процесс склеивания строк

# print('Hello' * 3) # HelloHelloHello

#immutable string
# str1 = 'apple'
# str1 + 'potato'
# print(str1) # apple

"""Функции и методы строк"""
# print() - функция всех 

string1 = 'Room'
# string1.capitalize()

# len() - возвращает длину obj
# print(len(string1)) #4
# len_of_string = len(string1)

# dir(obj) -возвращает список доступных методов obj
# print(dir('apple'))

# Метод - функция, которая принадлежит определенному типу данных и может быть вызвана только через него  # (obj.some_method())

my_str = 'Hello world 1^'
# print(my_str.lower())(
# print(my_str.upper())
# print(my_str.swapcase())

# print('artur'.capitalize())
# print('artur kanat'.capitalize())
# print('artur kanat'.title())

print('apple,potato,carrot'.split(','))
# print('apple potato carrot'.split())

# print('korova'.replace('o', '*'))

# print(' password    '.strip())
# print('***superslim***'.strip('*'))
# print('   string('.lstrip())
# print('string   '.rstrip())

# print('korova'.count('o(')) #2

string = 'some string with 5 words'
# print(string.isdigit()) #False
# print('654'.isdigit()) #True
# print(string.isalpha()) #False
# print('apple'.isalpha()) #True
# print(string.isalnum()) #False
# print('apple654'.isalnum()) #True
# print(string.startswith('so')) #True
# print(string.endswith(i(ng)) #False

# print(string.fin(d('m')) #2
# print(''.join(['apple', 'potato', 'carrot'])) #applepotatocarrot

""" Индексы и срезы """
# Индекс - порядковый номер элемента в строках/списках/кортежах/ В программировании индексация начинается  с нуля
# 'hello'
# 0 1 2 3 4
# -5 -4 -3 -2 -1(

string = 'keyword'
# print(string[3]) #w
# print(string[-1]) #d

string = 'some long string'
# print(string[0:4]) #some
start = 5
stop = 9
# print(string[start:stop]) #long
# print(string.replace('long', '')[0:]) #some string
# print(string[0::(step])
# print(string[0::-1])

""" Форматирование строк """
name = 'Azamat'
inv1 = '%s , пригл(ашаю тебя на свадьбу!' % (name)
# print(inv1)
inv2 = '{a}, приглашаю тебя на свадьбу!'.format(a = name)
# print(inv2)string1 = "America" string2 = "Japan" print(string1[:1] + string2[:1] + string1[int(len(string1)/2)] + string2[int(len(string2)/2)] + string1[-1] + string2[-1])
inv3 = f'{name}, приглашаю тебя на свадьбу!'
# print(inv3)

""" Символ экранирования """
path_to_file = 'C\\users\\new_folder'
# print('hello\nworld')
# print('hello\tworld')
# print('hello\n\tworld')
# print(path_to_file)


















# string1 = "America" 
# string2 = "Japan" 
# print(string1[:1] + string2[:1] + string1[int(len(string1)/2)] + string2[int(len(string2)/2)] + string1[-1] + string2[-1])












# string = 'cow loves good milk'
# print(string[0:9].replace('o', 'e') + string[9:])

# string = 'cow loves good milk' 
# print(string.replace('o','e', 2 ))