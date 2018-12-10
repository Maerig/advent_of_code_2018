import re

from utils.vector import Vector


class Point:
    vector_regex = "<\\s*(-?\\d+),\\s+(-?\\d+)>"
    regex = re.compile(f"position={vector_regex}\\s+velocity={vector_regex}")

    @classmethod
    def parse(cls, raw_string):
        match = Point.regex.match(raw_string)
        params = tuple(
            int(n)
            for n in match.groups()
        )
        position = Vector(*params[:2])
        velocity = Vector(*params[2:])
        return cls(position, velocity)

    def __init__(self, position, velocity):
        self.position = position
        self.velocity = velocity

    def move(self, n=1):
        self.position += self.velocity * n
