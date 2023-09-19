""" кортежи - tuple """
# tuple() - неизменяемый, итерируемый, индексируемый, упорядоченный тип данных.

# days = ['mon', 'tue', 'wed', 'thu', 'sat', 'sun']
# days[4] = 'feb'

immutable_days = ('mon', 'tue', 'wed', 'thu', 'sat', 'sun')
# immutable_days[3] = 'march' # TypeError

# print(dir(immutable_days))

list_ = [1, 2, 3]
tuple_ = (1, 2, 3)
# print(list_.__sizeof__())
# print(tuple_.__sizeof__())

""" распаковка """
# a, b = (1, 2)
# c, d = [3, 4]
  

*a, b, c = (1, 2, 3, 4, 5)
print(a)
print(b)
print(c)
# fake_tuple = (20) # int
# print(type(fake_tuple))

# real_tuple = (10, ) #tuple
# print(type(real_tuple))

# fake_int = 30, # tuple