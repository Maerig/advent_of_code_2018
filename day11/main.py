SERIAL = 5235
SIZE = 300


def power_level(x, y, serial):
    rack_id = x + 10
    power = rack_id * y
    power += serial
    power *= rack_id
    power = (power % 1000) // 100
    return power - 5


def get_powers(serial):
    return {
        (i, j): power_level(i, j, serial)
        for i in range(1, SIZE + 1)
        for j in range(1, SIZE + 1)
    }


def square_power(powers, x, y, size):
    return sum(
        powers[i, j]
        for i in range(x, x + size)
        for j in range(y, y + size)
    )


def get_max_square(powers, size):
    return max({
        (x, y): square_power(powers, x, y, size=size)
        for x in range(1, SIZE - size)
        for y in range(1, SIZE - size)
    }.items(), key=lambda x: x[1])


def part_1(serial):
    powers = get_powers(serial)
    coordinates, _ = get_max_square(powers, size=3)
    x, y = coordinates

    return f"{x},{y}"


def part_2(serial):
    powers = get_powers(serial)

    last_power = 0
    last_coordinates = None
    for size in range(1, SIZE + 1):
        coordinates, power = get_max_square(powers, size=size)
        print(f"size={size} power={power}")
        if power < last_power:
            x, y = last_coordinates
            return f"{x},{y},{size - 1}"
        last_power = power
        last_coordinates = coordinates


if __name__ == '__main__':
    print(f"Part 1: {part_1(SERIAL)}")
    print(f"Part 2: {part_2(SERIAL)}")
