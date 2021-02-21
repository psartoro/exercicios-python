import math as m
print('{:-^19}'.format('DESAFIO 17'))
print('Calcular a hipotenusa de um triângulo retângulo')

while True:
    try:
        co = float(input('Insira o comprimento do cateto oposto: '))
        ca = float(input('Insira o comprimento do cateto adjacente: '))
        hp = m.hypot(co, ca)
        #hp = (co ** 2 + ca ** 2)/(1/2) => calculo tradicional
        print('A hipoteusa é {:.2f}'.format(hp))
        break
    except:
        print('Valores inválidos!')