# слово - word
""" dictionaries - словари """
# dict() - изменяемый, итерируемый, неиндексируемый(вместо индексов выступают ключи). Состоит из пар -  ключ: значение

# ключи могут быть только неизменяемыми типами данных и должны быть уникальными

# значения могут быть любыми типами данных

# словари используются для описания объектов

# литералы -{}


# stol = {'nojki': 4, 'color': 'black', 'height': 80}

# print(stol['color']) # black
# print(stol['weight']) # KeyError

# stol['color'] = 'red' # меняем значение ключа (red)

# human = {
#     'name': 'Alyia',
#     'age': 22,
#     'height': 165,
#     'name': 'Aigerim' 
# }
# print(human)  # первое значение поменяется

# a = {[1, 2]: '996703565575'} # Ошибка

""" Методы. Создание словаря """

# dict1 = {'key': 'value'}

# dict2 = dict(key = 'value', key2 = 'value2')

# dict3 = dict.fromkeys(['a1', 'b1'], 'value12')

# print(dict1)
# print(dict2)
# print(dict3) 


# """ Получение данных из словарей """
# phone = {
#     'model': 'Samsung',
#     'color': 'black',
#     'memory' : 256
# }
# phone['memory'] # 256
# # phone['display'] # KeyError

# print(phone.get('color')) # black
# print(phone.get('size')) # None
# print(phone.get('power', 'Нет такого ключа в словаре')) # Нет такого ключа в словаре
# print(phone.setdefault('model')) # Samsung
# print(phone.setdefault('power')) #  None( и создаст новый ключ, и присвоил значение None)
# print(phone)


""" Добавление данных в словарь """
# human = {
#     'name': 'Bakyt',
#     'age': 24,
# }

# human['last_name'] = 'Kalykov' # добавление нового ключа
# print(human)

# human.setdefault('height', 180) # добавление нового ключа
# print(human)

# human.update({'weight': 80}) # добавление нового ключа
# print(human)

# human.update([['is_married', False]])
# print(human)



""" Удаление данных из словаря """
# movie = {
    # 'title': 'Вторая жизнь Уве',
    # 'duration': 160,
    # 'year' : 2015,
#     'genre': ['Drama', 'Comedy']
# }

# deleted_key = movie.pop('year') # удаляет и может возвратить значение( если указана переменная)
# print(movie)
# print(deleted_key)

# del_el = movie.pop('country') # KeyError

# default_el = movie.pop('country', 'Значение1') # вместо ошибки запишет значение 
# print(default_el)

# deleted_pair = movie.popitem() # удаляет последний элемент словаря

# print(deleted_pair)
# print(movie)

# del movie('title')
# print(movie)

# movie.clear() # очищает весь словарь
# print(movie)

""" Перебор словаря / работа с циклом """

product = {
    'title': 'Robot Vacuum',
    'description': ' Пылесос',
    'price': 25000,
    'in_stock': True
}

for i in product:
    print(i)

# for key in product:
#     print(product[key])

# print(product.keys()) # возвращает коллекцию из ключей словаря
# for key in product.keys():
#     print(key)

# print(product.values()) # возращает коллекцию из значений словаря
# for value in product.values():
#     print(value)

# print(product.items()) # .items() - возвращает коллекцию из кортежей состоящих из 2 значений, где первое ключ, второе - значение
# for key, value in product.items():
#     print(f'Ключ {key}', f'Значение {value}')

# a1, a2 = ('val1', 'val2') # распаковка


# product2 = product.copy()
# print(product2)


