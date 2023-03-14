import time
while True:
    try:
        while True:
            suv = int(input('Введите количество сувениров\n'))
            bez = int(input('Введите количество безделушек\n'))
            ves_suv = suv*75
            ves_bez = bez*112
            t = ves_suv+ves_bez
            print(f'Общий вес сувениров составляет: {ves_suv}\n'
                  f'Общий вес безделушек составляет: {ves_bez}\n'
                  f'Общей вес сувениров и безделушек составляет: {t} грамм')
            time.sleep(1)
    except ValueError:
        print('Недопустимый ввод')
        time.sleep(1)