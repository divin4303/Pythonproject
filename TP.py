import time


class TP:
    def __init__(self, PT):
        self.PT = PT
        self.start_time = None
        self.Q = False
        self.prev_IN = False

    def update(self, IN):
        if IN and not self.prev_IN:  # rising edge
            self.start_time = time.time()
            self.Q = True

        if self.Q and time.time() - self.start_time >= self.PT:
            self.Q = False

        self.prev_IN = IN
        return self.Q