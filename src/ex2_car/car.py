from .engine import Engine


class Car:
    def __init__(self, engine=None):
        if engine:
            self.engine = Engine()
        else:
            self.engine = engine

    def needsFuel(self):
        pass

    def getEngineTemperature(self):
        return self.engine.getTemperature()

    def driveTo(self, destination):
        pass
