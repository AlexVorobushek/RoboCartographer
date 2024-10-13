import pygame as pg
import sys
import math

class DrawController:
    def __init__(self) -> None:
        self.screenSize = (600, 600)
        self.screen = pg.display.set_mode(self.screenSize)
        self.zoom = 50
    
    def draw(self, history: list):
        # Выход из приложения
        for i in pg.event.get():
            if i.type == pg.QUIT:
                sys.exit()
        self.screen.fill("black")

        # В каком месте карты находится центр (относительно точки старта робота)
        center = (history[-1]["x"]*self.zoom-self.screenSize[0]/2, history[-1]['y']*self.zoom-self.screenSize[1]/2)

        # Линии траектории
        for i in range(len(history)-1):
            state = history[i]
            next_state = history[i+1]
            coor = (state['x']*self.zoom-center[0], state['y']*self.zoom-center[1])
            next_coor = (next_state['x']*self.zoom-center[0], next_state['y']*self.zoom-center[1])
            pg.draw.aaline(self.screen, "yellow", coor, next_coor)
        
        # Показания датчика
        for state in history:
            coor = (state['x']*self.zoom-center[0], state['y']*self.zoom-center[1])
            obstacle_coor = (
                coor[0]+self.zoom*state['sensorValue']*math.cos(state['orientation']),
                coor[1]+self.zoom*state['sensorValue']*math.sin(state['orientation'])
            )
            pg.draw.aaline(self.screen, "gray", coor, obstacle_coor)
            pg.draw.circle(self.screen, 'red', obstacle_coor, 3)
        
        # Последнее состояние робота
        lastState = history[-1]
        angleDeg = math.degrees(lastState['orientation'])+90
        angleImage = pg.transform.rotate(pg.transform.scale(pg.image.load('images/angleIcon.png'), (50, 50)), -angleDeg)

        coor = (state['x']*self.zoom-center[0], state['y']*self.zoom-center[1])
        rect = angleImage.get_rect(center=coor)
        self.screen.blit(angleImage, rect.topleft)
        # pg.draw.circle(self.screen, "blue", coor, 5)


        pg.display.update()
        pg.time.delay(100)