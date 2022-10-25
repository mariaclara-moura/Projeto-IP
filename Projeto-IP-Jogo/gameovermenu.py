import pygame, sys
from botoes import botao
import main

pygame.init()

tela = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Game Over")
fundo = pygame.image.load("Fundos/Background.png")


def get_font(size):
    return pygame.font.Font("MenuAssets/font.ttf", size)


def gameover():
    while True:
        tela = pygame.display.set_mode((1280, 720))
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()
        tela.blit(fundo, (0, 0))


        texto_gameover = get_font(45).render("GAME OVER", True, "Black")
        OPTIONS_RECT = texto_gameover.get_rect(center=(640, 260))
        tela.blit(texto_gameover, OPTIONS_RECT)

        OPTIONS_BACK = botao(image=None, pos=(640, 460),
                              text_input="Tente de novo", font=get_font(75), base_color="Black", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(tela)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main.game()

        pygame.display.update()