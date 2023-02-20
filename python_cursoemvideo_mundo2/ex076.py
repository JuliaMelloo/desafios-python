lista = ('Lápis', '1,75', 'Borracha', '2,00',
         'Caderno', '15,90', 'Estojo', '25,00',
         'Transferidor', '4,50', 'Compasso', '9,99',
         'Mochila', '120,32', 'Canetas', '22,30',
         'Livro', '34,90')
print('-' * 30)
print(f'{"LISTAGEM DE PREÇOS":^30}')
print('-' * 30)
for cont in range(0, len(lista)):
    if cont % 2 == 0:
        print(f'{lista[cont]:.<20}R$ ', end='')
    else:
        print(lista[cont])

print('-' * 30)
