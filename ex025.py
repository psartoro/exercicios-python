print('{:-^19}'.format('DESAFIO 25'))
print('Crie um programa que diga se um nome possui Silva em sua composição')

i = 0
nome = ""

while i == 0:
    nome = input('Digite um nome: ').strip()
    if nome != '':
        # for n in range(len(nome.split())):
        # if nome.split()[n].lower() == 'silva':
        if 'silva' in nome.lower():
            print('{} possui Silva no nome!'.format(nome.title().split()[0]))
            i = 1
