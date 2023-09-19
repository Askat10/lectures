import random
import  sys
name = input('Здравствуйте. Введите ваше имя пожалуйста: ').capitalize()
yes_or_no = input(
    f'{name}, давайте сыграем в игру "Угадай число".\n'
    'Если согласны, введите Да, если не хотите то введите Нет, и я завершу игру.\n'
    'Ваш ответ: '
    ).capitalize()

while yes_or_no != 'Нет' and yes_or_no != 'Да':

    print('Вы неправильно ввели ответ, попробуйте снова, но покорректнее(Да/Нет))))')
    yes_or_no = input('Введите ответ: ').capitalize()
if yes_or_no == 'Нет':
    print('Очень жаль(((\nЕсли хотите сыграть, можете перезапустить игру)))')
    sys.exit()

elif yes_or_no == 'Да':
    pass

condition = input('Отлично! Давайте скорее начнем игру. Но перед этим давайте ознакомлю вас условиями игры, вы согласны?(Д/Н): ').upper()
while condition != 'Д' and condition != 'Н':
    condition = input('Введите буквы(Д/Н): ').upper()
if condition == 'Д':
    print('Компьютер будет загадывать число от 1 до 20, а вы должны будете угадать это число')
    print('Давайте начнем игру!')
elif condition == 'Н':
    print('Хорошо, тогда начинаем!')
last = 'Д'
while last == 'Д':
    random_number = random.randint(1,20)
    gamers_number = (input('Угадайте число: '))

    while gamers_number.isdigit() is not True:
        gamers_number = (input('Введите только число: '))
    
    guess_value = 1
    while int(gamers_number) > 20 or int(gamers_number) <1:
        print('Пожалуйста введите числа только от 1 до 20 включительно')
        gamers_number = (input('Угадайте число: '))
        while gamers_number.isdigit() is not True:
            gamers_number = (input('Введите только число: '))
    while int(gamers_number) != random_number:
        gamers_number = (input('вы не угадали число, попробуйте еще раз:'))
        while gamers_number.isdigit() is not True or int(gamers_number) > 20 or int(gamers_number) <1:
            gamers_number = (input('Введите только число от 1 до 20: '))
        guess_value +=1
    print(f'Отлично! вы угадали с {guess_value} раза.')

    last = input('Хотите еще раз сыграть?(Д/Н): ').capitalize()
    while last != 'Д' and last != 'Н':
        last = input('Не те буквы(Д/Н): ').capitalize()
    if last == 'Н':
        print('Пока.')
        sys.exit()