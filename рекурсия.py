def sum_to(n):
    if n <= 0 :
        return 0 # Базовый случай
    else:
        return n + sum_to(n - 1) # Рекурсивный случай

num = int(input("Введите положительное целое число: "))
total = sum_to(num)
print("Сумма целых чисел от нуля до", num, "равна", total)
