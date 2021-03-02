from datetime import date
print(f'{"DESAFIO 41":-^50}')
print('Mostre a categoria do atleta.')
print('-' * 50)

while True:
    try:
        ano_nasc = int(input('Digite o ano de nascimento do atleta: '))
        idade = int(date.today().year) - ano_nasc
        if ano_nasc > 0 and len(str(ano_nasc)) == 4:
            if idade == 9:
                print(f'{idade} anos. MIRIM!')
                break
            elif 9 < idade <= 14:
                print(f'{idade} anos. INFANTIL!')
                break
            elif 15 <= idade <= 19:
                print(f'{idade} anos. JUNIOR!')
                break
            elif 20 <= idade <= 25:
                print(f'{idade} anos. SÊNIOR!')
                break
            else:
                print(f'{idade} anos. MASTER!')
                break
        else:
            print('Dados inválidos!')
    except:
        print('Dados inválidos!')