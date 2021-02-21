print('{:-^19}'.format('DESAFIO 15'))
print('Crie um programa que calcle a quantidade de KM percorridos e\n'
      'e a quantidade de dias pelos quais ele foi alugado.\n'
      'Qual o preço a pagar?\n')

while True:
    try:
        d = int(input('Insira a quantidade de dias do aluguel: '))
        km = float(input('Insira a quantidade de KM percorrido: '))
        r = (d * 60) + (km * 0.15)
        print('Dia: R$ 60.00\nKMs rodados: R$ 0.15')
        print('O valor a ser pago é R$ {:.2f}'.format(r))
        break
    except:
        print('Valores inválidos!')