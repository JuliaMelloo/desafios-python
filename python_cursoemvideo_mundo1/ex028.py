from random import choice
num = [0, 5]

print('-=-' * 19)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 19)
n = int(input('Em que número eu pensei? '))
print('Processando...')

escolhido = choice(num)
if escolhido == n:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print(f'GANHEI! Eu pensei no número {escolhido} e não no {n}')