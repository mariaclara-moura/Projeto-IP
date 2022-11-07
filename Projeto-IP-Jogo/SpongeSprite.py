#realizando as importações necessárias
import pygame
from pygame.locals import *

# definindo a sprite do Bob:
class Sponge(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load('sprites/bob_1.png'))
        self.sprites.append(pygame.image.load('sprites/bob_2.png'))
        self.atual = 0
        self.image = self.sprites[self.atual]
        self.image = pygame.transform.scale(self.image, (44, 44))
        self.rect = self.image.get_rect()
        self.x_bob = 100
        self.y_bob = 55
        self.rect.topleft = self.x_bob,self.y_bob
        self.animar = False

    # função que define a posição do Bob:
    def posicao(self):
        self.animar = True
        # modificando as coordenadas do Bob de acordo com a tecla pressionada no teclado (w, a, s, d):
        if pygame.key.get_pressed()[K_a]:
            self.x_bob -= 3
            if (self.x_bob <= 65 and self.x_bob >= 62) and self.y_bob <= 185:
                self.x_bob = 65
            if self.x_bob <= 20:
                self.x_bob = 20
            self.rect.topleft = self.x_bob, self.y_bob
        if pygame.key.get_pressed()[K_d]:
            self.x_bob +=3
            if self.x_bob >= 980:
                self.x_bob = 980
            self.rect.topleft = self.x_bob,self.y_bob
        if pygame.key.get_pressed()[K_w]:
            self.y_bob -= 3
            if (self.y_bob <= 185 and self.y_bob >= 182) and self.x_bob <= 65:
                self.y_bob = 185
            if self.y_bob <= 20:
                self.y_bob = 20
            self.rect.topleft = self.x_bob,self.y_bob
        if pygame.key.get_pressed()[K_s]:
            self.y_bob += 3
            if self.y_bob >= 580:
                self.y_bob = 580
            self.rect.topleft = self.x_bob,self.y_bob

    # atualizando a sprite:
    def update(self):
        if self.animar == True:
            self.atual += 0.03
            if self.atual >= len(self.sprites):
                self.atual = 0
                self.animar = False
            self.image = self.sprites[int(self.atual)]
            self.image = pygame.transform.scale(self.image, (44, 44))