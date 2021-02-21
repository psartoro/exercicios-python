print('{:-^19}'.format('DESAFIO 10'))
print('Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar.\n')

while True:
    try:
        qtde = float(input('Insira a quantidade de dinheiro que tem em sua carteira: R$ '))
        if qtde is not None:
            dol = float(5.41)
            print('Dólar hoje: R$ {:.2f}'.format(dol))
            print('Você pode comprar US$ {:.2f} Dólares'.format(qtde/dol))
            break
        else:
            print('Valor inválido!\n')
    except:
        print('Valor inválido!\n')