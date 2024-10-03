import math

class WheelsController():
    def __init__(self) -> None:
        pass

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
        return 2*math.pi, 1