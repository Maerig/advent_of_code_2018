class Step:
    BASE_TIME = 60

    def __init__(self, letter):
        self.letter = letter
        self.prev_steps = []
        self.next_steps = []

        extra_time = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".index(letter) + 1
        self.remaining_time = Step.BASE_TIME + extra_time
        self.doing = False
