from rangeSensorController import RangeSensorController
from wheelsController import WheelsController
import time
import numpy as np
import math

class Robot:
    def __init__(
            self,
            sensor: RangeSensorController,
            wheels: WheelsController,
            coors: tuple = [0, 0],
            orientationRadian = 0
        ) -> None:
        self.sensor: RangeSensorController = sensor
        self.wheels: WheelsController = wheels
        self.coors: np.array = coors
        self.orientation: float = orientationRadian
        self.actualTime = time.time()
    
    def refresh(self) -> tuple:
        """
        обновляет положение робота
        """
        speed, radius = self.wheels.getRelativeMotionLaw()
        nowtime = time.time()

        deltaTime = nowtime - self.actualTime
        # omega = volume/radius

        # # Вычисляем угол поворота
        # angle = omega*deltaTime

        # rightNormal = np.dot(np.array([[0,  1],
        #                         [-1, 0]]), self.orientation)
        # center = rightNormal*radius + self.coors

        # coors_by_center = self.coors - center
        # phi = np.acos(coors_by_center[0]) # начальная фаза

        # new_coors_by_center = np.array((radius*np.cos(angle+phi), radius*np.sin(angle+phi))).transpose()

        # self.coors = new_coors_by_center+center
        # self.orientation = np.dot(np.array([[np.cos(angle), -np.sin(angle)],
        #                             [np.sin(angle), np.cos(angle)]]), self.orientation)
        # self.actualTime += deltaTime
        angle = (speed * deltaTime) / radius

        # Новая ориентация
        new_orientation = self.orientation + angle

        # Расстояние, пройденное по окружности
        distance = speed * deltaTime

        # Новые координаты
        new_x = self.coors[0] + radius * math.sin(new_orientation) - radius * math.sin(self.orientation)
        new_y = self.coors[1] + radius * (1 - math.cos(new_orientation)) - radius * (1 - math.cos(self.orientation))
        self.coors = [new_x, new_y]
        self.orientation = new_orientation
        self.actualTime = nowtime
        return (new_x, new_y), 1

    def log(self) -> None:
        pass

