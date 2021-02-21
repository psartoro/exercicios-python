print('{:-^19}'.format('DESAFIO 11'))
print('Faça um programa que leia a largura e altura de uma parede em metros, calcule sua área e a quantidade de\n'
      'tinta necessária para pintá-la.\n')

while True:
    try:
        l = float(input('Insira a Largura da parede: '))
        a = float(input('Insisra a Altura da parede: '))
        if l is not None and a is not None:
            print('\nA parede tem a dimesão de {}x{} e sua área é de {}m'.format(l, a, (l * a)))
            print('Você precisará de {} litros de tinta para pintar sua parede!'.format((l*a)/2))
            break
        else:
            print('Valores inválidos!\n')
    except:
        print('Valores inválidos!\n')
