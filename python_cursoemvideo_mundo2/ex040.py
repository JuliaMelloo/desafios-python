nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))
media = (nota1 + nota2) / 2
print(f'Tirando {nota1:.2f} e {nota2:.2f}, a média do aluno é {media:.2f}.')

if media < 5:
    print('Aluno está REPROVADO!')
elif 7 > media >= 5:
    print('Aluno está em RECUPERAÇÃO!')
else :
    print('Aluno está APROVADO!')
