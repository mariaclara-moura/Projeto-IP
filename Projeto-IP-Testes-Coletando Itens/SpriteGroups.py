import pygame
from random import randint
import AlfaceSprite
import CarneSprite
import PaoSprite


todas_sprites = pygame.sprite.Group()
for i in range(5):
    alface_i = AlfaceSprite.Alface(randint(40, 600), randint(40, 420))
    todas_sprites.add(alface_i)
    carne_i = CarneSprite.Carne(randint(40, 600), randint(40, 420))
    todas_sprites.add(carne_i)
    pao_i = PaoSprite.Pao(randint(40, 600), randint(40, 420))
    todas_sprites.add(pao_i)
