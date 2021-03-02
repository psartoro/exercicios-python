print(f'{"DESAFIO 38":-^50}')
print('Programa que leia dois números inteiros e informe qual é o maior, o menor ou se são iguais.')
print('-' * 50)

while True:
    try:
        n1 = int(input('Digite o 1° número: '))
        n2 = int(input('Digite o 2° número: '))
        if 0 < n1 and 0 < n2:
            if n1 > n2:
                print(f'Número {n1} é maior que o número {n2}!')
                break
            elif n2 > n1:
                print(f'Número {n2} é maior que o número {n1}!')
                break
            else:
                print(f'Os números são iguais!')
                break
        else:
            print('Números não podem ser menores que zero!')
    except:
        print('Dados inválidos.')