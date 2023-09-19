from random import randint


def restart():
    confirmation = input('Хотите сыграть еще раз? (да/нет)\n')

    if confirmation.lower().startswith(('y', 'д')):
        init()
        play()
    elif confirmation.lower().startswith(('n', 'н')):

        print('Чао Какао!')

    else:
        print('Такого варианта нет. Попробуйте еще раз')

        restart()


def play():
    global counter
    global guessed_num

    try:
        num = int(input('Введите число: '))
        counter +=1

        if num == guessed_num:
            print(f'Вы угадали! Количество попыток: {counter}')
        elif num>guessed_num:
            print('загаданное число меньше')

            play()
        elif num<guessed_num:
            print('загаданное число больше')

            play()
        else:
            play()
    except ValueError:
        play()
    

def init():
    global guessed_num
    global user
    global counter

    guessed_num = randint(1, 25)
    print(f'Отлично, {user}, загаданное число находится между 1 и 25. Удачи!')
    counter = 0


def start():
    confirmation = input('Хотите сыграть? (да/нет)\n')

    if confirmation.lower().startswith(('y', 'д')):
        global user

        user = input('Пожалуйста введите Ваше имя: ').capitalize()

        init()
        play()
    elif confirmation.lower().startswith(('n', 'н')):

        print('Чао Какао!')

    else:
        print('Такого варианта нет. Попробуйте еще раз')

        start()

start()