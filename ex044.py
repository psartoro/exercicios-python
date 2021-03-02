print(f'{"DESAFIO 44":-^50}')
print('Calule o valor a ser pago pelo produto.')
print('-' * 50)

while True:
    try:
        val = float(input('Digite o valor do produto: R$'))
        print('[ 1 ] À Vista (Dinheiro/Cheque - com desconto)')
        print('[ 2 ] À Vista (Cartão - com desconto)')
        print('[ 3 ] Até 2 vezes no cartão (sem desconto)\n'
              '>= 3 vezes no cartão (com juros)')
        opcao = int(input('Opçao de pagto: '))
        if 0 < opcao <= 4:
            if opcao == 1:
                print(f'Valor a ser pago: R${val - ((val * 10) / 100):.2f}')
                print(f'Desconto 10%: R${(val * 10) / 100:.2f}')
                break
            elif opcao == 2:
                print(f'Valor a ser pago: R${val - ((val * 5) / 100):.2f}')
                print(f'Desconto 10%: R${(val * 5) / 100:.2f}')
                break
            elif opcao == 3:
                parcela = int(input('Qtde de parcelas: '))
                if parcela == 2:
                    print(f'Valor a ser pago: R${val:.2f}')
                    print(f'Valor da parcela: R${val / parcela:.2f}')
                    break
                elif parcela == 1:
                    opcao = 1
                else:
                    nval = float(val + ((val * 20) / 100))
                    print(f'Valor a ser pago: R${nval:.2f}')
                    print(f'Valor da parcela: R${nval / parcela:.2f}')
                    break
        else:
            print('Dados inválidos!')
    except:
        print('Dados inválidos!')