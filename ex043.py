print(f'{"DESAFIO 43":-^50}')
print('Calculadora IMC.')
print('-' * 50)
nome = ""
peso = ""
altura = ""


# funcao
def calculaimc(pes, alt):
    try:
        pes = float(pes)
        alt = float(alt)
        imc = pes / (alt * alt)
        return imc
    except:
        return 0


while not nome or not peso or not altura:
    nome = input('Digite seu nome: ').strip()
    peso = input('Digite seu peso: ').strip()
    altura = input('Digite sua altura: ').strip()
    dados = [nome, peso, altura]
    for n in range(3):
        if dados[n] == '':
            print('Valores incorretos!')
            break

imc = calculaimc(dados[1], dados[2])

while imc == 0:
    print('Peso e Altura devem ser numéricos!')
    print('-' * 45)
    peso = input('Digite seu peso: ').strip()
    altura = input('Digite sua altura: ').strip()
    dados[1] = peso
    dados[2] = altura
    imc = calculaimc(dados[1], dados[2])

print('-'*45)

if imc < 18.5:
    print('Seu IMC é de:', round(imc))
    print('\033[1;33mCuidado {}!!!\033[m Você está abaixo do peso!'.format(nome.capitalize()))
elif 18.5 <= imc <= 24.9:
    print('Seu IMC é de:', round(imc))
    print('\033[1;32mParabéns {}!!!\033[m Seu peso está normal!'.format(nome.capitalize()))
elif 25.0 <= imc <= 29.9:
    print('Seu IMC é:', round(imc))
    print('\033[1;33mCuidado {}!!!\033[m Você está acima de seu peso!'.format(nome.capitalize()))
elif 30.0 <= imc <= 34.9:
    print('Seu IMC é:', round(imc))
    print('\033[1;31mAtenção {}!!!\033[m Obesidade grau I'.format(nome.capitalize()))
elif 35 <= imc <= 39.9:
    print('Seu IMC é:', round(imc))
    print('\033[1;31mAtenção {}!!!\033[m Obesidade grau II'.format(nome.capitalize()))
elif 40 <= imc:
    print('Seu IMC é:', round(imc))
    print('\033[1;31mAtenção {}!!!\033[m Obesidade grau III'.format(nome.capitalize()))

print('-'*45)