print(f'{"DESAFIO 37":-^50}')
print('Programa que leia um número inteiro e converta para base escolhida.')
print('-' * 50)

while True:
    try:
        num = int(input('Digite um número: '))
        print('Escolha um opção de conversão:\n'
               '[ 1 ] Binário\n'
               '[ 2 ] Octal\n'
               '[ 3 ] Hexadecimal')
        opcao = int(input('Opção: '))
        if 0 < opcao <= 3:
            if opcao == 1:
                print(f'{num} em Binário é {bin(num)}')
                break
            elif opcao == 2:
                print(f'{num} em Octal é {oct(num)}')
                break
            else:
                print(f'{num} em Hexadecimal é {hex(num)}')
                break
        else:
            print('Opção inválida!')
    except:
        print('Dados inválidos!')