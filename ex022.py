print('{:-^19}'.format('DESAFIO 22'))
print('Crie um programa que receba o nome completo de uma pessoa\n'
      'e mostre:\n-> Tudo em maiúsculo\n-> Tudo em minúsculo\n-> Total de letras (não contar espaços)\n'
      '-> Total de letras do primeiro nome')
i = 0
while i == 0:
    try:
        nome = input('Digite seu nome completo: ')
        if nome.isnumeric() or not nome or len(nome) <= 5:
            print('Valores inválidos!\n')
        else:
            nome = nome.strip()
            print(nome.upper())
            print(nome.lower())
            print('Total de {} letras, sem contar os espaços'.format(len(nome.replace(' ', ''))))
            nome = nome.split()
            print('Total de {} letras no primeiro nome'.format(len(nome[0])), '\nFim!')
            i = 1
    except:
        print('Valores inválidos!')
