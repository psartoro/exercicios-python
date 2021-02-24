print('{:-^19}'.format('DESAFIO 24'))
print('Crie um programa que receba o nome de uma cidade e\n'
      'diga se ela começa com o nome Santo.')
i = 0
cid = ""
while i == 0:
    cid = input('Digite um nome de cidade: ')
    if cid != '':
        i = 1
        while cid.split()[0].lower() != 'santo':
            cid = input('Ops... Digite outro nome de cidade: ')
            if cid == '':
                i = 0
                break
print('A cidade {} possui Santo no nome!'.format(cid.title()))
