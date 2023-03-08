import time
while True:
    try:
        while True:
            obem = input('Введите объём стеклотары\n1. 0.5 л.\n2. 1 л.\n3. 1.5 л.\n4. 2 л.\n')
            kolvo = int(input('Введите количество сдаваемой стеклотары\n'))
            if obem == '1' or obem == '2':
                itogo = kolvo * 0.10
                print(f'Ваша выручка составит ${itogo:.2f}')
                time.sleep(1)
            elif obem == '3' or obem == '4':
                itogo = kolvo * 0.25
                print(f'Ваша выручка составит ${itogo:.2f}')
                time.sleep(1)
            else:
                print('Введены некоректные символы, проверьте правильность написания')
                time.sleep(1)
    except ValueError:
        print('Недопустимый ввод')
        time.sleep(1)