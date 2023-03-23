import math
import time
while True:
    try:
        while True:
            def med(x, y, z):
                list = [x, y, z]
                list.sort()
                b = list[1]
                print(f'Медиана Ваших трёх значений {b}')
            print('Эта программа поможет вычислить тебе медиану трёх значений')
            x = int(input('Введите первое значение\n'))
            y = int(input('Введите второе значение\n'))
            z = int(input('Введите третье значение\n'))
            med(x, y, z)
    except ValueError:
        print('Недопустимый ввод')
        time.sleep(1)