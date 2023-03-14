m = int(input('Введите кол-во монет: '))
cnt = 0
for i in range(m):
    p = int(input(f'Положение монеты {i+1}: 0 - это решка или 1 - это гербом ? '))
    if p == 0:
        cnt += 1
print(f'Кол-во монет, надо перевернуть: {cnt if cnt<m/2 else m-cnt}')
