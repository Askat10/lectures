""" comprehensions(генераторы) """

# list_ = []
# for i in range(11):
#     list_.append(i)
# print(list_)

# list1 = [i for i in range(11)]
# print(list1)

# comprehensions - короткий и быстрый способ создания коллекций
  
# пустой_список = []
# for переменная in итерируемый_объект:
#     пустой_список.append(переменная + 10) # выражение

# синтаксис_генератора = [переменная +10 for переменная in итерируемый объект]

""" list comprehensions """

# 1) добавить в список числа от 1 до 10
# list_ = []
# for i in range(1, 11):
#     list_.append(i)
# print(list_)

# list2 = [i for i in range(1, 11)]
# print(list2)

# добавить в список числа от 1 до 10, при этом каждое число умнжить на 2

# nums = [i *2 for i in range(1, 11)]
# print(nums)

# nums2 = []
# for i in range(1, 11):
#     nums2.append(i * 2)
# print(nums2)

# 3 добавить в список число из диапазона от 1 до 20, только четные без range
# list1 = []
# for i in range(1, 21):
#     if i %2 ==0:
#         list1.append(i)
# print(list1)

# list1 = [i for i in range(1, 21) if i % 2 == 0]
# print(list1)

# синтаксис_с_условием = [переменная for переменная in итерируемый_объект if условие]

# 4) добавить в список числа от 1 до 10, при этом к четным добавлять 100, к нечетным по 400
"""
list2 = []
for i in range(1, 11):
    if i % 2 == 0:
        list2.append(i+100)
    else:
        list2.append(i+400)
print(list2)

nums1 = []
for i in range(1, 11):
    nums1.append(i +100 if i %2 == 0 else i + 400)
print(nums1)
"""
"""
nums2 = [i +100 if i % 2 == 0 else i + 400 for i in range(1, 11)]
"""
# Тернарный оператор
"""
действие if условие == True else действие2
"""
#  синтаксис_с_двумя_условиями = [тернарный_оператор for переменная in итерируемый_объект]

# 5) Добавить в список числа от 1 до 50, при этом к четным добавить 100 к нечетным 400, но при этом работать с числами кратными 3
# list1 = []
# for i in range(1, 51):
#     if i % 3 ==0:
#         if i % 2 == 0:
#             list1.append(i +100)
#         else:
#             list1.append(i + 400)
#         #nums.append(i + 100 if i % 2 == 0 else i + 400)
# nums1 = [i + 100 if i % == 0 else i + 400 for i in range(1, 51) if i % 3 ==0]


# a = 10
# nums = a+ 10 if a> 5 else 0 if a %2 ==0 else a- 10 if a <10 else 1
# print(nums)

""" dictionary comprehensions """
names = {
    'bakyt': 20,
    'nurbek': 30,
    'kanat': 21
}
# new_names = {}
# for k, v in names.items():
#     new_names.update({k: v+1})
# print(new_names)

# new_names2 = {k: v+1 for k, v in names.items()}
# print(new_names2)

names = {
    'bakyt': 20,
    'nurbek': 30,
    'kanat': 21
}
# reversed_names = {}
# for k, v in names.items():
#     reversed_names.setdefault(v, k)
# print(reversed_names)

# reversed_names2 = {value: key for key, value in names.items()}
# print(reversed_names2)

""" вложенности """
# nums = []
# for i in range(1, 11):
#     for j in range(1, 3):
#         nums. append((i, j))
# print(nums)

# nums2 =[(i, j) for i in range(1, 11) for j in range(1, 3)]
# print(nums2)


# nums3 = [[i for i in range(1, 10)] for x in range(1, 6)]
# print(nums3)

# import this


""" set and tuple comprehensions """

# set_nums = {i for i in range(1, 10)}
# print(set_nums)

# generator_nums = (i for i in range(1, 10))
# print(generator_nums)
# list_nums = [*generator_nums]
# print(list_nums)

nums = [*range(1, 11)]
print(nums)

# gen = (i for i in range(1, 10))
# for i in gen:
#     print(i)

# for x in gen:
#     print(i)

# iterator = range(1, 10)
# for i in iterator:
#     print(i)
# for x in iterator:
#     print(x)

# nums = tuple(i for i in range(1, 10))
# print(nums)