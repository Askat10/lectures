# numbers1 = []
# numbers2 = list()
# print(type(numbers1))
# print(type(numbers2))

# numbers4 = [1, 2, 3, 4]
# numbers5 = list(numbers4)
# numbers6 = list(['makers', 'hello'])
# print(type(numbers5))

# numbers = [7, 7, 7, 7, 7, 7]
# numbers2 = [7] * 6
# print(numbers)
# print(numbers2)

""" range() """

#1. range(end)
# numbers = list(range(10))
# print(numbers)

#2. range(start, end)
# numbers = list(range(1, 10))
# print(numbers)

#3. range(start, end, step)
# numbers = list(range(1, 10, 2))
# print(numbers)
# numbers = list(range(10, 0, -3))
# print(numbers)


# for i in range(1, 11): # -> 1,2,3,4,5,6,7,8,9,10 заходят в i
#     print(i **2)
#     print(i + 1)

""" сравнение списков """
# numbers1 = [1, 2, 3, 4, 5, 11]
# numbers2 = [1, 2, 3, 4, 5, 9, 100, 999999]
# print(numbers1 > numbers2)

# сравнение списков производится по индексу и заканчивая с наименьшим количеством символов

""" Индексация """
# numbers = [1, True, 'Makers', 'hello', 8.9, (1,2), ['hello']]
# print(numbers[7])
# print(numbers[0])
# print(numbers[2])
# print(numbers[4])
# print(numbers[-1])
# print(numbers[-2])
# print(numbers[-3])

""" Изменение списка """
# numbers = [1, True, 'Makers', 'hello', 8.9, (1,2), ['hello']]
# numbers[3] = 'Bootcamp'
# numbers[-1] = {1: 'a'}
# numbers[7] = False
# print(numbers)

# users = ['Alice', 'Sam', 'Carol']
# for user in users:
#     print('Hello '+user)

# for letter in 'Makers':
#     print(letter.title())

""" Методы списков """

# append(element)
# users = ['Alice', 'Cat', 'Billy']
# print(users)
# user = 'Tom'
# users.append(user)
# users. append('John')
# print(users)

# guests = []
# list_length = int(input('Enter number of guests: '))

# for names in range(list_length):
#     print(guests)
#     guest = input('Enter guest name: ')
#     guests.append(guest)
# print(guests)


#extend(list)

# users1 = ['Alice', 'Sam']
# users2 = ['Bob', 'Tom']
# users1.extend(users2)
# print(users1)
# print(users2)

# users2.extend(['John', 'Harlow'])
# print(users2)

# print(users1 + users2)

# insert(index, element)

# users = ['John', 'Lenny', ' Andy', 'Anna']
# print(users)
# users.insert(1, 'Rachel')
# print(users)

#remove(element)

users = ['Sam','Cat', 'Carol', 'Cat']
# users.remove('Cat')
# print(users)
# # users.remove('Rachel')
# if 'Rachel' in users:
#     users.remove('Rachel')
# else:
#     print(users)

#clear()

# users = ['Sam', 'Cat','Carol']
# print(id(users))
# users.clear()
# print(id(users))

# del users
# print(users)

# index(element)

# list = ['hello', 'makers', True, 6]
# print(list.index(6))

# pop(index), default - pop(-1)

# numbers = [1, 2, 3, 4, 5]
# number = numbers.pop(3)
# number2 = numbers.pop()
# print(numbers)
# print(number)
# print(number2)

# count(element) 
# numbers = [2, 4, 2, 2, 6, 8, 0, 2, 2, 4, 5, 6, 7, 9]
# users = ['Alice', 'Bob', 'Alice']
# print(numbers.count(3))
# print(users.count('Alice'))

# sort(key)

# users = ['Alice', 'Tom', 'Cat', 'Ann', 'Rachel']
# users.sort(key = len)
# print(users)

#reverse()
# users = ['Alice', 'Tom', 'Cat', 'Ann', 'Rachel']
# users.reverse()
# print(users)

#copy()

# users1 = ['Tom', 'Bob', 'Ann']
# users2 = users1
# users3 = users1.copy()
# print(id(users1))
# print(id(users2))
# print(id(users3))

# users1.pop()
# print(users1)
# print(users2)
# print(users3)

""" Функции """

# len()
# numbers = [1, 2, 3, 4, 5, 6, -3, -5]
# print(len(numbers))

# max(), min()
# numbers = [4, 1, 6, 8, 9, 0, -6]
# print(max(numbers))
# print(min(numbers))

# sum()
# numbers = [4, 1, 6, 8, 9, 0, -6]
# print(sum(numbers))

# sorted()
# numbers = [4, 4, 7, 9, 4, 5, 1, 4, 2, 4, 3, 7, 8, 9, 6, 7, 4]
# print(sorted(numbers))
# print(numbers)

""" Срезы / Slices """
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#list[x:y]
# print(my_list[1:4])
# print(my_list)
# my_list = my_list[1:4]
# print(my_list)
#list[x:y:z]
# print(my_list[2:-1:2])


# users =[
#     ['Name', 'Age'],
#     ['Tom', 23],
#     ['Bob', 34],
#     ['Emily', 18]
# ]
# print(users[1][0][1])
# # print(users[1])
# # print(users[2])

# for list_ in users:
#     for element in list_:
#         print(element, end = '|')
#     print()

# if int('1') == int:
#     print('yes')
# else:
#     print('no')
# print(('1'))

