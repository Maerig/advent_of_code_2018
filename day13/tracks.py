from abc import ABC, abstractmethod

from day13.directions import Direction
from utils.vector import Vector


class Track(ABC):
    @staticmethod
    def parse(c):
        return {
            '|': Straight,
            '-': Straight,
            '\\': BackslashTurn,
            '/': SlashTurn,
            '+': Intersection
        }[c]

    @staticmethod
    @abstractmethod
    def move(position: Vector, direction: Direction) -> (Vector, Direction):
        pass


class Straight(Track):
    @staticmethod
    def move(position: Vector, direction: Direction) -> (Vector, Direction):
        return position + direction.offset(), direction


class BackslashTurn(Track):
    @staticmethod
    def move(position: Vector, direction: Direction) -> (Vector, Direction):
        new_direction = direction.right() if direction.is_horizontal() else direction.left()
        return position + new_direction.offset(), new_direction


class SlashTurn(Track):
    @staticmethod
    def move(position: Vector, direction: Direction) -> (Vector, Direction):
        new_direction = direction.left() if direction.is_horizontal() else direction.right()
        return position + new_direction.offset(), new_direction


class Intersection(Track):
    @staticmethod
    def move(position: Vector, direction: Direction) -> (Vector, Direction):
        return position + direction.offset(), direction
