from rangeSensorController import RangeSensorController
from wheelsController import WheelsController
from logger import Logger
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
        self.sensorValue = sensor.getValue()
        self.velocity, self.radius = wheels.getRelativeMotionLaw()
        self.logger = Logger()

    def _getNewPositioning(self, newV, newR, newT):
        newV, newR = self.wheels.getRelativeMotionLaw()
        newT = time.time()

        deltaTime = newT - self.actualTime
        angle = (newV * deltaTime) / newR

        # Новая ориентация
        new_orientation = self.orientation + angle

        # Расстояние, пройденное по окружности
        distance = newV * deltaTime

        # Новые координаты
        new_x = self.coors[0] + newR * math.sin(new_orientation) - newR * math.sin(self.orientation)
        new_y = self.coors[1] + newR * (1 - math.cos(new_orientation)) - newR * (1 - math.cos(self.orientation))
        self.coors = [new_x, new_y]
        
        return (new_x, new_y), new_orientation

    
    def refresh(self) -> None:
        """
        обновляет все характеристики робота
        """
        newVelosity, newRadius = self.wheels.getRelativeMotionLaw()
        newTime = time.time()

        self.sensorValue = self.sensor.getValue()
        self.coors, self.orientation = self._getNewPositioning(newVelosity, newRadius, newTime)
        self.actualTime = newTime

    def log(self) -> None:
        return self.logger.log(self)
    