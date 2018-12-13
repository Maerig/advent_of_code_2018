from dataclasses import dataclass
from typing import Dict


from day13.directions import Direction
from day13.tracks import Track, Intersection
from utils.vector import Vector


@dataclass
class Cart:
    position: Vector
    direction: Direction
    turn_index: int = 0

    intersection_turns = {
        0: lambda d: d.left(),  # Turn left
        1: lambda d: d,         # Go straight
        2: lambda d: d.right()  # Turn right
    }

    def move(self, tracks: Dict[Vector, Track]):
        current_track = tracks[self.position]
        self.position, self.direction = current_track.move(self.position, self.direction)
        new_track = tracks[self.position]
        if new_track == Intersection:
            self.make_intersection_turn()

    def make_intersection_turn(self):
        direction_change = self.intersection_turns[self.turn_index]
        self.direction = direction_change(self.direction)
        self.turn_index = (self.turn_index + 1) % len(self.intersection_turns)
