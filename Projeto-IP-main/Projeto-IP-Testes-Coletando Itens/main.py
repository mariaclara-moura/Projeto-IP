import pygame
from pygame.locals import *
from sys import exit
from random import randint
from extra import *

pygame.init()
txt = pygame.font.SysFont('arial', 25, bold=True, italic=False)
altura = 480
largura = 640

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Bob Esponja')
#========================================


class Sponge(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load('sprites/bob_1.png'))
        self.sprites.append(pygame.image.load('sprites/bob_2.png'))
        self.atual = 0
        self.image = self.sprites[self.atual]
        self.image = pygame.transform.scale(self.image, (40, 40))

        self.rect = self.image.get_rect()
        self.x_bob = 100
        self.y_bob = 100
        self.rect.topleft = self.x_bob,self.y_bob
        self.animar = False


    def posicao(self):
        self.animar = True
        if pygame.key.get_pressed()[K_a]:
            self.x_bob -= 3
            if self.x_bob <= 0:
                self.x_bob = 0
            self.rect.topleft = self.x_bob,self.y_bob
        if pygame.key.get_pressed()[K_d]:
            self.x_bob +=3
            if self.x_bob >= 600:
                self.x_bob = 600
            self.rect.topleft = self.x_bob,self.y_bob
        if pygame.key.get_pressed()[K_w]:
            self.y_bob -= 3
            if self.y_bob <= 0:
                self.y_bob = 0
            self.rect.topleft = self.x_bob,self.y_bob
        if pygame.key.get_pressed()[K_s]:
            self.y_bob += 3
            if self.y_bob >= 440:
                self.y_bob = 440
            self.rect.topleft = self.x_bob,self.y_bob
    def update(self):
        if self.animar == True:
            self.atual += 0.05
            if self.atual >= len(self.sprites):
                self.atual = 0
                self.animar = False
            self.image = self.sprites[int(self.atual)]
            self.image = pygame.transform.scale(self.image, (40, 40))

class Alface(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load('coletaveis/alface.png'))
        self.sprites.append(pygame.image.load('coletaveis/alface2.png'))
        self.atual = 0
        self.image = self.sprites[self.atual]
        self.x = x
        self.y = y
        self.image = pygame.transform.scale(self.image, (25,25))
        self.rect = self.image.get_rect()
        self.rect.topleft = self.x,self.y

    def update(self):
        self.atual += 0.015
        if self.atual >= len(self.sprites):
            self.atual = 0
        self.image = self.sprites[int(self.atual)]
        self.image = pygame.transform.scale(self.image, (25,25))
        if self.rect.colliderect(bob.rect):
            print('oi, colidiu eu acho ')
            global alfac
            alfac += 1
            self.kill()

class Carne(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load('coletaveis/carne.png'))
        self.sprites.append(pygame.image.load('coletaveis/carne2.png'))
        self.atual = 0
        self.image = self.sprites[self.atual]
        self.x = x
        self.y = y
        self.image = pygame.transform.scale(self.image, (25,25))
        self.rect = self.image.get_rect()
        self.rect.topleft = self.x,self.y

    def update(self):
        self.atual += 0.015
        if self.atual >= len(self.sprites):
            self.atual = 0
        self.image = self.sprites[int(self.atual)]
        self.image = pygame.transform.scale(self.image, (25,25))
        if self.rect.colliderect(bob.rect):
            print('oi, colidiu eu acho ')
            global carne
            carne += 1
            self.kill()


class Pao(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load('coletaveis/pao.png'))
        self.sprites.append(pygame.image.load('coletaveis/pao2.png'))
        self.atual = 0
        self.image = self.sprites[self.atual]
        self.x = x
        self.y = y
        self.image = pygame.transform.scale(self.image, (25,25))
        self.rect = self.image.get_rect()
        self.rect.topleft = self.x,self.y

    def update(self):
        self.atual += 0.015
        if self.atual >= len(self.sprites):
            self.atual = 0
        self.image = self.sprites[int(self.atual)]
        self.image = pygame.transform.scale(self.image, (25, 25))
        if self.rect.colliderect(bob.rect):
            print('oi, colidiu eu acho ')
            global paum
            paum += 1
            self.kill()


todas_sprites = pygame.sprite.Group()
bob = Sponge()

for i in range (3):
    alface_i = Alface(randint(40,600), randint(40,420))
    todas_sprites.add(alface_i)
    carne_i = Carne(randint(40,600), randint(40,420))
    todas_sprites.add(carne_i)
    pao_i = Pao(randint(40,600), randint(40,420))
    todas_sprites.add(pao_i)

todas_sprites.add(bob)

relogio = pygame.time.Clock()
carne = alfac = paum = 0

while True:
    relogio.tick(100)
    tela.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            while True:
                relogio.tick(100)
                tela.fill((0, 110, 100))
                msg1 = f'Carne: {carne}  Alface: {alfac}   Pão:  {paum}'
                posicao = txt.render(msg1, True, (0, 255, 0))
                for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
                        exit()

                if pygame.key.get_pressed():
                    bob.posicao()

                todas_sprites.draw(tela)
                todas_sprites.update()
                tela.blit(posicao, (20, 20))
                pygame.display.flip()










