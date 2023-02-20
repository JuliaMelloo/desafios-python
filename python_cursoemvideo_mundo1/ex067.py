while True:
    num = int(input('Quer ver a tabuada de qual valor? '))
    print('-'*30)
    if num < 0:
        break
    for cont in range(0, 11):
        print(f'{num}x{cont}={num*cont}')
    print('-' * 30)
print('Programa tabuada encerrado. Volte sempre!')

