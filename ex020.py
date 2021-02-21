import random as r

print('{:-^19}'.format('DESAFIO 20'))
print('Sorteie a ordem de alunos para apagar o quadro negro.')

while True:
    try:
        n = 0
        lst = []
        for n in range(4):
            al = input('Aluno {}: '.format(n + 1))
            lst.append(al)
            n += 1
        r.shuffle(lst)
        i = 0
        for i in range(len(lst)):
            print('O {}° aluno será: {}\nFim!'.format(i + 1, lst[i]))
            i += 1
        break
    except:
        print('Dados inválidos!')
