from time import sleep
from matplotlib import pyplot as plt


def setup():
    from robot import Robot
    from rangeSensorController import RangeSensorController
    from wheelsController import WheelsController
    global drawing
    drawing = True
    if drawing:
        from drawController import DrawController
        global history, painter
        painter = DrawController()
        history = []

    sensor = RangeSensorController()
    wheels = WheelsController()
    global robot
    robot = Robot(sensor, wheels)

    with open("log.txt", "w"): pass
    

def loop():
    robot.refresh()
    robotState = robot.log()

    if drawing:
        history.append(robotState)
        painter.draw(history)

if __name__ == "__main__":
    setup()
    while True:
        loop()
        sleep(0.001)
