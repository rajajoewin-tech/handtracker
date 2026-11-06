import time


class FPSCounter:

    def __init__(self):

        self.previous_time = time.perf_counter()
        self.fps = 0

    def update(self):

        current_time = time.perf_counter()

        elapsed_time = current_time - self.previous_time

        if elapsed_time > 0:
            self.fps = 1 / elapsed_time

        self.previous_time = current_time

        return int(self.fps)