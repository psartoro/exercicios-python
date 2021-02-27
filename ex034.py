print('{:-^50}'.format('DESAFIO 34'))
print('Informe o salário do funcionário e calcule um aumento.\n'
      '> R$ 1250, aumento de 10%\n'
      '< R$ 1250, aumento de 15%')
print('-' * 50)

i = 0
sal = 0
au = 0
nsal = 0

while i == 0:
    sal = input('Informe o salário: R$').strip()
    try:
        sal = float(sal)
        if sal > 0:
            if sal >= 1250:
                au = (sal * 10 / 100)
                nsal = sal + (sal * 10 / 100)
                i = 1
            else:
                au = sal * 15 / 100
                nsal = sal + au
                i = 1
        else:
            print('Salário não pode ser menor ou igual a 0!')
    except:
        print('Valor digitado inválido!')

print('-'*50)
print(f'\n{"RESULTADO":=^50}')
print(f'\nPorcentagem de aumento: {au/sal*100:.0f}%')
print(f'Valor do aumento: R${au:.2f}')
print(f'O novo salário será: R${nsal:.2f}')
print(f'\n{"Fim":=^50}')