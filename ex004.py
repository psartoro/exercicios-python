print('{:-^19}'.format('DESAFIO 4'))

algo = input('Digite algo: ')
i = 0
while i == 0:
    if not algo:
        print('Valor não pode ser em branco!')
        algo = input('Digite algo: ')
    else:
        i = 1
        print(f'Tem espaços? {algo.isspce()}')
        print('{} é um número?'.format(algo), algo.isnumeric())
        print('{} é alfabético?'.format(algo), algo.isalpha())
        print('{} é alfanumérico?'.format(algo), algo.isalnum())
        print('{} está em maiúsculas?'.format(algo), algo.isupper())
        print('{} está em minúsculas?'.format(algo), algo.islower())
        print('A primeira letra de {} está em maiúscula?'.format(algo), algo.istitle())
        print('Fim!')


