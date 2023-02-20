valor = float(input('Digite o valor do produto: '))

desc = valor - (valor * 5 / 100)

print(f'Esse produto de R${valor:.2f} fica por R${desc:.2f} com 5% de desconto')
