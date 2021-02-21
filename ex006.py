print('{:-^19}'.format('DESAFIO 6'))
print('\nCrie um algoritmo que lea um número e mostre o seu dobro, triplo e raiz quadrada.\n')

num = input('Digite um número: ')
i = 0

while i == 0:
    if not num.isnumeric() or not num:
        print('Valor inválido.', end=' ')
        num = input('Digite um número: ')
    else:
        i = 1
        num = int(num)
        print('\nO dobro de {} é {}, seu triplo é {} e a raiz quadrada é {:.2f}'
               .format(num, (num * 2), (num * 3), (num**(1/2))))
