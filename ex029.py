print('{:-^50}'.format('DESAFIO 29'))
print('Leia a velocidade de um carro. Se for maior que 80km/h, mostre uma mensagem\n'
      'de que foi multado. A multa custa R$ 7,00 por km acima do limite')
print('-' * 50)
vel = ""


def validanum(n):
    try:
        float(n)
        return 1
    except:
        return 0


while vel == '':
    vel = input('Digite a velocidade do carro: ').strip()
    if validanum(vel) > 0:
        break
    vel = ""

if float(vel) > 80:
    multa = (float(vel) - 80) * 7
    print(f'\n{"MULTA":=^50}')
    print(f'{"Parabéns! Você foi multado.": ^50}\n')
    print(f'Velocidade registrada: {vel}km/h\n'
          f'Velocidade excedida: {float(vel) - 80:.0f}km/h\n'
          f'Valor da multa: R${multa:.2f}')
    print(f'\n{"Fim":=^50}')
else:
    print(f'\n{"MULTA":=^50}')
    print(f'{"Ótimo! Você não foi multado.": ^50}\n')
    print(f'Velocidade compatível com a via {vel}km/h')
    print(f'\n{"Fim":=^50}')
