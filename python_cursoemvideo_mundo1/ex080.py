# lista = list()
# for c in range(1, 6):
#     valor = int(input(f'Digite o {c}º número: '))
#     if c == 1:
#         lista.append(valor)
#     if c == 2:
#         if valor < lista[0]:
#             lista.insert(0, valor)
#         else:
#             lista.append(valor)
#     if c == 3:
#         if valor < lista[0]:
#             lista.insert(0, valor)
#         if valor < lista[1]:
#             lista.insert(1, valor)
#         else:
#             lista.append(valor)
#     if c == 4:
#         if valor < lista[0]:
#             lista.insert(0, valor)
#         if valor < lista[1]:
#             lista.insert(1, valor)
#         if valor < lista[2]:
#             lista.insert(2, valor)
#         else:
#             lista.append(valor)
#     if c == 5:
#         if valor < lista[0]:
#             lista.insert(0, valor)
#         if valor < lista[1]:
#             lista.insert(1, valor)
#         if valor < lista[2]:
#             lista.insert(2, valor)
#         if valor < lista[3]:
#             lista.insert(3, valor)
#         else:
#             lista.append(valor)
#     if c == 6:
#         if valor < lista[0]:
#             lista.insert(0, valor)
#         if valor < lista[1]:
#             lista.insert(1, valor)
#         if valor < lista[2]:
#             lista.insert(2, valor)
#         if valor < lista[3]:
#             lista.insert(3, valor)
#         if valor < lista[4]:
#             lista.insert(4, valor)
#         else:
#             lista.append(valor)
# print(lista)

lista = list()
for c in range(1, 6):
    valor = int(input(f'Digite o {c}º número: '))
    if c == 1 or valor > lista[-1]:
        lista.append(valor)
        print(f'Adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(lista):
            if valor <= lista[pos]:
                lista.insert(pos, valor)
                print(f'Adicionado na posição {pos} da lista...')
                break
            pos += 1
print(f'Os valores digitados em ordem foram {lista}')
