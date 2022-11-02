import pygame, sys
from botoes import botao

pygame.init()
# definindo tela e o nome do jogo
tela = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Get The B(ob)urger")

fundo = pygame.image.load("Fundos/Background.png")

# função que retorna uma fonte de escrita a ser utilizada:
def get_font(size):
    return pygame.font.Font("MenuAssets/font.ttf", size)


def play():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        tela.fill("black")

        PLAY_TEXT = get_font(45).render("Tela do jogo", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 260))
        tela.blit(PLAY_TEXT, PLAY_RECT)

        PLAY_BACK = botao(image=None, pos=(640, 460),
                           text_input="Voltar", font=get_font(75), base_color="White", hovering_color="Green")

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(tela)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()

        pygame.display.update()


def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        tela.fill("white")

        OPTIONS_TEXT = get_font(45).render("Tela das opções", True, "Black")
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
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()

        pygame.display.update()


def main_menu():
    while True:
        tela.blit(fundo, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(55).render("GET THE B(OB)URGUER!", True, "#EEE8AA")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        PLAY_BUTTON = botao(image=pygame.image.load("MenuAssets/Options Rect.png"), pos=(640, 250),
                             text_input="INICIAR", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = botao(image=pygame.image.load("MenuAssets/Options Rect.png"), pos=(640, 400),
                                text_input="OPÇÕES", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = botao(image=pygame.image.load("MenuAssets/Quit Rect.png"), pos=(1120, 650),
                             text_input="SAIR", font=get_font(38), base_color="#d7fcd4", hovering_color="White")

        tela.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(tela)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    game()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

main_menu()