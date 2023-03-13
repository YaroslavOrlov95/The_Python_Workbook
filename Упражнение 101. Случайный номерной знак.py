import random
from random import choice

while True:
    u = input('Напишите любой символ\n')
    q = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    chisla1 = random.choice(q)
    w = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    chisla2 = random.choice(w)
    e = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    chisla3 = random.choice(e)
    r = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    chisla4 = random.choice(r)
    t = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    alf1 = random.choice(t)
    y = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    alf2 = random.choice(y)
    u = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    alf3 = random.choice(u)
    print(f'Старый номерной знак: {alf1}{alf2}{alf3} {chisla1}{chisla2}{chisla3}\nНовый номерной знак: {chisla1}{chisla2}{chisla3}{chisla4} {alf1}{alf2}{alf3}')


