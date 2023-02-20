from datetime import date
data_atual = date.today().year
quant_maior = 0
quant_menor = 0
for c in range(1, 8):
    nasc = int(input(f'Digite o {c}º ano de nascimento: '))
    idade = data_atual - nasc
    if idade >= 18:
        quant_maior += 1
    else:
        quant_menor += 1
print(f'''Ao todo tivemos {quant_maior} pessoas maiores de idade
E também tivemos {quant_menor} pessoas menores de idade''')

