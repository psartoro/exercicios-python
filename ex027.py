print('{:-^19}'.format('DESAFIO 27'))
print('Faça um programa que leia um nome completo e mostre\n'
      'o primeiro e último nome.')

nome = ""

while nome == '':
    nome = input('Digite um nome completo: ').strip()
    if nome.isnumeric():
        nome = ""

len = len(nome.split())
print(f'\nO primeiro nome é {nome.split()[0].title()} e o último é {nome.split()[len - 1].title()}.')
