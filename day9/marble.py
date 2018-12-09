class Marble:
    def __init__(self, number):
        self.number = number
        self.prev_marble = None
        self.next_marble = None

    def set_next(self, marble):
        self.next_marble = marble
        marble.prev_marble = self

    def get_next(self, n):
        current = self
        for _ in range(n):
            current = current.next_marble
        return current

    def get_prev(self, n):
        current = self
        for _ in range(n):
            current = current.prev_marble
        return current

    def add_next(self, marble):
        marble.set_next(self.next_marble)
        self.set_next(marble)

    def remove(self):
        self.prev_marble.set_next(self.next_marble)
        return self.number

    def __str__(self):
        return str(self.number)

    def __repr__(self):
        return self.__str__()
