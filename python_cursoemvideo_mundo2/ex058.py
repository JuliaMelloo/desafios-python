from random import randint
escolhido = randint(0, 10)
cont = 0
n = 11
print('{:=^200}'.format('\nVou pensar em um número entre 0 e 10. Tente adivinhar...\n'))
while n != escolhido:
    cont += 1
    n = int(input('Qual seu palpite? '))
    if n < escolhido:
        print('Mais... Tente novamente')
    if n > escolhido:
        print('Menos... Tente novamente')
print(f'Acertou com {cont} tentativas. Parabéns!')
