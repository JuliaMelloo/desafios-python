print('SEQUÊNCIA FIBONACCI')
começo = 1
anterior = 1
atual = 0
cont = 3
quant = int(input('Quantos números você deseja calcular na sequência fibonacci? '))
print('0..1..1..', end='')
while cont < quant:
    atual = começo + anterior
    print(f'{atual}..', end='')
    começo = anterior
    anterior = atual
    cont += 1
