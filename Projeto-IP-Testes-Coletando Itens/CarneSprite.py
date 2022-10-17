import pygame
import BobGroup
import PontuacaoContagem


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
        if self.rect.colliderect(BobGroup.bob.rect):
            print('Carne Coletada!')
            PontuacaoContagem.carne += 1
            self.kill()