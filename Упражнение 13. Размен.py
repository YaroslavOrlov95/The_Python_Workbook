import time
while True:
    try:
        while True:
            sdacha = int(input(f'Введите сумму сдачи в центах\n'))
            x = 0
            z = 0
            v = 0
            n = 0
            a = 0
            d = 0
            g = 0
            while sdacha >= 200:
                x = x + 1
                sdacha = sdacha - 200
            if x != 0:
                print(f'Вы получите сдачу монетами номиналом в:\n2$ - {x} шт.')
            while sdacha >= 100:
                z = z + 1
                sdacha = sdacha - 100
            if z != 0:
                print(f'1$ - {z} шт.')
            while sdacha >= 50:
                v = v + 1
                sdacha = sdacha - 50
            if v != 0:
                print(f'0.50$ - {v} шт.')
            while sdacha >= 25:
                n = n + 1
                sdacha = sdacha - 25
            if n != 0:
                print(f'0.25$ - {n} шт.')
            while sdacha >= 10:
                a = a + 1
                sdacha = sdacha - 10
            if a != 0:
                print(f'0.10$ - {a} шт.')
            while sdacha >= 5:
                d = d + 1
                sdacha = sdacha - 5
            if d != 0:
                print(f'0.05$ - {d} шт.')
            while sdacha >= 1:
                g = g + 1
                sdacha = sdacha - 1
            if g != 0:
                print(f'0.01$ - {g} шт.')
            time.sleep(1)
    except ValueError:
        print('Недопустимый ввод')
        time.sleep(1)