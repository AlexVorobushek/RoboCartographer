from datetime import datetime

class Logger:
    def __init__(self):
        self.filename = f"./log/{datetime.now().strftime("%Y-%m-%d_%H-%M")}.txt"
        with open(self.filename, "w"): pass
    
    def log(self, robot):
        data = {
                'time': round(robot.actualTime, 2),
                'x': round(robot.coors[0], 2),
                'y': round(robot.coors[1], 2),
                'orientation': round(robot.orientation, 2),
                'sensorValue': round(robot.sensorValue, 2),
        }

        with open(self.filename, "a") as file:
            file.write('\t'.join(map(str, data.values()))+"\n")
        
        return data
