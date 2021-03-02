print(f'{"DESAFIO 40":-^50}')
print('Calcule a média.')
print('-' * 50)

while True:
    try:
        n1 = float(input('Digite a 1° nota: '))
        n2 = float(input('Digite a 2° nota: '))
        media = (n1 + n2) / 2
        if 0 < n1 <= 10 and 0 < n2 <= 10:
            if media >= 7:
                print(f'\033[1;32mMédia {media}. APROVADO!\033[m')
                break
            elif 5 <= media <= 6.9:
                print(f'\033[1;33mMédia {media}. RECUPERAÇÃO!\033[m')
                break
            else:
                print(f'\033[1;31mMédia {media}. REPROVADO!\033[m')
                break
        else:
            print('\033[1;31mNotas não podem ser menores que zero ou maiores que dez.\033[m')
    except:
        print('Dados inválidos.')