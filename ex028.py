from random import randint
from time import sleep
import emoji

print('{:-^50}'.format('DESAFIO 28'))
print('Faça um programa que sorteie um número entre 0 e 5 \n'
      'e o usuário tente descobrir qual foi o escolhido.')
print('-'*50)

num = ""

while num == '':
    num = input('Digite um número de 0 a 5: ').strip()
    print('Processando...', emoji.emojize(':game_die:', use_aliases=True))
    sleep(3)
    if num.isnumeric():
        if int(num) < 0 or int(num) > 5:
            num = ""
        else:
            break
    num = ""

st = randint(0, 5)

if int(st) == int(num):
    print('='*40)
    print(f'Número sorteado: {st}')
    print('Parabéns!!! Você acertou o número', emoji.emojize(':thumbsup:', use_aliases=True), '!!!')
    print('='*40)
else:
    print('='*30)
    print(f'Número sorteado: {st}')
    print('Ops! Ganhei... não foi dessa vez!', emoji.emojize(":stuck_out_tongue_winking_eye:", use_aliases=True))
    print('='*30)
