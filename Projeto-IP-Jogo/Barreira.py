import pygame
import BobGroup


class BARREIRA(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load('foto_alga.png'))
        self.atual = 0
        self.image = self.sprites[self.atual]
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect()
        self.x_alga = 100
        self.y_alga = 100
        self.rect = self.image.get_rect()
        self.rect.topleft = self.x_alga, self.y_alga

    def update(self):
        self.atual += 0.015
        if self.atual >= len(self.sprites):
            self.atual = 0
        self.image = self.sprites[int(self.atual)]
        self.image = pygame.transform.scale(self.image, (25, 25))
        if self.rect.colliderect(BobGroup.bob.rect):
            print('Bob cruzou com a alga!')
            # Colisão a ser ajustada:
            pass
