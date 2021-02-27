print('{:-^50}'.format('DESAFIO 31'))
print('Leia a distância do percurso de uma viagem e calcule o preço da passagem.\n'
      'Até 200km, R$ 0,50 por km\n'
      'Acima de 200km, R$ 0,45 por km.')
print('-' * 50)


def validanum(n):
    try:
        float(n)
        return 1
    except:
        return 0

dst = ""

while dst == "":
    dst = input('Digite o percurso (em KM) da viagem: ').strip()
    if validanum(dst) > 0:
        break
    dst = ""

if float(dst) <= 200:
    cst = float(dst) * 0.5
else:
    cst = float(dst) * 0.45

print(f'\n{"PASSAGEM":=^50}\n')
print(f'Percurso: {dst}km')
print(f'Custo da passagem: R${cst:.2f}')
print(f'\n{"Fim":=^50}')
