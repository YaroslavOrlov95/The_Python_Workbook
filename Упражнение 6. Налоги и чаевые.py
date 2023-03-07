import time
while True:
    try:
        while True:
            check = int(input('Введите сумму ресторанного чека,\nЧто бы узнать НДС(20%) и сумму чаевых 18%\n'))
            nalog = check / 100 * 20
            weiter = (check - nalog) / 100 * 18
            itogo = nalog + weiter
            print(f'Сумма НДС с Вашего чека составила: {nalog:.2f}\nСумма чаевых составила: {weiter:.2f}\nОбщая сумма НДС и Чаевые: {itogo:.2f}')
            time.sleep(1)
    except ValueError:
        print('Недопустимый ввод')
        time.sleep(1)