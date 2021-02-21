print('{:-^19}'.format('DESAFIO 12'))
print('Faça um programa que leia o preço de um produto e dê 5% de desconto.\n')

while True:
    try:
        p = float(input('Insira o preço do produto: R$ '))
        p = p - (p*5/100)
        print('O novo preço do produto é R$ {:.2f}'.format(p), '\nFim!')
        break
    except:
        print('Valor inválido!!!')