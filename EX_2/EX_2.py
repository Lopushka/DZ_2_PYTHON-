from math import sqrt  # библиотека

s = int(input('Введите сумму чисел: '))
p = int(input('Введите произведение чисел: '))
k =sqrt((s/2)**2-p)
print(f'Первое число: {int(s/2-k)}. Второе число: {int(s/2+k)}')