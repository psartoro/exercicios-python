print('{:-^19}'.format('DESAFIO 8'))
print('Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.\n')

i = 0
while i == 0:
    try:
        val = float(input('Insira um valor: '))
        if val is not None:
            i = 1
            print('{} em km é {}, em hm é {}, em dam e {} é em dm é {},'.format(val, (val/1000), (val/100), (val/10), (val*10)))
            print('em cm é {:.0f} e em mm é {:.0f}!'.format((val*100), (val*1000)), '\nFim!')
    except:
        print('Valor inválido!\n')