import time

class TOF:
    def __init__(self, PT):
        self.PT = PT
        self.end_time = None
        self.Q = False

    def update(self, IN):
        if IN:
            self.Q = True
            self.end_time = None
        else:
            if self.end_time is None:
                self.end_time = time.time()
            if time.time() - self.end_time >= self.PT:
                self.Q = False

        return self.Q