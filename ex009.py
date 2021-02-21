print('{:-^19}'.format('DESAFIO 9'))
print('Faça um rograma que leia um número inteiro qualquer e mostre a sua tabuada.\n')

while True:
    try:
        n = int(input('Insira um número inteiro: '))
        if n is not None:
            i = 0
            while i <= 10:
                print('{} x {} = {}'.format(n, i, (n*i)))
                i += 1
            break
        else:
            print('Valor inválido!\n')
    except:
            print('Valor inválido!\n')