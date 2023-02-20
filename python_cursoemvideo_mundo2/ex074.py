from random import randint
num = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print('Os números sortedos foram: ', end='')
for n in num:
    print(f'{n} ', end='')
print(f'\nO MAIOR número sorteado foi {max(num)}')  # Maior número
print(f'O MENOR número sorteado foi {min(num)}')  # Menor número

