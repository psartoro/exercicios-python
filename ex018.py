import math as m

print('{:-^19}'.format('DESAFIO 18'))
print('Leia um ângulo e calcule o seno, cosseno e tangente.')

while True:
    try:
        ang = float(input('Digite o ângulo: '))
        ang = m.radians(ang)
        sn = m.sin(ang)
        csn = m.cos(ang)
        tng = m.tan(ang)
        print('Valor digitado: {}\nSeno: {:.2f}\nCosseno: {:.2f}\nTangente: {:.2f}'
              '\nFim!'.format(ang, sn, csn, tng))
        break
    except:
        print('Dados inválidos!')
