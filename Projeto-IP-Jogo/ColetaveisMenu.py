#realizando as importações necessárias
import pygame
import BobGroup

# criando a sprite da batatinha e a colocando no menu como um ítem (definindo coordenadas para localização
# e definindo sua escala/tamanho)
class FriesMenu(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load('coletaveis/fries.png'))
        self.sprites.append(pygame.image.load('coletaveis/fries2.png'))
        self.atual = 0
        self.image = self.sprites[self.atual]
        self.x = 600
        self.y = 348
        self.image = pygame.transform.scale(self.image, (29,31))
        self.rect = self.image.get_rect()
        self.rect.topleft = self.x,self.y

    # atualizando a sprite
    def update(self):
        self.atual += 0.015
        if self.atual >= len(self.sprites):
            self.atual = 0
        self.image = self.sprites[int(self.atual)]
        self.image = pygame.transform.scale(self.image, (29, 31))
        if self.rect.colliderect(BobGroup.menus.bob_menu2.rect):
            print('Batatinha Coletada!')
            coletou = pygame.mixer.Sound('sons/temacoletados.wav')
            pygame.mixer.Sound.set_volume(coletou, 0.2)
            coletou.play()
            self.kill()

# criando a sprite do hamburguer e a colocando no menu como um ítem (definindo coordenadas para localização
# e definindo sua escala/tamanho)
class BurguerMenu(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load('coletaveis/burguer1.png'))
        self.sprites.append(pygame.image.load('coletaveis/burguer2.png'))
        self.atual = 0
        self.image = self.sprites[self.atual]
        self.x = 700
        self.y = 350
        self.image = pygame.transform.scale(self.image, (28,28))
        self.rect = self.image.get_rect()
        self.rect.topleft = self.x,self.y

    # atualizando a sprite
    def update(self):
        self.atual += 0.015
        if self.atual >= len(self.sprites):
            self.atual = 0
        self.image = self.sprites[int(self.atual)]
        self.image = pygame.transform.scale(self.image, (28,28))
        if self.rect.colliderect(BobGroup.menus.bob_menu2.rect):
            print('Burguer Coletado!')
            coletou = pygame.mixer.Sound('sons/temacoletados.wav')
            pygame.mixer.Sound.set_volume(coletou, 0.2)
            coletou.play()
            self.kill()

# criando a sprite do refri e a colocando no menu como um ítem (definindo coordenadas para localização
# e definindo sua escala/tamanho)
class RefriMenu(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load('coletaveis/soda1.png'))
        self.sprites.append(pygame.image.load('coletaveis/soda2.png'))
        self.atual = 0
        self.image = self.sprites[self.atual]
        self.x = 500
        self.y = 350
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
        if self.rect.colliderect(BobGroup.menus.bob_menu2.rect):
            print('Refri Coletado!')
            coletou = pygame.mixer.Sound('sons/temacoletados.wav')
            pygame.mixer.Sound.set_volume(coletou, 0.2)
            coletou.play()
            self.kill()