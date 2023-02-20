cinquenta = vinte = dez = um = rest50 = rest20 = rest10 = 0
print('{:=^100}'.format('\n BANCO DAJU \n'))
while True:
    valor = int(input('Qual valor deseja sacar ?R$ '))
    cinquenta = int(valor / 50)
    rest50 = valor - (cinquenta * 50)
    vinte = int(rest50 / 20)
    rest20 = rest50 - (vinte * 20)
    dez = int(rest20 / 10)
    rest10 = rest20 - (dez * 10)
    um = int(rest10 / 1)
    break
print(f'O total do valor {valor} será dispensado em:')
if cinquenta >= 1:
    print(f'{cinquenta} notas de R$50,00')
if vinte >= 1:
    print(f'{vinte} notas de R$20,00')
if dez >= 1:
    print(f'{dez} notas de R$10,00')
if um >= 1:
    print(f'{um} notas de R$1,00')
print('='*50)
print('Volte sempre ao BANCO DAJU! Tenha um ótimo dia!')
