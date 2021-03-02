from random import randint
from time import sleep
import emoji

print(f'{"DESAFIO 45":-^50}')
print('Pedra, papel, tesoura. Melhor de 5!!!')
print('-' * 50)

j = 0
c = 0
i = 0

while True:
    try:
        opcao = int(input(f'Escolha {emoji.emojize(":punch:", use_aliases=True)}{emoji.emojize(":wave:", use_aliases=True)}'
                          f'{emoji.emojize(":v:", use_aliases=True)}\n'
                          '[ 0 ] Finalizar\n'
                          '[ 1 ] Pedra\n'
                          '[ 2 ] Papel\n'
                          '[ 3 ] Tesoura\n'
                          'Opção: '))
        if 1 <= opcao <= 3:
            st = randint(1, 3)
            if st == 1:
                cm = 'Pedra'
            elif st == 2:
                cm = 'Papel'
            else:
                cm = 'Tesoura'

            if opcao == 1:
                jg = 'Pedra'
            elif opcao == 2:
                jg = 'Papel'
            else:
                jg = 'Tesoura'

            print('Pedra')
            sleep(1)
            print('Papel')
            sleep(1)
            print('Tesoura...')
            sleep(1)
            print(f'\nJoguei >>> {cm}')
            print(f'Você jogou >>> {jg}')
            if opcao == st:
            # computador e jogador ecolheram a mesma opcao
                print(f'Empate!!!{emoji.emojize(":neutral_face:", use_aliases=True)}')
                i += 1
            # computador ganha -> pedra x papel, papel x tesoura, tesoura x pedra
            elif opcao == 1 and st == 2 or opcao == 2 and st == 3 or opcao == 3 and st == 1:
                print(f'Ganhei!!! ha ha ha {emoji.emojize(":zany_face:", use_aliases=True)}')
                c += 1
                i += 1
            # jogador ganha -> pedra x tesoura, tesoura x papel, papel x pedra
            elif opcao == 1 and st == 3 or opcao == 3 and st == 2 or opcao == 2 and st == 1:
                print(f'Você ganhou!!! Revanche...{emoji.emojize(":rage:", use_aliases=True)}')
                j += 1
                i += 1
            if i < 5:
                print(f'\n{"PLACAR":-^25}\nJOGADOR {j} X {c} COMPUTADOR')
                print('-' * 25)
                print('\nQuer jogar denovo?')
        if opcao == 0 or i == 5:
            print(f'\n{"PLACAR FINAL":-^25}\nJOGADOR {j} X {c} COMPUTADOR')
            sleep(3)
            print('\033[1;32mAté a próxima!!!\033[m')
            sleep(3)
            print(f'{"FIM":-^25}')
            break
    except:
        print('\033[1;31mOpsss... algo deu errado. Tente denovo!\033[m')