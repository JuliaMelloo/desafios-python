soma = 0
cont = 0
for num in range(0, 501, 3):
     if num % 2 == 1:
        soma += num
        cont += 1
print(f'A soma de todos os {cont} valores solicitados é {soma}')





