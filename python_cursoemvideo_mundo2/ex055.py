menor = 0
maior = 0
for c in range(1, 6):
    peso = float(input(f'Digite o {c}º peso: '))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso < menor:
            menor = peso
        if peso > maior:
            maior = peso
print(f"""O maior peso lido foi de {maior}Kg
O menor peso lido doi de {menor}Kg""")




