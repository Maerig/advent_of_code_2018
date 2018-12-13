from abc import ABC, abstractmethod

from utils.vector import Vector


class Direction(ABC):
    @staticmethod
    def parse(c):
        return {
            '^': Up,
            '>': Right,
            'v': Down,
            '<': Left,
        }[c]

    @staticmethod
    @abstractmethod
    def offset():
        pass

    @staticmethod
    @abstractmethod
    def is_horizontal():
        pass

    @classmethod
    def right(cls):
        return cls._rotate(cls, _clockwise_rotation, +1)

    @classmethod
    def left(cls):
        return cls._rotate(cls, _clockwise_rotation, -1)

    @staticmethod
    def _rotate(elt, l, delta):
        return l[(l.index(elt) + delta) % len(l)]


class Up(Direction):
    @staticmethod
    def offset():
        return Vector(0, -1)

    @staticmethod
    @abstractmethod
    def is_horizontal():
        return False


class Right(Direction):
    @staticmethod
    def offset():
        return Vector(1, 0)

    @staticmethod
    @abstractmethod
    def is_horizontal():
        return True


class Down(Direction):
    @staticmethod
    def offset():
        return Vector(0, 1)

    @staticmethod
    @abstractmethod
    def is_horizontal():
        return False


class Left(Direction):
    @staticmethod
    def offset():
        return Vector(-1, 0)

    @staticmethod
    @abstractmethod
    def is_horizontal():
        return True


_clockwise_rotation = (Up, Right, Down, Left)
