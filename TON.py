import time

class TON:
    def __init__(self, PT):
        self.PT = PT          # preset time in seconds
        self.start_time = None
        self.Q = False

    def update(self, IN):
        if IN:
            if self.start_time is None:
                self.start_time = time.time()
            if time.time() - self.start_time >= self.PT:
                self.Q = True
        else:
            self.start_time = None
            self.Q = False

        return self.Q
