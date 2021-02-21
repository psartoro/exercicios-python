import random as r

print('{:-^19}'.format('DESAFIO 19'))
print('Sorteie um de quatro alunos para apagar o quadro negro.')

while True:
    try:
        n = 0
        lst = []
        for n in range(4):
            al = input('Aluno {}: '.format(n+1))
            lst.append(al)
            n += 1
        st = r.choice(lst)
        print('O aluno sorteado foi: {}\nFim!'.format(st))
        break
    except:
        print('Dados inválidos!')
