import pygame
from random import randint
import BobGroup
import PontuacaoContagem

class Plancton(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load('sprites/plancton.png'))
        self.atual = 0
        self.image = self.sprites[self.atual]
        self.image = pygame.transform.scale(self.image, (40.3, 71.5))
        self.rect = self.image.get_rect()
        self.x_planc = randint(40,600)
        self.y_planc = randint(40,420)
        self.change_position = 1
        self.rect.topleft = self.x_planc,self.y_planc

    def posicao(self):
        self.x_planc += self.change_position
        self.y_planc -= self.change_position
        if self.x_planc <= 40:
            self.x_planc += self.change_position
        if self.x_planc >= 500:
            self.x_planc -= self.change_position
        if self.y_planc <= 50:
            self.y_planc += self.change_position
        if self.y_planc >= 100:
            self.y_planc -= self.change_position
        self.rect.topleft = self.x_planc, self.y_planc
    def update(self):
        if self.rect.colliderect(BobGroup.bob.rect):
            print('Vida perdida!')
            PontuacaoContagem.vidas -= 1

