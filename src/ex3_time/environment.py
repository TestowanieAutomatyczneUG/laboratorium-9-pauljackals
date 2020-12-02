class Environment:
    def __init__(self):
        self.played = False

    def get_time(self):
        pass

    def play_wav_file(self, file):
        self.played = True

    def was_wav_played(self):
        return self.played

    def reset_wav(self):
        self.played = False
