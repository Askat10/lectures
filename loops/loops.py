""" Циклы for и while """

names = ['Azat', 'Timurlan', 'Marat']
# print(len(names[0]))
# print(len(names[1]))
# print(len(names[2]))

# for name in names:
#     print(len(name))

# for промежуточная_переменная in iterable_obj:
    # тело цикла

data_types = [
    int,
    str,
    list,
    bool,
    None,
    tuple,
    set,
    dict,
]
# print(dir(list))
# iter_objs = []
# non_iter_objs = []
# for type_ in data_types:
#     if'__iter__' in dir(type_):
#         iter_objs.append(type_)
#     else:
#         non_iter_objs.append(type_)
# print(iter_objs)
# print(non_iter_objs)


# nums = [10, 20, 30]



# # range()
# for i in range(11):
#     print(i)

# nums = range(5, 20, 2)
# for i in nums:
#     print(i)


    # Циклы - многократное выполнение определенного участка кода

    # Итерация - процесс повторения действия

    # итерируемый обьект - тот обьект, к которому применим цикл for

    # for - цикл, который работает до тех пор, пока в iter_obj не кончатся элементы




""" while """

# while условие
#  while - цикл, который работает до тех пор, пока условие возвращает True

# condition = 10 > 3
# # while condition is True: # Ok
# while condition:
#     print('Hello World')

# counter = 0
# while counter < 5:
#     print('hello world')
#     # counter = counter + 1
#     counter += 1

# for i in range(5):
#     print('Hello World')


""" break, continue """
# string = 'ABCDEFG'
# for letter in string:
#     if letter == 'D':
#         break
#     print(letter)

# for i in string:
#     break

# for letter in string:
#     if letter == 'D':
#         continue
#     print(letter)


# for letter in string:
#     if letter == 'D':
#         pass
#     else:
#         print(letter)



# msg = input('write the message: ')
# while msg != 'stop':
#     print(f'your message: {msg}')
#     msg = input('write the message: ')


# while True:
#     msg = input('Enter the message: ')
#     if msg == 'stop':
#         break
#     print(f'your message is: {msg}')


""" else в циклах"""
# for i in range(10):
#     print(i)
# else:
#     print('cycle was stopped')

# for i in 


# black_list = ['Don', 'Valera', 'Maksat']
# guests_q = 5
# while guests_q > 0:
#     name = input('Enter the guests name: ')
#     if name in black_list:
#         print('you are not allowed')
#         continue
#     guests_q -= 1
# else:
#     print('Party is STARTING!!!')


# string = 'apple'
# for i in string:
#     print(i)


# counter = 0
# while counter!= len(string):
#     print(string[counter])
#     counter +=1


# += - инеремент
# -= - декремент