diaria = int(input('Quantos dias o carro foi alugado ? '))
km = float(input('Quantos km o carro percorreu nesses dias ? '))

total = (60 * diaria) + (0.15 * km)

print(f'O total a pagar é de R${total:.2f}')
