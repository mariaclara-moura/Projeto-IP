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
        self.x_planc = randint(40,980)
        self.y_planc = randint(40,600)
        self.change_position = 1.5
        self.rect.topleft = self.x_planc,self.y_planc
        self.colidiu = False
        self.ida_horizontal = True
        self.ida_vertical = False

    def subindo(self):
        self.y_planc += self.change_position
        if self.y_planc >= 560:
            self.ida_vertical = False
        return self
    def descendo(self):
        self.y_planc -= self.change_position
        if self.y_planc <= 0:
            self.ida_vertical = True
        return self
    def direita(self):
        self.x_planc += self.change_position
        if self.x_planc >= 980:
            self.ida_horizontal = False
        return self
    def esquerda(self):
        self.x_planc -= self.change_position
        if self.x_planc <= 0:
            self.ida_horizontal = True
        return self
    def posicao(self):
        if self.ida_horizontal:
            Plancton.direita(BobGroup.plancton)
        else:
            Plancton.esquerda(BobGroup.plancton)
        if self.ida_vertical:
            Plancton.subindo(BobGroup.plancton)
        else:
            Plancton.descendo(BobGroup.plancton)
        self.rect.topleft = self.x_planc, self.y_planc

    def update(self):
        if self.rect.colliderect(BobGroup.bob.rect) and (self.colidiu == False):
            print('Vida perdida!')
            PontuacaoContagem.vidas -= 1
            perdeu = pygame.mixer.Sound('inimigo.wav')
            pygame.mixer.Sound.set_volume(perdeu, 0.2)
            perdeu.play()
            self.colidiu = True

        if not self.rect.colliderect(BobGroup.bob.rect):
            self.colidiu = False