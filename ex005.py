print('{:-^19}'.format('DESAFIO 5'))
print('\nFaça um programa que leia um número inteiro\ne mostre seu antecessor e sucessor.\n')

num = input('Digite um número: ')
i = 0

while i == 0:
    if not num:
        print('Valor não pode ser em branco!', end=' ')
        num = input('Digite um número: ')
    else:
        i = 1
        ant = int(num) - 1
        suc = int(num) + 1
        print('O Antecessor de {} é {} e o sucessor é {}'.format(num, ant, suc), '\nFim!')