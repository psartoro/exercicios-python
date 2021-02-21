print('{:-^19}'.format('DESAFIO 14'))
print('Escreva um programa que converta °C em °F')

while True:
    try:
        t = float(input('Insira a temperatura em °C: '))
        f = (t*1.8) + 32
        print('{} °C equivale a {} °F'.format(t, f))
        break
    except:
        print('Valor inváido!')