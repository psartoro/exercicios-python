print(f'{"DESAFIO 35":-^50}')
print('Faça um programa que leia o comprimento de retas e informe se elas podem\n'
      'ou não formar um triângulo. Obs: pesquise o princípio matemático de triângulo.')
print('-' * 50)

i = 0
lst = []

while i < 3:
    lado = input(f'Digite o {i + 1}° lado do triângulo: ').strip()
    try:
        lado = float(lado)
        if lado > 0:
            lst.append(lado)
            i += 1
        else:
            print('Lado não pode ser igual ou menor que 0!')
    except:
        print('Valores digitados incorretos!')

if (lst[0] + lst[1]) > lst[2] and (lst[1] + lst[2]) > lst[0] and (lst[0] + lst[2]) > lst[1]:
    print('-' * 50)
    print(f'\n{"RESULTADO":=^50}')
    print(f'\n{lst[0]}, {lst[1]} e {lst[2]} formam um Triângulo!')
    print(f'\n{"FIM":=^50}')
else:
      print('-' * 50)
      print(f'\n{"RESULTADO":=^50}')
      print(f'\n{lst[0]}, {lst[1]} e {lst[2]} não formam um Triângulo!')
      print(f'\n{"FIM":=^50}')
