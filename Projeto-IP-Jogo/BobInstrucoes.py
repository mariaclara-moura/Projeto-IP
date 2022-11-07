#realizando as importações necessárias
import pygame
from pygame.locals import *

#criando as sprites dos bob's que serão utilizados na primeira tela de instruções
class BobMenu(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load('sprites/bob_1.png'))
        self.sprites.append(pygame.image.load('sprites/bob_2.png'))
        self.atual = 0
        self.image = self.sprites[self.atual]
        self.image = pygame.transform.scale(self.image, (44, 44))

        self.rect = self.image.get_rect()
        self.x_bob = 200
        self.y_bob = 350
        self.rect.topleft = self.x_bob,self.y_bob
        self.animar = False

 # modificando as coordenadas do Bob de acordo com a tecla pressionada no teclado (w, a, s, d):
    def posicao_menu(self):
        self.animar = True
        if pygame.key.get_pressed()[K_a]:
            self.x_bob -= 10
            if self.x_bob <= 200:
                self.x_bob = 200
            self.rect.topleft = self.x_bob, self.y_bob
        if pygame.key.get_pressed()[K_d]:
            self.x_bob += 10
            if self.x_bob >= 770:
                self.x_bob = 770
            self.rect.topleft = self.x_bob,self.y_bob
        if pygame.key.get_pressed()[K_w]:
            self.y_bob -= 10
            if self.y_bob <= 300:
                self.y_bob = 300
            self.rect.topleft = self.x_bob,self.y_bob
        if pygame.key.get_pressed()[K_s]:
            self.y_bob += 10
            if self.y_bob >= 440:
                self.y_bob = 440
            self.rect.topleft = self.x_bob,self.y_bob

    # atualizando a sprite:
    def update(self):
        if self.animar == True:
            self.atual += 0.05
            if self.atual >= len(self.sprites):
                self.atual = 0
                self.animar = False
            self.image = self.sprites[int(self.atual)]
            self.image = pygame.transform.scale(self.image, (44, 44))

#criando as sprites dos bob's que serão utilizados na segunda tela de instruções
class BobMenu2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load('sprites/bob_1.png'))
        self.sprites.append(pygame.image.load('sprites/bob_2.png'))
        self.atual = 0
        self.image = self.sprites[self.atual]
        self.image = pygame.transform.scale(self.image, (44, 44))

        self.rect = self.image.get_rect()
        self.x_bob = 200
        self.y_bob = 320
        self.rect.topleft = self.x_bob,self.y_bob
        self.animar = False

    # modificando as coordenadas do Bob de acordo com a tecla pressionada no teclado (w, a, s, d):
    def posicao_menu(self):
        self.animar = True
        if pygame.key.get_pressed()[K_a]:
            self.x_bob -= 10
            if self.x_bob <= 200:
                self.x_bob = 200
            self.rect.topleft = self.x_bob, self.y_bob
        if pygame.key.get_pressed()[K_d]:
            self.x_bob += 10
            if self.x_bob >= 770:
                self.x_bob = 770
            self.rect.topleft = self.x_bob, self.y_bob
        if pygame.key.get_pressed()[K_w]:
            self.y_bob -= 10
            if self.y_bob <= 220:
                self.y_bob = 220
            self.rect.topleft = self.x_bob, self.y_bob
        if pygame.key.get_pressed()[K_s]:
            self.y_bob += 10
            if self.y_bob >= 440:
                self.y_bob = 440
            self.rect.topleft = self.x_bob, self.y_bob

    # atualizando a sprite:
    def update(self):
        if self.animar == True:
            self.atual += 0.05
            if self.atual >= len(self.sprites):
                self.atual = 0
                self.animar = False
            self.image = self.sprites[int(self.atual)]
            self.image = pygame.transform.scale(self.image, (44, 44))

#criando as sprites dos bob's que serão utilizados na primeira tela de instruções
class BobMenu3(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load('sprites/bob_1.png'))
        self.sprites.append(pygame.image.load('sprites/bob_2.png'))
        self.atual = 0
        self.image = self.sprites[self.atual]
        self.image = pygame.transform.scale(self.image, (44, 44))

        self.rect = self.image.get_rect()
        self.x_bob = 200
        self.y_bob = 320
        self.rect.topleft = self.x_bob,self.y_bob
        self.animar = False

    # modificando as coordenadas do Bob de acordo com a tecla pressionada no teclado (w, a, s, d):
    def posicao_menu(self):
        self.animar = True
        if pygame.key.get_pressed()[K_a]:
            self.x_bob -= 10
            if self.x_bob <= 200:
                self.x_bob = 200
            self.rect.topleft = self.x_bob, self.y_bob
        if pygame.key.get_pressed()[K_d]:
            self.x_bob += 10
            if self.x_bob >= 770:
                self.x_bob = 770
            self.rect.topleft = self.x_bob, self.y_bob
        if pygame.key.get_pressed()[K_w]:
            self.y_bob -= 10
            if self.y_bob <= 260:
                self.y_bob = 260
            self.rect.topleft = self.x_bob, self.y_bob
        if pygame.key.get_pressed()[K_s]:
            self.y_bob += 10
            if self.y_bob >= 440:
                self.y_bob = 440
            self.rect.topleft = self.x_bob, self.y_bob

    # atualizando a sprite:
    def update(self):
        if self.animar == True:
            self.atual += 0.05
            if self.atual >= len(self.sprites):
                self.atual = 0
                self.animar = False
            self.image = self.sprites[int(self.atual)]
            self.image = pygame.transform.scale(self.image, (44, 44))