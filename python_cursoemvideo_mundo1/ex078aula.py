num = [2, 5, 9, 1]
num[2] = 3  # muda o valor de um índice desejado
num.insert(2, 0)  # insere um novo valor a um índice desejado
num.append(7)  # Adiciona um valor ao final da lista
num.sort()  # Coloca a lista em ordem
num.sort(reverse=True)  # Coloca a lista em ordem revertida
num.pop(2)  # Exclui o valor do indice desejado
num.remove(2)  # Remove o valor desejado da lista
if 5 in num:
    num.remove(5)
else:
    print('O Número 5 não foi encontrado')
print(num)
print(f'Essa lista tem {len(num)} elementos. ')
