import time
while True:
    try:
        while True:
            s = int(input('Эта программа поможет переводить сантиметры в дюймы и в футы\nИз какой системы исчесления Вы будете переводить?\n1. Сантиметры\n2. Дюймы\n3. Футы\n'))
            if s == 1:
                f = 'сантиметров'
            if s == 2:
                f = 'дюймов'
            if s == 3:
                f = 'футов'
            c = int(input(f'Введите сколько {f}\n'))
            g = int(input('Введите в какую систему исчесления Вы хотите перевести\n1. Сантиметры\n2. Дюймы\n3. Футы\n'))
            if s == 1 and g ==2:
                print(c * 0.39)
            elif s == 1 and g == 3:
                print(c * 0.0328083992)
            elif s == 2 and g == 3:
                print(c * 0.083333292960053)
            elif s == 2 and g == 1:
                print(c * 2.54)
            elif s == 3 and g == 2:
                print((c * 12)+1)
            elif s == 3 and g == 1:
                print(c * 30,48)
            else:
                print('Столько же!')
                time.sleep(1)
    except ValueError:
        print('Недопустимый ввод')
        time.sleep(1)