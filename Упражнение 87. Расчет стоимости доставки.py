import math
import time
while True:
    try:
        while True:
            def dostavka(g):
                x = g - 1
                y = x * 2.95 + 10.95
                print(f'Ваша сумма доставки составляет ${y:.2f}')
            g = float(input('Введите сколько товаров Вы заказли\n'))
            dostavka(g)
    except ValueError:
        print('Недопустимый ввод')
        time.sleep(1)