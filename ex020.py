import random as r

print('{:-^19}'.format('DESAFIO 20'))
print('Sorteie a ordem de alunos para apagar o quadro negro.')

while True:
    try:
        n = 0
        lst = []
        al = input('Aluno {}: '.format(n + 1))
        if al != '':
            for n in range(4):
                lst.append(al)
                n += 1
            r.shuffle(lst)
            i = 0
            for i in range(len(lst)):
                print('O {}° aluno será: {}\nFim!'.format(i + 1, lst[i]))
                i += 1
        else:
            print('Dados inválidos!\nFim!')
            break
    except:
        print('Dados inválidos!')
    break
