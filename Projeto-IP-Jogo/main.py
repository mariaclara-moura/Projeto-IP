import pygame
from pygame.locals import *
from sys import exit
from botoes import botao

from instrucoes import instrucoes1
from instrucoes import instrucoes2
from instrucoes import instrucoes3

import BobGroup
import PontuacaoContagem
import SpriteGroups

from SpongeSprite import Sponge

def get_font(size):
    return pygame.font.Font("MenuAssets/font.ttf", size)


def game():
    pygame.init()

    txt = pygame.font.SysFont('arial', 25, bold=True, italic=False)

    pygame.mixer.music.set_volume(1.0)
    pygame.mixer.music.load('music_bob.mp3')
    pygame.mixer.music.play(-1)

    altura = 640
    largura = 1024
    background = pygame.image.load(('fundomapa.jpg'))
    icon = pygame.image.load('sprites/bob_1.png')
    vidas = pygame.image.load('coletaveis/vidas.png')
    burguer = pygame.image.load('coletaveis/burguer1.png')
    burguer = pygame.transform.scale(burguer, (26, 26))
    vidas = pygame.transform.scale(vidas, (26, 26))
    fries = pygame.image.load('coletaveis/fries.png')
    fries = pygame.transform.scale(fries, (29, 32))
    soda = pygame.image.load('coletaveis/soda1.png')
    soda = pygame.transform.scale(soda, (22, 40))

    pygame.display.set_icon(icon)
    pygame.display.set_caption('Get the B(ob)urger!')
    relogio = pygame.time.Clock()
    status = "start"

    while True:
        if status == "game":
            tela = pygame.display.set_mode((largura, altura))
            relogio.tick(100)
            tela.blit(background, (0, 0))
            tela.blit(vidas, (218, 22))
            tela.blit(burguer, (15, 22))
            tela.blit(soda, (82, 13))
            tela.blit(fries, (145, 17))
            msg1 = f'    : {PontuacaoContagem.burguer}       : {PontuacaoContagem.refri}       :  {PontuacaoContagem.fries}       :{PontuacaoContagem.vidas}'
            posicao = txt.render(msg1, True, (0, 110, 110))
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
            if pygame.key.get_pressed():
                BobGroup.bob.posicao()
                BobGroup.plancton.posicao()

            if PontuacaoContagem.vidas == 0:
                morte = pygame.mixer.Sound('morte.wav')
                pygame.mixer.Sound.set_volume(morte, 1)
                morte.play()
                PontuacaoContagem.burguer = PontuacaoContagem.refri = PontuacaoContagem.fries = 0
                PontuacaoContagem.vidas = 3
                SpriteGroups.todas_sprites = SpriteGroups.desenhar()
                status = "gameover"
                SpriteGroups.todas_sprites.add(BobGroup.bob)
                SpriteGroups.todas_sprites.add(BobGroup.plancton)

            if PontuacaoContagem.burguer == PontuacaoContagem.fries == PontuacaoContagem.refri == 5:
                venceu = pygame.mixer.Sound('venceu.wav')
                pygame.mixer.Sound.set_volume(venceu, 1)
                venceu.play()
                PontuacaoContagem.burguer = PontuacaoContagem.refri = PontuacaoContagem.fries = 0
                PontuacaoContagem.vidas = 3
                SpriteGroups.todas_sprites = SpriteGroups.desenhar()
                status = "win"
                SpriteGroups.todas_sprites.add(BobGroup.bob)
                SpriteGroups.todas_sprites.add(BobGroup.plancton)
            SpriteGroups.todas_sprites.draw(tela)
            SpriteGroups.todas_sprites.update()
            tela.blit(posicao, (20, 20))
            pygame.display.flip()
            pygame.display.update()

        if status == "start":
            fundo = pygame.image.load("Fundos/Background.png")
            tela = pygame.display.set_mode((largura, altura))
            tela.blit(fundo, (0, 0))
            MENU_MOUSE_POS = pygame.mouse.get_pos()

            MENU_TEXT = get_font(48).render("GET THE B(OB)URGUER!", True, "#EEE8AA")
            MENU_RECT = MENU_TEXT.get_rect(center=(518, 100))

            PLAY_BUTTON = botao(image=pygame.image.load("MenuAssets/Options Rect.png"), pos=(518, 250),
                                text_input="INICIAR", font=get_font(70), base_color="#d7fcd4",
                                hovering_color="White")
            OPTIONS_BUTTON = botao(image=pygame.image.load("MenuAssets/Options Rect.png"), pos=(518, 400),
                                   text_input="OPÇÕES", font=get_font(70), base_color="#d7fcd4",
                                   hovering_color="White")
            QUIT_BUTTON = botao(image=pygame.image.load("MenuAssets/Quit Rect.png"), pos=(920, 590),
                                text_input="SAIR", font=get_font(35), base_color="#d7fcd4", hovering_color="White")

            tela.blit(MENU_TEXT, MENU_RECT)

            for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
                button.changeColor(MENU_MOUSE_POS)
                button.update(tela)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                        status = "instrucoes1"
                    if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                        options()
                    if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                        pygame.quit()
                        exit()

            pygame.display.update()

        if status == "instrucoes1":
            altura = 640
            largura = 1024
            fundo = pygame.image.load("Fundos/Background.png")
            tela = pygame.display.set_mode((largura, altura))
            tela.blit(fundo, (0, 0))
            menu_instrucao1_pos = pygame.mouse.get_pos()

            titulo = get_font(45).render("GET THE B(OB)URGUER!", True, "#EEE8AA")
            titulo_espaco = titulo.get_rect(center=(518, 100))
            tela.blit(titulo, titulo_espaco)
            historia1 = get_font(20).render("Mais uma vez a receita do tão aclamado", True, "#EEE8AA")
            historia_espaco1 = historia1.get_rect(center=(510, 240))
            tela.blit(historia1, historia_espaco1)
            historia2 = get_font(20).render("Hambúrguer de Siri está em perigo! Seu", True, "#EEE8AA")
            historia_espaco2 = historia2.get_rect(center=(510, 270))
            tela.blit(historia2, historia_espaco2)
            historia3 = get_font(20).render("trabalho, no jogo, será ajudar o Bob a ", True, "#EEE8AA")
            historia_espaco3 = historia3.get_rect(center=(510, 300))
            tela.blit(historia3, historia_espaco3)
            historia4 = get_font(20).render("coletar todos os itens dos seus pedidos", True, "#EEE8AA")
            historia_espaco4 = historia4.get_rect(center=(510, 330))
            tela.blit(historia4, historia_espaco4)
            historia5 = get_font(20).render(" e não deixar que o Plancton alcance ele.", True, "#EEE8AA")
            historia_espaco5 = historia5.get_rect(center=(510, 360))
            tela.blit(historia5, historia_espaco5)

            instrucoes = botao(image=pygame.image.load("MenuAssets/Botao Instrucoes.png"), pos=(290, 530),
                               text_input="INSTRUÇÕES", font=get_font(30), base_color="#d7fcd4",
                               hovering_color="White")
            iniciar = botao(image=pygame.image.load("MenuAssets/Botao Instrucoes.png"), pos=(718, 530),
                            text_input="JOGAR", font=get_font(30), base_color="#d7fcd4",
                            hovering_color="White")

            for button in [instrucoes, iniciar]:
                button.changeColor(menu_instrucao1_pos)
                button.update(tela)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if instrucoes.checkForInput(menu_instrucao1_pos):
                        status = "instrucoes2"
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if iniciar.checkForInput(menu_instrucao1_pos):
                        status = "game"

            pygame.display.update()

        if status == "instrucoes2":
            relogio = pygame.time.Clock()
            relogio.tick(100)
            altura = 640
            largura = 1024
            fundo = pygame.image.load("Fundos/Background.png")
            tela = pygame.display.set_mode((largura, altura))
            tela.blit(fundo, (0, 0))
            menu_instrucao2_pos = pygame.mouse.get_pos()

            titulo = get_font(45).render("INSTRUÇÕES", True, "#EEE8AA")
            titulo_espaco = titulo.get_rect(center=(518, 100))
            tela.blit(titulo, titulo_espaco)
            historia1 = get_font(20).render("Para se movimentar aperte as teclas do teclado:", True, "#EEE8AA")
            historia_espaco1 = historia1.get_rect(center=(510, 160))
            tela.blit(historia1, historia_espaco1)
            historia2 = get_font(20).render(" W, A, S, D", True, "#EEE8AA")
            historia_espaco2 = historia2.get_rect(center=(510, 190))
            tela.blit(historia2, historia_espaco2)

            seguinte = botao(image=pygame.image.load("MenuAssets/Botao Instrucoes.png"), pos=(518, 530),
                             text_input="SEGUINTE", font=get_font(30), base_color="#d7fcd4",
                             hovering_color="White")


            for button in [seguinte]:
                button.changeColor(menu_instrucao2_pos)
                button.update(tela)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if seguinte.checkForInput(menu_instrucao2_pos):
                        status = "instrucoes3"
                if pygame.key.get_pressed():
                    BobGroup.bob_menu.posicao_menu()

            SpriteGroups.bob_menu.draw(tela)
            SpriteGroups.bob_menu.update()
            pygame.display.flip()
            pygame.display.update()

        if status == "instrucoes3":
            altura = 640
            largura = 1024
            fundo = pygame.image.load("Fundos/Background.png")
            tela = pygame.display.set_mode((largura, altura))
            tela.blit(fundo, (0, 0))
            menu_instrucao3_pos = pygame.mouse.get_pos()

            titulo = get_font(45).render("INSTRUÇÕES", True, "#EEE8AA")
            titulo_espaco = titulo.get_rect(center=(518, 100))
            tela.blit(titulo, titulo_espaco)
            historia1 = get_font(20).render("Mais uma vez a receita do tão aclamado", True, "#EEE8AA")
            historia_espaco1 = historia1.get_rect(center=(510, 160))
            tela.blit(historia1, historia_espaco1)
            historia2 = get_font(20).render("Hambúrguer de Siri está em perigo! Seu", True, "#EEE8AA")
            historia_espaco2 = historia2.get_rect(center=(510, 190))
            tela.blit(historia2, historia_espaco2)

            anterior = botao(image=pygame.image.load("MenuAssets/Botao Instrucoes.png"), pos=(290, 530),
                             text_input="ANTERIOR", font=get_font(30), base_color="#d7fcd4",
                             hovering_color="White")
            jogar = botao(image=pygame.image.load("MenuAssets/Botao Instrucoes.png"), pos=(718, 530),
                          text_input="JOGAR", font=get_font(30), base_color="#d7fcd4",
                          hovering_color="White")

            for button in [anterior, jogar]:
                button.changeColor(menu_instrucao3_pos)
                button.update(tela)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if anterior.checkForInput(menu_instrucao3_pos):
                        status = "instrucoes2"
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if jogar.checkForInput(menu_instrucao3_pos):
                        status = "game"
            pygame.display.update()

        if status == "win":
            tela = pygame.display.set_mode((largura, altura))
            OPTIONS_MOUSE_POS = pygame.mouse.get_pos()
            tela.blit(fundo, (0, 0))

            OPTIONS_TEXT = get_font(45).render("Você ganhou!!", True, "Black")
            OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(518, 260))
            tela.blit(OPTIONS_TEXT, OPTIONS_RECT)

            OPTIONS_BACK = botao(image=None, pos=(518, 460),
                                 text_input="Voltar", font=get_font(70), base_color="Black", hovering_color="Green")

            OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
            OPTIONS_BACK.update(tela)

            for button in [OPTIONS_BACK]:
                button.changeColor(OPTIONS_MOUSE_POS)
                button.update(tela)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                        status = "start"
            pygame.display.update()

        if status == "gameover":
            tela = pygame.display.set_mode((largura, altura))
            OPTIONS_MOUSE_POS = pygame.mouse.get_pos()
            tela.blit(fundo, (0, 0))

            texto_gameover = get_font(45).render("GAME OVER", True, "Black")
            OPTIONS_RECT = texto_gameover.get_rect(center=(518, 260))
            tela.blit(texto_gameover, OPTIONS_RECT)

            OPTIONS_BACK = botao(image=None, pos=(518, 460),
                                 text_input="Tente de novo", font=get_font(70), base_color="Black",
                                 hovering_color="Green")

            OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
            OPTIONS_BACK.update(tela)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                        status = "start"


            pygame.display.update()

        pygame.display.update()


if __name__ == '__main__':
    game()