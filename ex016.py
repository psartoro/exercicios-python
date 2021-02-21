from math import trunc

print('{:-^19}'.format('DESAFIO 16'))
print('Crie um programa que leia um número real qualquer e\n'
      'mostre sua porção inteira')

while True:
    try:
        vl = float(input('Digite um valor qualquer: '))
        print('Porção inteira de {} é {}!'.format(vl, trunc(vl)))
        break
    except:
        print('Valor inválido!')
