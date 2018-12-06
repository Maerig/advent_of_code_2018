from collections import Counter
from utils.vector import Vector


def read_input():
    return tuple(
        Vector(*(
            int(i)
            for i in l.strip().split(",")
        ))
        for l in open('input.txt').readlines()
    )


def fit_grid(points):
    min_x, min_y = min(points)
    max_x, max_y = max(points)

    return tuple(
        Vector(x, y)
        for x in range(min_x, max_x)
        for y in range(min_y, max_y)
    )


def closest(point, points):
    distances = tuple(Vector.manhattan_distance(other - point) for other in points)
    min_dist = min(distances)
    minima = tuple(
        i
        for i, dist in enumerate(distances)
        if dist == min_dist
    )
    if len(minima) == 1:
        return minima[0]
    return None


def part_1(points):
    grid = fit_grid(points)
    closest_grid = tuple(
        closest(point, points)
        for point in grid
    )
    area_sizes = Counter(
        area
        for area in closest_grid
    )

    return max(area_sizes.values())


def total_distance(point, points):
    return sum(
        Vector.manhattan_distance(other - point)
        for other in points
    )


def part_2(points):
    grid_size = max(max(points))

    return sum(
        1
        for i in range(grid_size)
        for j in range(grid_size)
        if total_distance(Vector(i, j), points) < 10000
    )


if __name__ == '__main__':
    day6_input = read_input()

    print(f"Part 1: {part_1(day6_input)}")
    print(f"Part 2: {part_2(day6_input)}")
