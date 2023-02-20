valor = list()
while True:
    novovalor = int(input('Digite um valor: '))
    if novovalor in valor:
        print(f'Erro! O valor {novovalor} já existe na lista')
    else:
        valor.append(novovalor)
        print(f'O valor {novovalor} foi adicionado com sucesso a lista')
    sair = str(input('Deseja encerrar o programa ?[S/N]: ')).lower()
    if sair == 's':
        break
print('*' * 20)
valor.sort()
print(f'Você digitou os valores {valor}')
