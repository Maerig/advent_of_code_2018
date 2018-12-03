import re


claim_regex = re.compile("#(\\d+) @ (\\d+),(\\d+): (\\d+)x(\\d+)")


class Claim:
    def __init__(self, raw_string):
        match = claim_regex.match(raw_string)
        self.id, self.x, self.y, self.width, self.height = (
            int(group)
            for group in match.groups()
        )

    def get_squares(self):
        return (
            (i, j)
            for i in range(self.x, self.x + self.width)
            for j in range(self.y, self.y + self.height)
        )
