"""print('\033[1;30;45mOlá, Mundo!\033[m')"""

nome = 'Júlia'
cores = {'limpa':'\033[m',
        'azul':'\033[34m',
        'amarelo':'\033[33m',
        'pretoebranco':'\033[7;30m'}
print('Olá! Muito prazer em te conhecer, {}{}{}!!!'.format(cores['amarelo'], nome, cores['limpa']))
