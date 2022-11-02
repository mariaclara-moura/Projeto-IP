import pygame
import BobGroup
import PontuacaoContagem

# pegando a imagem da soda e a colocando no jogo como um ítem (definindo coordenadas para localização
# e definindo sua escala/tamanho
class Refri(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load('coletaveis/soda1.png'))
        self.sprites.append(pygame.image.load('coletaveis/soda2.png'))
        self.atual = 0
        self.image = self.sprites[self.atual]
        self.x = x
        self.y = y
        self.image = pygame.transform.scale(self.image, (25,40))
        self.rect = self.image.get_rect()
        self.rect.topleft = self.x,self.y

    # atualizando a sprite
    def update(self):
        self.atual += 0.015
        if self.atual >= len(self.sprites):
            self.atual = 0
        self.image = self.sprites[int(self.atual)]
        self.image = pygame.transform.scale(self.image, (25,40))
        # se o bob colidir com a soda, a sprite é eliminada
        if self.rect.colliderect(BobGroup.bob.rect):
            print('Refri Coletado!')
            coletou = pygame.mixer.Sound('sons/temacoletados.wav')
            pygame.mixer.Sound.set_volume(coletou, 0.2)
            coletou.play()
            PontuacaoContagem.refri += 1
            self.kill()