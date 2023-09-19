""" list - Списки """

# list() - коллекция. Изменяемый, упорядоченный, индексируемый, итерируемый. Служит для хранения набора элементов

# Элементами списка могут быть любые типы данных

# list = [10, 'str', [1, 2, 3], (1, 2, 3), {'key':'value'}, True, None, set()]

# list1 = [1, 2, 3]
# print(list1[1])   #   2
# list1[1] = 5
# print(list1[1])   #   5
# print(list1)   #  [1, 5, 3]

""" Методы списков """
# print(dir(list))

# 1. Добавление элементов в список
# my_list = [1, 2, 3]
# print('До', my_list)
# my_list.append(4)
# print('После', my_list)

# list.append(obj) - Добавляет обьект в конец списка

# my_list2 = [1, 3, 4]
# my_list2.insert(1, 'str')
# print(my_list2)

# list.insert(index, obj) - вставляет обьект на место указанного индекса

# list_1 = [1, 2, 3]
# list_2 = [4, 5, 6]
# list_1.extend(list_2)
# print(list_1)

# list.extend(iterable) - добавляет элементы iterable в конец list


# 2. Удаление элементов из списка
# nums = [1, 2, 3]
# deleted_el = nums.pop()
# first_el = nums.pop(0)
# print(deleted_el)
# print(nums)

# list.pop([index]) - удаляет и может возвращает(если дать переменную) элемент по index, по умолчанию последний 

nums = [4, 5, 6, 7, 5, 5]
# nums.remove(5)
# print(nums)

# list.remove(obj) - удаляет первый встретившийся obj из списка

# nums.clear()
# print(nums)

# nums.clear() - полностью очищает список

nums = [1, 1, 2, 3]
# del nums[1]
# print(nums)


nums = [5, 3, 6, 2, 1]
# nums.sort() # сортировка списка по возрастанию
# print(nums)
# nums.sort(reverse=True) # сортировка списка по убыванию

names = ['Aliya', 'Sergey', 'Kanat', 'Mariya']
# names.sort()
# print(names)
# names.sort(key=len)
# print(names)
# list.sort([key], [reverse]) - сортирует список по возрастанию, если reverse = True - по убываниюб. Если в key передать имя функции, применит key к каждому элементу списка

# names.reverse()
# print(names)

# list.reverse() - переворачивает список

# print(names[::-1])

# nums = [1, 1, 1, 2, 3, 4, 5,]
# print(nums.count(1))

# list.count(value) - считает количество value в списке

# print(nums.index(3)) # показывает под каким индексом

# list_ = ['sdf']
# print(list_.index('sdf'))


