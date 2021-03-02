print(f'{"DESAFIO 36":-^50}')
print('Programa de aprovação de empréstimo bancário.')
print('-' * 50)

while True:
    try:
        val_imovel = float(input('Insira o valor do imóvel: R$'))
        salario = float(input('Insira o salário: R$'))
        prazo = int(input('Em quantos anos vai pagar? '))
        if val_imovel > 0 and salario > 0 and 0 < prazo <= 12:
            prestacao = val_imovel/(prazo*12)
            if (prestacao / salario)*100 < 30:
                print('\n\033[1;32mEmpréstimo aprovado.\033[m')
                print(f'Valor do imóvel: R${val_imovel:.2f}')
                print(f'% sobre o salário: {(prestacao / salario)*100:.0f}%')
                print(f'Total de parcelas: {prazo*12}')
                print(f'Valor da prestação: R${prestacao:.2f}')
                break
            else:
                print('\n\033[1;31mEmpréstimo não aprovado.\033[m')
                print(f'Valor do imóvel: R${val_imovel:.2f}')
                print(f'% sobre o salário: {(prestacao / salario) * 100:.0f}%')
                print(f'Total de parcelas: {prazo * 12}')
                print(f'Valor da prestação: R${prestacao:.2f}')
                break
        else:
            print('Valores não podem ser iguais a zero e/ou prazo incorreto!')
    except:
        print('Valores inválidos!')