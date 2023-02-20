tot = totmil = menor = cont = 0
produtobarato = ' '
print('MERCADINHO DA JÚ')
while True:
    print('-'*30)
    produto = str(input('Nome do produto? '))
    valor = float(input('Valor do produto? R$ '))
    tot += valor
    cont += 1
    if cont == 1:
        menor = valor
        produtobarato = produto
    else:
        if valor < menor:
            menor = valor
            produtobarato = produto
    if valor > 1000:
        totmil += 1
    stop = ' '
    while stop not in 'NS':
        stop = str(input('Deseja continuar [S/N]? ')).strip().upper()[0]
    if stop == 'N':
        break
print('{:-^99}'.format(' FIM DAS COMPRAS '))
print(f'''Total da sua compra foi R${tot:.2f}
{totmil} produtos custando mais que R$1000.00
O produto mais barato foi {produtobarato} custando {menor:.2f}''')
