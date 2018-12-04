from collections import Counter


class Guard:
    def __init__(self):
        self.is_sleeping = False
        self.time_slept = Counter()
        self.last_time = None

    def begin(self, dt):
        self.is_sleeping = False
        self.last_time = dt

    def sleep(self, dt):
        if self.is_sleeping:
            return
        self.is_sleeping = True
        self.last_time = dt

    def wake_up(self, dt):
        if not self.is_sleeping:
            return
        self.is_sleeping = False

        for minute in range(self.last_time.minute, dt.minute):
            self.time_slept[minute] += 1

        self.last_time = dt
