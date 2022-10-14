import pygame
from pygame.locals import *
from sys import exit
from random import randint
from extra import *

pygame.init()

altura = 480
largura = 640

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Bob Esponja')


todas_sprites = pygame.sprite.Group()

for i in range (3):
    alface_i = Alface(randint(40,600), randint(40,420))
    todas_sprites.add(alface_i)
    carne_i = Carne(randint(40,600), randint(40,420))
    todas_sprites.add(carne_i)
    pao_i = Pao(randint(40,600), randint(40,420))
    todas_sprites.add(pao_i)
    
todas_sprites.add(bob)

relogio = pygame.time.Clock()

while True:
    relogio.tick(100)
    tela.fill((0,110,100))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if pygame.key.get_pressed():
            bob.posicao()
    todas_sprites.draw(tela)
    todas_sprites.update()
    pygame.display.flip()


    #retangulo = pygame.draw.rect(tela, (0, 0, 255), (370, 420, 10, 10))

    #colisoes()
   # if retangulo.colliderect(bob):
    #    print('colidiu')


