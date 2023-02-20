lanche = ('hamburguer', 'suco', 'pizza', 'pudim')
for comida in lanche:
    print(f'Eu vou comer {comida}')
print('Comi pra caramba!')

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')
print('Comi pra caramba!')

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')
print('Comi pra caramba!')

print(sorted(lanche))   # Coloca em ordem alfabetica


a = (2, 3, 4)
b = (5, 8, 1, 2)
c = a + b
print(c.count(5))  # Conta quantas vezes aparece o número que esta dentro do parenteses.
print(c.index(8))  # Em qual posição está o número dentro do parenteses.
del(c)  # Deleta a tupla 