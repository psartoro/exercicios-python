from datetime import date
print(f'{"DESAFIO 39":-^50}')
print('Programa que leia o ano de nascimento e informe se irá se alistar no serviço militar e,\n'
      'se sim, quando. Senão, quanto tempo passou.')
print('-' * 50)

while True:
    try:
        ano_nasc = int(input('Digite o ano de nascimento: '))
        idade = int(date.today().year) - ano_nasc
        if len(str(ano_nasc)) == 4:
            if idade == 18:
                print(f'Você tem {idade} anos. É hora de se alistar!!!')
                break
            elif idade < 18:
                sera = 18 - idade
                print(f'Você tem {idade} anos.\nSeu alistamento militar será em {date.today().year + sera}, daqui {sera} anos!')
                break
            else:
                passou = idade - 18
                print(f'Você tem {idade} anos.\nSeu alistamento militar foi em {date.today().year - passou}, {passou} anos atrás!')
                break
        else:
            print('Dados inválidos!')
    except:
        print('Dados invalidos!')