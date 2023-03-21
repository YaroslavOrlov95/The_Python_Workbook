import time
while True:
    try:
        while True:
            n = int(input('Введите число до какого будет считать программа сумму n положительных чисел\n(счёт начинается от 1)\n'))
            sum = (n * (n+1)) / 2
            print(int(sum))
            time.sleep(1)
    except ValueError:
        print('Недопустимый ввод')
        time.sleep(1)