import pygame as pg
import sys
import math

class DrawController:
    def __init__(self) -> None:
        self.screen = pg.display.set_mode((300, 300))
    
    def draw(self, history: list):
        for i in pg.event.get():
            if i.type == pg.QUIT:
                sys.exit()
        self.screen.fill("black")
        zoom = 300

        center = (history[-1]["x"]*zoom-150, history[-1]['y']*zoom-150)

        for i in range(len(history)-1):
            state = history[i]
            next_state = history[i+1]
            coor = (state['x']*zoom-center[0], state['y']*zoom-center[1])
            next_coor = (next_state['x']*zoom-center[0], next_state['y']*zoom-center[1])
            pg.draw.aaline(self.screen, "yellow", coor, next_coor)
        
        for state in history:
            coor = (state['x']*zoom-center[0], state['y']*zoom-center[1])
            obstacle_coor = (
                coor[0]+zoom*state['sensorValue']*math.cos(state['orientation']),
                coor[1]+zoom*state['sensorValue']*math.sin(state['orientation'])
            )
            pg.draw.aaline(self.screen, "white", coor, obstacle_coor)
            pg.draw.circle(self.screen, 'red', obstacle_coor, 3)
            
        lastState = history[-1]
        coor = (state['x']*zoom-center[0], state['y']*zoom-center[1])
        pg.draw.circle(self.screen, "blue", coor, 5)
        pg.display.update()
        pg.time.delay(100)