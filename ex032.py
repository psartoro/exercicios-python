from datetime import date
print('{:-^50}'.format('DESAFIO 32'))
print('Faça um programa que leia um ano e informe se é ou não bissexto.')
print('-' * 50)
ano = ""

while ano == "":
    ano = input('Digite um ano ou 0 para ano atual ou \"Exit\" para \"sair\": ').strip()
    if ano == '0':
        ano = str(date.today().year)
    if ano.isnumeric() and len(ano) == 4:
        # divisivel por 4 mas nao divisivel por 100
        if int(ano) % 4 == 0 and int(ano) % 100 > 0:
            print(f'{ano} é um ano bissexto!')
        # nao divisivel 100 mas é divisivel 400
        elif int(ano) % 400 == 0 and int(ano) % 100 == 0:
            print(f'{ano} é um ano bissexto!')
        else:
            print(f'{ano} não é um ano bissexto!')
    elif ano.lower() == 'exit':
        break
    ano = ""


