#realizando as importações necessárias
import pygame
import BobGroup
import PontuacaoContagem

# determinando a sprite do plankton do menu:
class PlanctonMenu(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load('sprites/plancton.png'))
        self.atual = 0
        self.image = self.sprites[self.atual]
        self.image = pygame.transform.scale(self.image, (40.3, 71.5))
        self.rect = self.image.get_rect()
        self.x_planc = 700
        self.y_planc = 300
        self.change_position = 1.5
        self.rect.topleft = self.x_planc,self.y_planc
        self.colidiu = False
        self.ida_horizontal = True
        self.ida_vertical = False

    # atualizando sprite e computando colisão
    def update(self):
        # perdendo 1 vida quando o Bob colide com o plankton
        if self.rect.colliderect(BobGroup.menus.bob_menu3.rect) and (self.colidiu == False):
            print('Vida perdida!')
            PontuacaoContagem.status_menu = "PERDEU A VIDA"
            perdeu = pygame.mixer.Sound('sons/inimigo.wav')
            pygame.mixer.Sound.set_volume(perdeu, 0.2)
            perdeu.play()
            self.colidiu = True
        # caso contrário:
        if not self.rect.colliderect(BobGroup.menus.bob_menu3.rect):
            self.colidiu = False