print(f'{"DESAFIO 42":-^50}')
print('Classifique o triângulo.')
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
    if lst[0] == lst[1] == lst[2]:
        print('Triânguulo Equilátero!')
    elif lst[0] != lst[1] != lst[2] != lst[0]:
        print('Triângulo Escaleno!')
    else:
        print('Triângulo Isóceles!')
else:
      print('-' * 50)
      print(f'\n{lst[0]}, {lst[1]} e {lst[2]} não formam um Triângulo!')

