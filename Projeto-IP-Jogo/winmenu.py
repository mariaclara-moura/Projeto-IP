import pygame, sys
from botoes import botao

pygame.init()

tela = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Você Conseguiu!!")
fundo = pygame.image.load("Fundos/Background.png")


def get_font(size):
    return pygame.font.Font("MenuAssets/font.ttf", size)


def win():
    while True:
        tela = pygame.display.set_mode((1280, 720))
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()
        tela.blit(fundo, (0, 0))


        OPTIONS_TEXT = get_font(45).render("Você ganhou!!", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
        tela.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = botao(image=None, pos=(640, 460),
                              text_input="Voltar", font=get_font(75), base_color="Black", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(tela)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()