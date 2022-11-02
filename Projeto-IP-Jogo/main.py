import pygame
from pygame.locals import *
from sys import exit
from botoes import botao

import BobGroup
import PontuacaoContagem
import SpriteGroups

def get_font(size):
    return pygame.font.Font("MenuAssets/font.ttf", size)


def game():
    global fase
    fase = 0
    pygame.init()

    txt = pygame.font.SysFont('arial', 25, bold=True, italic=False)

  #  pygame.mixer.music.set_volume(1.0)
  #  pygame.mixer.music.load('sons\music_bob.mp3')
  #  pygame.mixer.music.play(-1)

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

    # looping principal do jogo:
    while True:
        if status == "game":
            tela = pygame.display.set_mode((largura, altura))
            relogio.tick(100)
            tela.blit(background, (0, 0))
            tela.blit(vidas, (15, 162))
            tela.blit(burguer, (15, 22))
            tela.blit(soda, (15, 59))
            tela.blit(fries, (15, 112))
            msg1 = f'       : {PontuacaoContagem.burguer}'
            msg2 = f'       : {PontuacaoContagem.refri}'
            msg3 = f'       : {PontuacaoContagem.fries}'
            msg4 = f'       : {PontuacaoContagem.vidas}'
            posicao = txt.render(msg1, True, (250, 0, 90))
            posicao2 = txt.render(msg2, True, (250, 0, 90))
            posicao3 = txt.render(msg3, True, (250, 0, 90))
            posicao4 = txt.render(msg4, True, (250, 0, 90))

            for event in pygame.event.get():
                # condição para sair do jogo
                if event.type == QUIT:
                    pygame.quit()
                    exit()
            # retornando as funções de determinação das posições do bob e do plankton:
            if pygame.key.get_pressed():
                BobGroup.bob.posicao()
                BobGroup.plancton.posicao()
                if fase == 2:
                    BobGroup.plancton2.posicao()


            # se as vidas acabarem e o jogador perder o jogo:
            # definindo som a ser emitido
            # novo status
            if PontuacaoContagem.vidas == 0:
                morte = pygame.mixer.Sound('sons/morte.wav')
                pygame.mixer.Sound.set_volume(morte, 1)
                morte.play()
                PontuacaoContagem.burguer = PontuacaoContagem.refri = PontuacaoContagem.fries = 0
                PontuacaoContagem.vidas = 3
                SpriteGroups.todas_sprites = SpriteGroups.desenhar()
                status = "gameover"
                SpriteGroups.todas_sprites.add(BobGroup.bob)
                SpriteGroups.todas_sprites.add(BobGroup.plancton)
                SpriteGroups.todas_sprites.add(BobGroup.plancton2)

            # se coletar todos os itens e vencer:
            # definindo som
            # novo status
            if (PontuacaoContagem.burguer == PontuacaoContagem.fries == PontuacaoContagem.refri == 5) and fase != 2:
                venceu = pygame.mixer.Sound('sons/venceu.wav')
                pygame.mixer.Sound.set_volume(venceu, 1)
                venceu.play()
                PontuacaoContagem.burguer = PontuacaoContagem.refri = PontuacaoContagem.fries = 0
                PontuacaoContagem.vidas = 3
                SpriteGroups.todas_sprites = SpriteGroups.desenhar()
                status = "fase_2"
                SpriteGroups.todas_sprites.add(BobGroup.bob)
                SpriteGroups.todas_sprites.add(BobGroup.plancton)
            SpriteGroups.todas_sprites.draw(tela)
            SpriteGroups.todas_sprites.update()
            tela.blit(posicao, (3, 20))
            tela.blit(posicao2, (3, 70))
            tela.blit(posicao3, (3, 115))
            tela.blit(posicao4, (3, 160))
            pygame.display.flip()
            pygame.display.update()

            if (PontuacaoContagem.burguer == PontuacaoContagem.fries == PontuacaoContagem.refri == 5) and fase == 2:
                venceu = pygame.mixer.Sound('sons/venceu.wav')
                pygame.mixer.Sound.set_volume(venceu, 1)
                venceu.play()
                PontuacaoContagem.burguer = PontuacaoContagem.refri = PontuacaoContagem.fries = 0
                PontuacaoContagem.vidas = 3
                SpriteGroups.todas_sprites = SpriteGroups.desenhar()
                status = "win"
                SpriteGroups.todas_sprites.add(BobGroup.bob)
                SpriteGroups.todas_sprites.add(BobGroup.plancton)
                SpriteGroups.todas_sprites.add(BobGroup.plancton2)


            SpriteGroups.todas_sprites.draw(tela)
            SpriteGroups.todas_sprites.update()
            tela.blit(posicao, (3, 20))
            tela.blit(posicao2, (3, 70))
            tela.blit(posicao3, (3, 115))
            tela.blit(posicao4, (3, 160))
            pygame.display.flip()
            pygame.display.update()

        if status == "fase_2":
            altura = 640
            largura = 1024
            fundo = pygame.image.load("Fundos/Background.png")
            tela = pygame.display.set_mode((largura, altura))
            tela.blit(fundo, (0, 0))
            menu_inicial_pos = pygame.mouse.get_pos()

            titulo = get_font(45).render("GET THE B(OB)URGUER!", True, "#EEE8AA")
            titulo_espaco = titulo.get_rect(center=(518, 100))
            tela.blit(titulo, titulo_espaco)
            historia1 = get_font(20).render("Parabéns!!! Você conseguiu completar o ", True, "#EEE8AA")
            historia_espaco1 = historia1.get_rect(center=(510, 240))
            tela.blit(historia1, historia_espaco1)
            historia2 = get_font(20).render("pedido sem que o Plankton o pegasse.", True, "#EEE8AA")
            historia_espaco2 = historia2.get_rect(center=(510, 270))
            tela.blit(historia2, historia_espaco2)
            historia3 = get_font(20).render("Mas agora a situação está ficando cada ", True, "#EEE8AA")
            historia_espaco3 = historia3.get_rect(center=(510, 300))
            tela.blit(historia3, historia_espaco3)
            historia4 = get_font(20).render("vez mais difícil. O siri Cascudo conta", True, "#EEE8AA")
            historia_espaco4 = historia4.get_rect(center=(510, 330))
            tela.blit(historia4, historia_espaco4)
            historia5 = get_font(20).render("com a sua ajuda. Aceita o desafio?", True, "#EEE8AA")
            historia_espaco5 = historia5.get_rect(center=(510, 360))
            tela.blit(historia5, historia_espaco5)

            voltar = botao(image=pygame.image.load("MenuAssets/Botao Instrucoes.png"), pos=(290, 530),
                               text_input="VOLTAR", font=get_font(30), base_color="#d7fcd4",
                               hovering_color="White")
            iniciar = botao(image=pygame.image.load("MenuAssets/Botao Instrucoes.png"), pos=(718, 530),
                            text_input="FASE 2", font=get_font(30), base_color="#d7fcd4",
                            hovering_color="White")
            fase = 2
            for button in [voltar, iniciar]:
                button.changeColor(menu_inicial_pos)
                button.update(tela)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if voltar.checkForInput(menu_inicial_pos):
                        status = "start"
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if iniciar.checkForInput(menu_inicial_pos):
                        status = "game"
                        SpriteGroups.todas_sprites.add(BobGroup.plancton2)



            pygame.display.update()

        if status == "start":
            fundo = pygame.image.load("Fundos/Background.png")
            tela = pygame.display.set_mode((largura, altura))
            tela.blit(fundo, (0, 0))
            MENU_MOUSE_POS = pygame.mouse.get_pos()

            MENU_TEXT = get_font(48).render("GET THE B(OB)URGUER!", True, "#EEE8AA")
            MENU_RECT = MENU_TEXT.get_rect(center=(518, 100))

            PLAY_BUTTON = botao(image=pygame.image.load("MenuAssets/Options Rect.png"), pos=(518, 350),
                                text_input="INICIAR", font=get_font(70), base_color="#d7fcd4",
                                hovering_color="White")
            QUIT_BUTTON = botao(image=pygame.image.load("MenuAssets/Quit Rect.png"), pos=(920, 590),
                                text_input="SAIR", font=get_font(35), base_color="#d7fcd4", hovering_color="White")

            tela.blit(MENU_TEXT, MENU_RECT)

            for button in [PLAY_BUTTON, QUIT_BUTTON]:
                button.changeColor(MENU_MOUSE_POS)
                button.update(tela)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                        status = "instrucoes1"
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
            historia5 = get_font(20).render(" e não deixar que o Plancton o alcance.", True, "#EEE8AA")
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

            seguinte = botao(image=pygame.image.load("MenuAssets/Botao Instrucoes.png"), pos=(518, 530),
                             text_input="SEGUINTE", font=get_font(30), base_color="#d7fcd4",
                             hovering_color="White")
            W = botao(image=pygame.image.load("MenuAssets/Teclas.png"), pos=(518, 210),
                      text_input="W", font=get_font(30), base_color="#d7fcd4",
                      hovering_color="White")
            A = botao(image=pygame.image.load("MenuAssets/Teclas.png"), pos=(468, 260),
                      text_input="A", font=get_font(30), base_color="#d7fcd4",
                      hovering_color="White")
            S = botao(image=pygame.image.load("MenuAssets/Teclas.png"), pos=(518, 260),
                      text_input="S", font=get_font(30), base_color="#d7fcd4",
                      hovering_color="White")
            D = botao(image=pygame.image.load("MenuAssets/Teclas.png"), pos=(568, 260),
                      text_input="D", font=get_font(30), base_color="#d7fcd4",
                      hovering_color="White")

            for button in [seguinte, W, A, S, D]:
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
            historia1 = get_font(20).render("Agora que você já sabe se mover, você", True, "#EEE8AA")
            historia_espaco1 = historia1.get_rect(center=(510, 160))
            tela.blit(historia1, historia_espaco1)
            historia2 = get_font(20).render("deve tentar coletar todos esses itens", True, "#EEE8AA")
            historia_espaco2 = historia2.get_rect(center=(510, 190))
            tela.blit(historia2, historia_espaco2)
            anterior = botao(image=pygame.image.load("MenuAssets/Botao Instrucoes.png"), pos=(290, 530),
                             text_input="ANTERIOR", font=get_font(30), base_color="#d7fcd4",
                             hovering_color="White")
            seguinte = botao(image=pygame.image.load("MenuAssets/Botao Instrucoes.png"), pos=(718, 530),
                          text_input="SEGUINTE", font=get_font(30), base_color="#d7fcd4",
                          hovering_color="White")

            for button in [anterior, seguinte]:
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
                    if seguinte.checkForInput(menu_instrucao3_pos):
                        status = "instrucoes4"
                if pygame.key.get_pressed():
                    BobGroup.bob_menu2.posicao_menu()

            SpriteGroups.personagensmenu2.draw(tela)
            SpriteGroups.personagensmenu2.update()
            pygame.display.flip()
            pygame.display.update()

        if status == "instrucoes4":
            altura = 640
            largura = 1024
            fundo = pygame.image.load("Fundos/Background.png")
            tela = pygame.display.set_mode((largura, altura))
            tela.blit(fundo, (0, 0))
            menu_instrucao4_pos = pygame.mouse.get_pos()

            titulo = get_font(45).render("INSTRUÇÕES", True, "#EEE8AA")
            titulo_espaco = titulo.get_rect(center=(518, 100))
            tela.blit(titulo, titulo_espaco)
            historia1 = get_font(20).render("Agora que você ja sabe andar e coletar,", True, "#EEE8AA")
            historia_espaco1 = historia1.get_rect(center=(510, 160))
            tela.blit(historia1, historia_espaco1)
            historia2 = get_font(20).render("Experimente chegar perto do plâncton!", True, "#EEE8AA")
            historia_espaco2 = historia2.get_rect(center=(510, 190))
            tela.blit(historia2, historia_espaco2)
            vidasmenu = f'       : {PontuacaoContagem.vidas_menu}'
            posicaovidasmenu = txt.render(vidasmenu, True, (250, 0, 90))

            anterior = botao(image=pygame.image.load("MenuAssets/Botao Instrucoes.png"), pos=(290, 530),
                             text_input="ANTERIOR", font=get_font(30), base_color="#d7fcd4",
                             hovering_color="White")
            jogar = botao(image=pygame.image.load("MenuAssets/Botao Instrucoes.png"), pos=(718, 530),
                          text_input="JOGAR", font=get_font(30), base_color="#d7fcd4",
                          hovering_color="White")

            for button in [anterior, jogar]:
                button.changeColor(menu_instrucao4_pos)
                button.update(tela)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if anterior.checkForInput(menu_instrucao4_pos):
                        status = "instrucoes3"
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if jogar.checkForInput(menu_instrucao4_pos):
                        status = "game"
                if pygame.key.get_pressed():
                    BobGroup.bob_menu3.posicao_menu()

            SpriteGroups.personagensmenu3.draw(tela)
            SpriteGroups.personagensmenu3.update()
            tela.blit(posicaovidasmenu, (3, 160))
            pygame.display.flip()
            pygame.display.update()

        if status == "win":
            tela = pygame.display.set_mode((largura, altura))
            OPTIONS_MOUSE_POS = pygame.mouse.get_pos()
            tela.blit(fundo, (0, 0))


            OPTIONS_TEXT = get_font(65).render("VOCÊ CONSEGUIU!", True, "#EEE8AA")
            OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(518, 260))
            tela.blit(OPTIONS_TEXT, OPTIONS_RECT)
            fundo_jogar_novamente = pygame.image.load('MenuAssets/Quit Rect.png')
            fundo_jogar_novamente = pygame.transform.scale(fundo_jogar_novamente, (650, 65))
            OPTIONS_BACK = botao(image=fundo_jogar_novamente, pos=(518, 360),
                                 text_input="JOGAR NOVAMENTE", font=get_font(40), base_color="#EEE8AA",
                                 hovering_color="#d7fcd4")
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

            texto_gameover = get_font(70).render("GAME OVER!", True, "#EEE8AA")
            OPTIONS_RECT = texto_gameover.get_rect(center=(518, 260))
            tela.blit(texto_gameover, OPTIONS_RECT)
            fundo_jogar_novamente = pygame.image.load('MenuAssets/Quit Rect.png')
            fundo_jogar_novamente = pygame.transform.scale(fundo_jogar_novamente, (650, 65))
            OPTIONS_BACK = botao(image=fundo_jogar_novamente, pos=(518, 360),
                                 text_input="JOGAR NOVAMENTE", font=get_font(40), base_color="#EEE8AA",
                                 hovering_color="#d7fcd4")

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