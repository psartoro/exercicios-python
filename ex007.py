print('{:-^19}'.format('DESAFIO 7'))
print('Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre sua média.\n')

i = 0

while i == 0:
    try:
        n1 = float(input('Digite a nota 1: '))
        n2 = float(input('Digite a nota 2: '))
        if n1 is not None and n2 is not None and 0 <= n1 <= 10 and 0 <= n2 <= 10:
            i = 1
            m = (n1 + n2) / 2
            print('\nA média do aluno é {}'.format(m))
            if 6 <= m <= 10:
                print('\nAprovado!!!')
            elif m < 5:
                print('\nReprovado!!!')
            else:
                print('\nExame!!!')
        else:
            print('Valores inválidos!\n')
    except ValueError:
            print('Valores inválidos!\n')
