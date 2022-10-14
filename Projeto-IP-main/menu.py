import pygame as pg
import numpy as np


def splash_screen(msg, splash, clock, font, screen):
    running = 1
    while running:
        clock.tick(60)
        surf = splash.copy()
        ticks = pg.time.get_ticks()/200
        surf.blit(font.render(msg, 1, (0, 0, 0)), (50, 500+5*np.sin(ticks-1)))
        surf.blit(font.render(msg, 1, (255, 255, 255)), (52, 500+5*np.sin(ticks)))

        p_mouse = pg.mouse.get_pos()
        pg.draw.polygon(surf, (200, 50, 50), (p_mouse, (p_mouse[0] + 20, p_mouse[1] + 22), (p_mouse[0], p_mouse[1] + 30)))

        screen.blit(surf, (0, 0))
        pg.display.update()

        for event in pg.event.get():
            if event.type == pg.KEYDOWN or event.type == pg.MOUSEBUTTONDOWN:
                return 0
            elif event.type == pg.QUIT:
                pg.quit()
