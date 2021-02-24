print('{:-^19}'.format('DESAFIO 26'))
print('Faça um programa que leia uma frase e mostre: \n'
      '-> Quantas vezes aparece a letra A\n'
      '-> Em que posição ela aparece pela primeira vez\n'
      '-> Em que posição ela aparece pela última vez')

frase = ""

while frase == '':
    frase = input('Digite uma frase: ').strip()
    if frase.isnumeric():
        frase = ""

print('-> A letra \"A\" aparece {} vezes na frase!'.format(frase.lower().count('a')))
print('-> A letra \"A\" aparece pela prmeira vez na posição {}'.format(frase.lower().find('a')+1))
print('-> A letra \"A\" aparece pela última vez na posição {}'.format(frase.lower().rfind('a')+1))



