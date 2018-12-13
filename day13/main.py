from utils.vector import Vector

from day13.cart import Cart
from day13.directions import Direction
from day13.tracks import Straight, Track


def read_input():
    tracks = {}
    carts = []

    for (j, l) in enumerate(open('input.txt').readlines()):
        for (i, c) in enumerate(l):
            if c in ('^', '>', 'v', '<'):
                # Cart
                position = Vector(i, j)
                direction = Direction.parse(c)
                carts.append(Cart(position, direction))
                tracks[position] = Straight
            elif c != " " and c != "\n":
                # Track
                tracks[Vector(i, j)] = Track.parse(c)

    return tracks, carts


def is_colliding_position(position, carts):
    return sum(cart.position == position for cart in carts) > 1


def part_1(tracks, carts):
    while True:
        carts = sorted(carts, key=lambda c: c.position[::-1])
        for cart in carts:
            cart.move(tracks)
            new_position = cart.position
            if is_colliding_position(new_position, carts):
                return new_position


def part_2(tracks, carts):
    while True:
        carts = sorted(carts, key=lambda c: c.position[::-1])
        removed_carts = []
        for cart in carts:
            if cart in removed_carts:
                continue

            cart.move(tracks)
            new_position = cart.position
            if is_colliding_position(new_position, carts):
                removed_carts += [
                    cart
                    for cart in carts
                    if cart.position == new_position
                ]
        carts = [
            cart
            for cart in carts
            if cart not in removed_carts
        ]
        if len(carts) == 1:
            return carts[0].position


if __name__ == '__main__':
    print(f"Part 1: {part_1(*read_input())}")
    print(f"Part 2: {part_2(*read_input())}")
