cont = soma = n = 0
n = int(input('Digite um número [999 para parar]: '))
while n != 999:
    soma += n
    cont += 1
    n = int(input('Digite um número  [999 para parar]: '))
print(f'Foram digitados {cont} números e a soma deles foi de {soma}')
