print('{:-^19}'.format('DESAFIO 23'))
print('Faça um programa que leia um número de 0 a 9999\n'
      'e mostre os dígitos separados.\n'
      'Ex: 1234\n'
      'Unidade: 4\n'
      'Dezena: 3\n'
      'Centena: 2\n'
      'Milhar: 1')
i = 0
while i == 0:
    try:
        num = input('Digite um número de 0 a 9999: ')
        if num != '' and 0 <= int(num) <= 9999:
            # lst = list(num)
            # lst.reverse()
            num = num[::-1]
            for n in range(4):
                if n == 0:
                    print('Unidade: {}'.format(num[n]))
                if n == 1:
                    print('Dezena: {}'.format(num[n]))
                if n == 2:
                    print('Centena: {}'.format(num[n]))
                if n == 3:
                    print('Milhar: {}'.format(num[n]))
            i = 1
        else:
            print('Dados inválidos!')
    except:
        print('Dados inválidos 2!')
