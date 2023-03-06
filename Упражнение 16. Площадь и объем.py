import math
import time
while True:
    try:
        while True:
            x = float(input('Что Вы хотите узнать?\n1. Площадь круга\n2. Площадь шара\n'))
            r = float(input('Введите число радиуса\n'))
            if x == 1:
                area = math.pi * r**2
                print(area)
            if x == 2:
                area = 4*math.pi * r**2
                print(area)
    except ValueError:
        print('Недопустимый ввод')
        time.sleep(1)