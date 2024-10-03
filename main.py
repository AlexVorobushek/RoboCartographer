from time import sleep
from matplotlib import pyplot as plt


def setup():
    from robot import Robot
    from rangeSensorController import RangeSensorController
    from wheelsController import WheelsController

    sensor = RangeSensorController()
    wheels = WheelsController()
    global robot
    robot = Robot(sensor, wheels)

    global ax, fig
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.set_xlim(-5, 5)
    ax.set_ylim(-5, 5)
    plt.show(block=False) # Показываем график, но не блокируем выполнение
    

def loop():
    a, b = robot.refresh()
    # print(list(a))
    ax.cla()
    ax.set_xlim(-5, 5)
    ax.set_ylim(-5, 5)
    ax.scatter(*list(a), c='blue', s=50)
    fig.canvas.draw_idle()
    fig.canvas.flush_events()

if __name__ == "__main__":
    setup()
    while True:
        loop()