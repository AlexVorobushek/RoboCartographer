import math

class WheelsController():
    def __init__(self) -> None:
        self.R=-10

    def getRelativeMotionLaw(self) -> tuple:
        """
        функция возвращает 
            (
            ±velocity,
            ±radius|null
            )

        +radius - робот поворачивает вправо при двежении вперед
        -radius - робот поворачивает влево при движении вперед
        """
        self.R += 0.01
        return 2*math.pi, self.R