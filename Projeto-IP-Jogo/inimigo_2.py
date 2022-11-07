#realizando as importações necessárias
import pygame
from random import randint
import BobGroup
import PontuacaoContagem

# determinando a sprite do segundo inimigo:
class Plancton_2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        for i in range(16):
            self.sprites.append(pygame.image.load(f'sprites/inimigo_2/{i}.png'))
        self.atual = 0
        self.image = self.sprites[self.atual]
        self.image = pygame.transform.scale(self.image, (40.3, 71.5))
        self.rect = self.image.get_rect()
        self.x_planc = randint(65, 980)
        self.y_planc = randint(20, 580)
        self.change_position = 2
        self.rect.topleft = self.x_planc, self.y_planc
        self.colidiu = False
        self.ida_horizontal = True
        self.ida_vertical = False

    # definindo funções que mudam a direção do inimigo quando ele atinge os cantos da tela:
    # ("subindo", "descendo", "direita" e "esquerda")
    def subindo(self):
        self.y_planc += self.change_position
        if self.y_planc >= 530:
            self.ida_vertical = False
        return self
    def descendo(self):
        self.y_planc -= self.change_position
        if (self.y_planc <= 185 and self.y_planc >= 183) and self.x_planc <= 65:
            self.ida_vertical = True
        elif self.y_planc <= 0:
            self.ida_vertical = True
        return self
    def direita(self):
        self.x_planc += self.change_position
        if self.x_planc >= 900:
            self.ida_horizontal = False
        return self
    def esquerda(self):
        self.x_planc -= self.change_position
        if (self.x_planc <= 65 and self.x_planc >= 63) and self.y_planc <= 185:
            self.ida_horizontal = True
        elif self.x_planc <= 0:
            self.ida_horizontal = True
        return self
    # verifica a condição do inimigo e chama as funções anteriores, de mudar de direção, quando necessário:
    def posicao(self):
        if self.ida_horizontal:
            Plancton_2.direita(BobGroup.personagens.plancton2)
        else:
            Plancton_2.esquerda(BobGroup.personagens.plancton2)
        if self.ida_vertical:
            Plancton_2.subindo(BobGroup.personagens.plancton2)
        else:
            Plancton_2.descendo(BobGroup.personagens.plancton2)
        self.rect.topleft = self.x_planc, self.y_planc

    # atualizando sprite e computando colisão
    def update(self):
        self.atual += 0.05
        if self.atual >= len(self.sprites):
            self.atual = 0
        self.image = self.sprites[int(self.atual)]
        self.image = pygame.transform.scale(self.image, (120, 120))
        # perdendo 1 vida quando o Bob colide com o inimigo
        if self.rect.colliderect(BobGroup.personagens.bob.rect) and (self.colidiu == False):
            print('Vida perdida!')
            PontuacaoContagem.vidas -= 1
            perdeu = pygame.mixer.Sound('sons/inimigo.wav')
            pygame.mixer.Sound.set_volume(perdeu, 0.2)
            perdeu.play()
            self.colidiu = True
        # caso contrário:
        if not self.rect.colliderect(BobGroup.personagens.bob.rect):
            self.colidiu = False