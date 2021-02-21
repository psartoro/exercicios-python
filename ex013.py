print('{:-^19}'.format('DESAFIO 13'))
print('Faça um programa que leia o salário de um funcionário e aplique 15% de aumento.\n')

while True:
    try:
        sal = float(input('Insira o salário: R$ '))
        sal = sal + (sal*15/100)
        print('Novo salário com aumento de 15% aplicado: R$ {:.2f}'.format(sal), '\nFim!')
        break
    except:
        print('Valor inválido!')