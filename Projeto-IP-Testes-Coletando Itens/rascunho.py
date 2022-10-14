import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()

altura = 480
largura = 640


tela = pygame.display.set_mode((largura,altura))
pygame.display.set_caption('Bob Esponja')

class Sponge(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load('sprites/bob_1.png'))
        self.sprites.append(pygame.image.load('sprites/bob_2.png'))
        
        self.atual = 0
        self.image = self.sprites[self.atual]
        self.image = pygame.transform.scale(self.image, (50, 50))

        self.rect = self.image.get_rect()
        self.x_bob = 100
        self.y_bob = 100
        self.rect.topleft = self.x_bob,self.y_bob
        self.animar = False

    def posicao(self):
        self.animar = True
        if pygame.key.get_pressed()[K_a]: 
            self.x_bob -= 10 
            if self.x_bob <= 0:
                self.x_bob = 0
            self.rect.topleft = self.x_bob,self.y_bob
        if pygame.key.get_pressed()[K_d]:
            self.x_bob += 10
            if self.x_bob >= 580:
                self.x_bob = 580
            self.rect.topleft = self.x_bob,self.y_bob
        if pygame.key.get_pressed()[K_w]:
            self.y_bob -= 10
            if self.y_bob <= 0:
                self.y_bob = 0
            self.rect.topleft = self.x_bob,self.y_bob
        if pygame.key.get_pressed()[K_s]:
            self.y_bob += 10
            if self.y_bob >= 400:
                self.y_bob = 400
            self.rect.topleft = self.x_bob,self.y_bob

    def update(self):
        if self.animar == True:
            self.atual += 0.25
            if self.atual >= len(self.sprites):
                self.atual = 0 
                self.animar = False
            self.image = self.sprites[int(self.atual)]
            self.image = pygame.transform.scale(self.image, (50, 50))


todas_sprites = pygame.sprite.Group()
bob = Sponge()
todas_sprites.add(bob)

class Coletaveis():
    def __init__(self):
        self.image1 = pygame.image.load('coletaveis/alface.png')
        self.image2 = pygame.image.load('coletaveis/carne.png')
        self.image3 = pygame.image.load('coletaveis/pao.png')

        self.x_i = randint(30,100)
        self.y_i = randint(20,50)
        self.x_j = randint(10,130)
        self.y_j = randint(60,80)
        self.x_k = randint(0,100)
        self.y_k = randint(20,50)

    def desenhar(self):
            tela.blit(self.image1,(self.x_i,self.y_i)) 
            tela.blit(self.image2,(self.x_j,self.y_j)) 
            tela.blit(self.image3,(self.x_k,self.y_k)) 

coletaveis = Coletaveis()     

relogio = pygame.time.Clock()

while True:
    relogio.tick(30)
    tela.fill((0,110,100))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        
        if pygame.key.get_pressed()[K_a] or pygame.key.get_pressed()[K_d] or pygame.key.get_pressed()[K_w] or pygame.key.get_pressed()[K_s]:  
            bob.posicao()
    
    coletaveis.desenhar()
    todas_sprites.draw(tela)
    todas_sprites.update()
    pygame.display.flip()