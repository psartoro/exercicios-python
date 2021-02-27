print('{:-^19}'.format('DESAFIO 30'))
print('Crie um programa que leia um número inteiro e mostre se ele é par ou ímpar.')
print('-' * 50)

num = ""


def validanum(n):
    try:
        float(n)
        return 1
    except:
        return 0


while num == "":
    num = input('Digite um número: ').strip()
    if validanum(num) > 0:
        break
    num = ""

if float(num) % 2 == 0:
    print(f'\nO número {num} é PAR!')
else:
    print(f'\nO número {num} é IMPAR!')
