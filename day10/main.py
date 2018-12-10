from collections import defaultdict

from day10.point import Point


START = 10630
END = 10650
STEP = 1


def read_input():
    return tuple(
        Point.parse(l.strip())
        for l in open('input.txt').readlines()
    )


def show_points(points):
    min_x = 2 ** 16
    max_x = -2 ** 16
    min_y = 2 ** 16
    max_y = -2 ** 16

    d = defaultdict(lambda: defaultdict(int))
    for p in points:
        x, y = p.position
        if x < min_x:
            min_x = x
        if x > max_x:
            max_x = x
        if y < min_y:
            min_y = y
        if y > max_y:
            max_y = y
        d[y][x] = '#'

    width = max_x - min_x
    height = max_y - min_y
    if width > 100 or height > 100:
        print(f"Size: {width}x{height}")
        return

    for j in range(min_y, max_y + 1):
        for i in range(min_x, max_x + 1):
            print(d[j].get(i, '.'), end=' ')
        print()


def run(points, start, end, step):
    for point in points:
        point.move(start)

    for i in range(start, end, step):
        print("i = %d" % i)
        for point in points:
            point.move(step)
        show_points(points)


if __name__ == '__main__':
    day10_input = read_input()
    run(tuple(day10_input), START, END, STEP)
