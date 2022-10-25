import pygame
from sys import exit
from botoes import botao

import BobGroup
import SpriteGroups


def get_font(size):
    return pygame.font.Font("MenuAssets/font.ttf", size)


def instrucoes1():
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


def instrucoes2():
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
            BobGroup.bob.posicao()

    SpriteGroups.bob.draw(tela)
    SpriteGroups.bob.update()
    pygame.display.flip()
    pygame.display.update()

def instrucoes3():
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
