while True:
    try:
        while True:
            def ine(x):
                chisla = {1:'one', 2:'two', 3:'thee', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine', 10:'ten', 11:'eleven', 12:'twelve'}
                if x < 13 and x>0:
                    y = chisla[x]
                    print(f'Ваше число на английском пишется как: {y}')
                else:
                    print(' ')
            x = int(input('Введите ваше целое число от 1 до 12:\n'))
            ine(x)
    except:
        print('Недопустимый ввод')