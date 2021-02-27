print('{:-^50}'.format('DESAFIO 33'))
print('Faça um programa que leia três números e informe qual é o maior e qual é o menor.')
print('-' * 50)

n = 0
maior = 0
menor = 0

while n < 3:
    num = input(f'Digite o {n + 1}° número: ').strip()
    try:
        num = int(num)
        if num > 0:
            if n == 0:
                maior = num
                menor = num
                n += 1
            elif num > maior:
                maior = num
                n += 1
            elif num < menor:
                menor = num
                n += 1
        else:
            print('Valor não pode ser menor ou igual a 0.')
    except:
        print('Valor digitado não é um número inteiro.')

print('-'*50)
print(f'\n{"RESULTADO":=^50}')
print(f'\nO maior número é {maior} e o menor número é {menor}')
print(f'\n{"Fim":=^50}')