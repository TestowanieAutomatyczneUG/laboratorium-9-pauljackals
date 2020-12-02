from .environment import Environment
import datetime


class Checker:
    def __init__(self, environment=None):
        self.environment = environment is None\
                           and Environment()\
                           or environment

    def remainder(self, file='default.wav'):
        time = self.environment.get_time()
        if (time - datetime.datetime.strptime('17:00', '%H:%M')).total_seconds() >= 0:
            self.environment.play_wav_file(file)
