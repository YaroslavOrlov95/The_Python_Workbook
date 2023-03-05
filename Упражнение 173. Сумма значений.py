while True:
    try:
        def a():
            x = float(input('Введите число: '))
            if x <= 0 or x == '':
                return 0
            else:
                return float(x) + a()

        def main():
            print('Привет, дальше тебе нужно по очереди вводить числа, которые ты хочешь сумировать\nКак нужно будет получить итог - введи 0')
            d = a()
            print(d)
        main()
    except:
        print("Вы ввели, что то не так")