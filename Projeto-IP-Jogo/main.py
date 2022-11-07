#realizando as importações necessárias
import pygame
from pygame.locals import *
from sys import exit
from botoes import botao
import BobGroup
import PontuacaoContagem
import SpriteGroups

#definindo funcao fonte
def get_font(size):
    return pygame.font.Font("MenuAssets/font.ttf", size)

#definindo funcao game, que controla o jogo
def game():
    fase = 0
    # iniciando o pygame
    pygame.init()
    # definindo a fonte para a contagem
    txt = pygame.font.SysFont('arial', 25, bold=True, italic=False)

#musica de fundo
    pygame.mixer.music.set_volume(1.0)
    pygame.mixer.music.load('sons\music_bob.mp3')
    pygame.mixer.music.play(-1)

#definicoes basicas (ex: tamanho): tela, icones: bob, vidas e coletaveis
    altura = 640
    largura = 1024
    background = pygame.image.load(('Fundos/fundomapa.jpg'))
    vidas = pygame.image.load('coletaveis/vidas.png')
    burguer = pygame.image.load('coletaveis/burguer1.png')
    burguer = pygame.transform.scale(burguer, (26, 26))
    vidas = pygame.transform.scale(vidas, (26, 26))
    fries = pygame.image.load('coletaveis/fries.png')
    fries = pygame.transform.scale(fries, (29, 32))
    soda = pygame.image.load('coletaveis/soda1.png')
    soda = pygame.transform.scale(soda, (22, 40))

    # adicionando um icon para a tela do jogo e o título do jogo
    icon = pygame.image.load('sprites/bob_1.png')
    pygame.display.set_icon(icon)
    pygame.display.set_caption('Get the B(ob)urger!')

    # inicializando o jogo
    relogio = pygame.time.Clock()
    status = "start"

    # looping principal do jogo:
    while True:
        #iniciando o jogo: definindo tamanhos, textos e icones de contagem dos coletaveis
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
                BobGroup.personagens.bob.posicao()
                BobGroup.personagens.plancton.posicao()
                if fase == 2:
                    BobGroup.personagens.plancton2.posicao()


            # se as vidas acabarem e o jogador perder o jogo:
            # definindo som a ser emitido
            # mudando o status para a tela do menu de derrota e reiniciando as sprites e a contagem
            if PontuacaoContagem.vidas == 0:
                morte = pygame.mixer.Sound('sons/morte.wav')
                pygame.mixer.Sound.set_volume(morte, 1)
                morte.play()
                PontuacaoContagem.burguer = PontuacaoContagem.refri = PontuacaoContagem.fries = 0
                PontuacaoContagem.vidas = 3
                SpriteGroups.todas_sprites = SpriteGroups.desenhar()
                status = "gameover"
                fase = 0
                SpriteGroups.todas_sprites.add(BobGroup.personagens.bob)
                SpriteGroups.todas_sprites.add(BobGroup.personagens.plancton)


            # se coletar todos os itens e vencer:
            # definindo som
            # mudando o status para a fase 2 e reiniciando as sprites e a contagem
            if (PontuacaoContagem.burguer == PontuacaoContagem.fries == PontuacaoContagem.refri == 5) and fase != 2:
                venceu = pygame.mixer.Sound('sons/venceu.wav')
                pygame.mixer.Sound.set_volume(venceu, 1)
                venceu.play()
                PontuacaoContagem.burguer = PontuacaoContagem.refri = PontuacaoContagem.fries = 0
                PontuacaoContagem.vidas = 3
                SpriteGroups.todas_sprites = SpriteGroups.desenhar()
                status = "fase_2"
                SpriteGroups.todas_sprites.add(BobGroup.personagens.bob)
                SpriteGroups.todas_sprites.add(BobGroup.personagens.plancton)

            # desenhando todos os itens e atualizando-os constantemente durante a fase1
            SpriteGroups.todas_sprites.draw(tela)
            SpriteGroups.todas_sprites.update()
            tela.blit(posicao, (3, 20))
            tela.blit(posicao2, (3, 70))
            tela.blit(posicao3, (3, 115))
            tela.blit(posicao4, (3, 160))
            pygame.display.flip()

            #se coletar todos os itens na fase 2
            #definindo som
            # mudando o status para a tela do menu de vitória e reiniciando as sprites e a contagem
            if (PontuacaoContagem.burguer == PontuacaoContagem.fries == PontuacaoContagem.refri == 5) and fase == 2:
                venceu = pygame.mixer.Sound('sons/venceu.wav')
                pygame.mixer.Sound.set_volume(venceu, 1)
                venceu.play()
                PontuacaoContagem.burguer = PontuacaoContagem.refri = PontuacaoContagem.fries = 0
                PontuacaoContagem.vidas = 3
                fase = 0
                SpriteGroups.todas_sprites = SpriteGroups.desenhar()
                status = "win"
                SpriteGroups.todas_sprites.add(BobGroup.personagens.bob)
                SpriteGroups.todas_sprites.add(BobGroup.personagens.plancton)

            # desenhando novamente os itens e atualizando-os constantemente durante a fase2
            SpriteGroups.todas_sprites.draw(tela)
            SpriteGroups.todas_sprites.update()
            tela.blit(posicao, (3, 20))
            tela.blit(posicao2, (3, 70))
            tela.blit(posicao3, (3, 115))
            tela.blit(posicao4, (3, 160))
            pygame.display.flip()

        #fase 2:
        if status == "fase_2":
            #definicoes tela para fase 2
            altura = 640
            largura = 1024
            fundo = pygame.image.load("Fundos/Background.png")
            tela = pygame.display.set_mode((largura, altura))
            tela.blit(fundo, (0, 0))
            menu_inicial_pos = pygame.mouse.get_pos()

            #menu intermediario: escrevendo título do jogo na tela, a história, e os botoões com a opção de voltar
            # ou de seguir para a fase 2

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

            # analisando se o mouse está em cima do botão e mudando de cor em caso afirmativo
            for button in [voltar, iniciar]:
                button.changeColor(menu_inicial_pos)
                button.update(tela)

            for event in pygame.event.get():
                # condição para sair do jogo, voltar ou seguir
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if voltar.checkForInput(menu_inicial_pos):
                        status = "start"
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if iniciar.checkForInput(menu_inicial_pos):
                        status = "game"
                        SpriteGroups.todas_sprites.add(BobGroup.personagens.plancton2)



            pygame.display.update()

        #menu inicial
        if status == "start":
            # definindo a tela de fundo e iniciando ela
            fundo = pygame.image.load("Fundos/Background.png")
            tela = pygame.display.set_mode((largura, altura))
            tela.blit(fundo, (0, 0))
            # reconhecendo a posição do mouse na tela
            menu_inical_pos = pygame.mouse.get_pos()

            # escrevendo título do jogo na tela, os botões com a opção de iniciar o jogo e de sair
            menu = get_font(48).render("GET THE B(OB)URGUER!", True, "#EEE8AA")
            menu_espaco = menu.get_rect(center=(518, 100))

            iniciar = botao(image=pygame.image.load("MenuAssets/Options Rect.png"), pos=(518, 350),
                                text_input="INICIAR", font=get_font(70), base_color="#d7fcd4",
                                hovering_color="White")
            sair = botao(image=pygame.image.load("MenuAssets/Quit Rect.png"), pos=(920, 590),
                                text_input="SAIR", font=get_font(35), base_color="#d7fcd4", hovering_color="White")

            tela.blit(menu, menu_espaco)

            # analisando se o mouse está em cima do botão e mudando de cor em caso afirmativo
            for button in [iniciar, sair]:
                button.changeColor(menu_inical_pos)
                button.update(tela)

            for event in pygame.event.get():
                # condições para sair do jogo ou seguir as instruções
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if iniciar.checkForInput(menu_inical_pos):
                        status = "instrucoes1"
                    if sair.checkForInput(menu_inical_pos):
                        pygame.quit()
                        exit()

            pygame.display.update()

        #menu instrucoes
        # definindo a tela de fundo e iniciando ela
        if status == "instrucoes1":
            altura = 640
            largura = 1024
            fundo = pygame.image.load("Fundos/Background.png")
            tela = pygame.display.set_mode((largura, altura))
            tela.blit(fundo, (0, 0))
            menu_instrucao1_pos = pygame.mouse.get_pos()

            # escrevendo título do jogo na tela, a história, botões com a opção de ler as instruções ou seguir direto para o jogo

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

            # analisando se o mouse está em cima do botão e mudando de cor em caso afirmativo
            for button in [instrucoes, iniciar]:
                button.changeColor(menu_instrucao1_pos)
                button.update(tela)

            for event in pygame.event.get():
                # condição para sair do jogo ou seguir para as próximas instruções
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if instrucoes.checkForInput(menu_instrucao1_pos):
                        status = "instrucoes2"
                        BobGroup.menus.bob_menu.x_bob = 200
                        BobGroup.menus.bob_menu.y_bob = 350
                        # redesenhando os personagens necessários
                        SpriteGroups.bob_menu = SpriteGroups.bob_desenho()
                        SpriteGroups.bob_menu.add(BobGroup.menus.personagens_menu())
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if iniciar.checkForInput(menu_instrucao1_pos):
                        status = "game"

            pygame.display.update()

        if status == "instrucoes2":
            # definindo a tela de fundo e iniciando ela
            altura = 640
            largura = 1024
            fundo = pygame.image.load("Fundos/Background.png")
            tela = pygame.display.set_mode((largura, altura))
            tela.blit(fundo, (0, 0))
            menu_instrucao2_pos = pygame.mouse.get_pos()

            # escrevendo as instruções na tela e o botão com a opção de seguir para as próximas instruções
            titulo = get_font(45).render("INSTRUÇÕES", True, "#EEE8AA")
            titulo_espaco = titulo.get_rect(center=(518, 100))
            tela.blit(titulo, titulo_espaco)
            historia1 = get_font(20).render("Para se movimentar aperte as teclas do teclado:", True, "#EEE8AA")
            historia_espaco1 = historia1.get_rect(center=(510, 160))
            tela.blit(historia1, historia_espaco1)
            seguinte = botao(image=pygame.image.load("MenuAssets/Botao Instrucoes.png"), pos=(518, 530),
                             text_input="SEGUINTE", font=get_font(30), base_color="#d7fcd4",
                             hovering_color="White")

            # desenhando os botões ilustrativos do teclado para movimentação
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

            # analisando se o mouse está em cima do botão e mudando de cor em caso afirmativo
            for button in [seguinte, W, A, S, D]:
                button.changeColor(menu_instrucao2_pos)
                button.update(tela)

            for event in pygame.event.get():
                # condição para sair do jogo ou seguir para as próximas instruções
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if seguinte.checkForInput(menu_instrucao2_pos):
                        status = "instrucoes3"
                        #reposicionando o bob do instrucoes2 caso o jogador volte para essa tela posteriormente
                        BobGroup.menus.bob_menu2.x_bob = 200
                        BobGroup.menus.bob_menu2.y_bob = 320
                        # redesenhando os personagens necessários
                        SpriteGroups.personagensmenu2 = SpriteGroups.bob_desenho2()
                        SpriteGroups.personagensmenu2.add(BobGroup.menus.personagens_menu2())
                        SpriteGroups.personagensmenu2.draw(tela)
                        SpriteGroups.personagensmenu2.update()
                # movimentando o bob caso as teclas de movimento sejam apertadas
                if pygame.key.get_pressed():
                    BobGroup.menus.bob_menu.posicao_menu()
            # desenhando os personagens necessários para as próximas instruções e atualizando-os constantemente
            BobGroup.menus.bob_menu.posicao_menu()
            SpriteGroups.bob_menu.draw(tela)
            SpriteGroups.bob_menu.update()
            pygame.display.flip()

        if status == "instrucoes3":
            # definindo a tela de fundo e iniciando ela
            altura = 640
            largura = 1024
            fundo = pygame.image.load("Fundos/Background.png")
            tela = pygame.display.set_mode((largura, altura))
            tela.blit(fundo, (0, 0))
            menu_instrucao3_pos = pygame.mouse.get_pos()

            # escrevendo as instruções na tela e os botões com a opção de seguir para as próximas instruções ou voltar para a anterior
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

            # analisando se o mouse está em cima do botão e mudando de cor em caso afirmativo
            for button in [anterior, seguinte]:
                button.changeColor(menu_instrucao3_pos)
                button.update(tela)

            for event in pygame.event.get():
                # condição para sair do jogo, voltar ou seguir para as próximas instruções
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if anterior.checkForInput(menu_instrucao3_pos):
                        status = "instrucoes2"
                        # reposicionando o bob do instrucoes2 caso o jogador volte para essa tela posteriormente
                        BobGroup.menus.bob_menu.x_bob = 200
                        BobGroup.menus.bob_menu.y_bob = 350
                        # redesenhando os personagens necessários
                        SpriteGroups.bob_menu = SpriteGroups.bob_desenho()
                        SpriteGroups.bob_menu.add(BobGroup.menus.personagens_menu())

                if event.type == pygame.MOUSEBUTTONDOWN:
                    # se o botão seguinte for clicado, posicionar bob e escrever a contagem de vidas das instruções
                    if seguinte.checkForInput(menu_instrucao3_pos):
                        status = "instrucoes4"
                        PontuacaoContagem.status_menu = "1 VIDA"
                        BobGroup.menus.bob_menu3.x_bob = 200
                        BobGroup.menus.bob_menu3.y_bob = 320
                        SpriteGroups.personagensmenu3 = SpriteGroups.bob_desenho3()
                        SpriteGroups.personagensmenu3.add(BobGroup.menus.personagens_menu3())

                # movimentando o bob caso as teclas de movimento sejam apertadas
                if pygame.key.get_pressed():
                    BobGroup.menus.bob_menu2.posicao_menu()

            # desenhando os personagens necessários para as próximas instruções e atualizando-os constantemente
            BobGroup.menus.bob_menu2.posicao_menu()
            SpriteGroups.personagensmenu2.draw(tela)
            SpriteGroups.personagensmenu2.update()
            pygame.display.flip()

        if status == "instrucoes4":
            # definindo a tela de fundo e iniciando ela
            altura = 640
            largura = 1024
            fundo = pygame.image.load("Fundos/Background.png")
            tela = pygame.display.set_mode((largura, altura))
            tela.blit(fundo, (0, 0))
            menu_instrucao4_pos = pygame.mouse.get_pos()

            # escrevendo as instruções na tela e criando os botões com a opção de seguir para começar o jogo ou voltar para a instrução anterior
            titulo = get_font(45).render("INSTRUÇÕES", True, "#EEE8AA")
            titulo_espaco = titulo.get_rect(center=(518, 100))
            tela.blit(titulo, titulo_espaco)
            historia1 = get_font(20).render("Agora que você ja sabe andar e coletar,", True, "#EEE8AA")
            historia_espaco1 = historia1.get_rect(center=(510, 160))
            tela.blit(historia1, historia_espaco1)
            historia2 = get_font(20).render("Experimente chegar perto do plâncton!", True, "#EEE8AA")
            historia_espaco2 = historia2.get_rect(center=(510, 190))
            tela.blit(historia2, historia_espaco2)
            # expondo a contagem de vidas
            if PontuacaoContagem.status_menu == "1 VIDA":
                vidasmenu = get_font(20).render(f"{PontuacaoContagem.status_menu}", True, "#006400")
                vidasmenu_espaco = vidasmenu.get_rect(center=(520, 250))
            else:
                vidasmenu = get_font(20).render(f"{PontuacaoContagem.status_menu}", True, "#FF0000")
                vidasmenu_espaco = vidasmenu.get_rect(center=(515, 250))
            tela.blit(vidasmenu, vidasmenu_espaco)
            anterior = botao(image=pygame.image.load("MenuAssets/Botao Instrucoes.png"), pos=(290, 530),
                             text_input="ANTERIOR", font=get_font(30), base_color="#d7fcd4",
                             hovering_color="White")
            jogar = botao(image=pygame.image.load("MenuAssets/Botao Instrucoes.png"), pos=(718, 530),
                          text_input="JOGAR", font=get_font(30), base_color="#d7fcd4",
                          hovering_color="White")

            # analisando se o mouse está em cima do botão e mudando de cor em caso afirmativo
            for button in [anterior, jogar]:
                button.changeColor(menu_instrucao4_pos)
                button.update(tela)

            for event in pygame.event.get():
                # condição para sair do jogo, voltar para as instruções anteriores ou seguir para o jogo
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if anterior.checkForInput(menu_instrucao4_pos):
                        status = "instrucoes3"
                        # reposicionando o bob do instrucoes3 caso o jogador volte para essa tela posteriormente
                        BobGroup.menus.bob_menu2.x_bob = 200
                        BobGroup.menus.bob_menu2.y_bob = 320
                        # redesenhando os personagens necessários
                        SpriteGroups.personagensmenu2 = SpriteGroups.bob_desenho2()
                        SpriteGroups.personagensmenu2.add(BobGroup.menus.personagens_menu2())
                        SpriteGroups.personagensmenu2.draw(tela)
                        SpriteGroups.personagensmenu2.update()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if jogar.checkForInput(menu_instrucao4_pos):
                        status = "game"
                        PontuacaoContagem.status_menu = "1 VIDA"
                        BobGroup.menus.bob_menu3.x_bob = 200
                        BobGroup.menus.bob_menu3.y_bob = 320

                # movimentando o bob caso as teclas de movimento sejam apertadas
                if pygame.key.get_pressed():
                    BobGroup.menus.bob_menu3.posicao_menu()

            # desenhando os personagens necessários e atualizando-os constantemente
            BobGroup.menus.bob_menu3.posicao_menu()
            SpriteGroups.personagensmenu3.draw(tela)
            SpriteGroups.personagensmenu3.update()
            pygame.display.flip()

        #menu vencedor
        if status == "win":
            # definindo a tela de fundo e iniciando ela
            tela = pygame.display.set_mode((largura, altura))
            win_pos = pygame.mouse.get_pos()
            tela.blit(fundo, (0, 0))

            # escrevendo a parabenização na tela e criando o botão com a opção de jogar novamente
            win = get_font(65).render("VOCÊ CONSEGUIU!", True, "#EEE8AA")
            win_espaco = win.get_rect(center=(518, 260))
            tela.blit(win, win_espaco)
            fundo_jogar_novamente = pygame.image.load('MenuAssets/Quit Rect.png')
            fundo_jogar_novamente = pygame.transform.scale(fundo_jogar_novamente, (650, 65))
            jogar_novamente = botao(image=fundo_jogar_novamente, pos=(518, 360),
                                 text_input="JOGAR NOVAMENTE", font=get_font(40), base_color="#EEE8AA",
                                 hovering_color="#d7fcd4")
            jogar_novamente.changeColor(win_pos)
            jogar_novamente.update(tela)

            # analisando se o mouse está em cima do botão e mudando de cor em caso afirmativo
            for button in [jogar_novamente]:
                button.changeColor(win_pos)
                button.update(tela)

            # condição para sair ou reiniciar o jogo
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if jogar_novamente.checkForInput(win_pos):
                        status = "start"
            pygame.display.update()

        #menu gameover
        if status == "gameover":
            # definindo a tela de fundo e iniciando ela
            tela = pygame.display.set_mode((largura, altura))
            gameover_pos = pygame.mouse.get_pos()
            tela.blit(fundo, (0, 0))

            # noticiando a perda na tela e criando o botão com a opção de jogar novamente
            gameover = get_font(70).render("GAME OVER!", True, "#EEE8AA")
            gameover_espaco = gameover.get_rect(center=(518, 260))
            tela.blit(gameover, gameover_espaco)
            fundo_jogar_novamente = pygame.image.load('MenuAssets/Quit Rect.png')
            fundo_jogar_novamente = pygame.transform.scale(fundo_jogar_novamente, (650, 65))
            jogar_novamente = botao(image=fundo_jogar_novamente, pos=(518, 360),
                                 text_input="JOGAR NOVAMENTE", font=get_font(40), base_color="#EEE8AA",
                                 hovering_color="#d7fcd4")

            # analisando se o mouse está em cima do botão e mudando de cor em caso afirmativo
            jogar_novamente.changeColor(gameover_pos)
            jogar_novamente.update(tela)

            for event in pygame.event.get():
                # condição para sair ou reiniciar o jogo
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if jogar_novamente.checkForInput(gameover_pos):
                        status = "start"
            pygame.display.update()

        pygame.display.update()

# analisando se o arquivo main está sendo rodado e inicializando o jogo
if __name__ == '__main__':
    game()