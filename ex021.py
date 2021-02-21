import pygame as pg
#modulo para usar funcionalidades do SO
import os

print('{:-^19}'.format('DESAFIO 21'))
print('Ler e tocar um MP3')

#inicializando pygame
pg.init()
#verifica se arquivo esta na pasta do projeto
if os.path.exists('ex021.mp3'):
    pg.mixer.music.load('ex021.mp3')
    pg.mixer.music.play()

    while pg.mixer.music.get_busy():
        pg.event.poll()

    print('Execução finalizada!')
else:
    print('Arquivo não encontrado!\nFim!')
