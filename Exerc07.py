import pygame as pg
from random import randrange

pg.init()
tela = pg.display.set_mode([800, 600])
posx= 0
posy= 0

def sair():
    pg.display.quit()
    pg.quit()
    exit()

cont = 0
while True:
    for evt in pg.event.get():
        if (evt.type == pg.MOUSEBUTTONDOWN):
            (posx, posy) = pg.mouse.get_pos()
            pg.draw.rect(tela, (255, 255, 0), (posx, posy, 50, 50))
            cont += 1
            if cont == 50:
                tela.fill((0, 0, 0))
                continue
        if evt.type == pg.KEYDOWN:
            if (evt.key == pg.K_SPACE ):
                posx = randrange(0, 800)
                posx = randrange(0, 600)
                pg.draw.rect(tela, (255, 255, 0), (posx, posy, 50, 50))
                cont += 1
                if cont == 50:
                    tela.fill((0, 0, 0))
                    continue


        if (evt.type == pg.QUIT):
            sair()



    pg.display.update()