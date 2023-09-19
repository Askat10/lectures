""" set - множества """
# set() - коллекция уникальных, неизменяемых элементов. Может хранить в себе только неизменяемые типы данных.
#  Убирает дубликаты элементов. Итерируемый, изменяемый, неиндексируемый, неупорядоченный.

# литералы - {}

# empty_set = {} # Error
# print(type(empty_set))
# empty_set = set() # Ok

# set_1= {1, 2, 3}
# print(type(set_1))

# u_set = {1, 'hello', (1, 2), True, False, None, 0, 1, 2}
# print(u_set)

# nums_set = {5, 6, 3, 2, 8, 10}
# print(nums_set)

# set_2 = {1, 2, [3, 4]} # TypeError

# list_ = ['hello', 'hello', 1, 2, 1, 2, 3, 4, 5, 6, 4, 3, 5]
# a = set(list_)
# b = list(a)
# print(b)

""" методы коллекции """

# a1 = {1, 2, 3, 4, 4}
# b1 = {8, 7, 2, 4, 4}
# print(a1.intersection(b1))



