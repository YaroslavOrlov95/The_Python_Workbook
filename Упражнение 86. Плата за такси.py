import math
import time

while True:
    try:
        while True:
            def taxi(km, baz_tarif, za_140m):
                u = km*1000
                m = u/140
                itogo = m*za_140m+baz_tarif
                (itogo)
                print(f'Вы должны оплатить ${math.ceil(itogo)}')
            km = float(input('Введите Ваше расстояние в км\n'))
            baz_tarif = 4
            za_140m = 0.25
            taxi(km, baz_tarif, za_140m)
    except ValueError:
        print('Недопустимый ввод')
        time.sleep(1)