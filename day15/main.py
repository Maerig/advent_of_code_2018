from utils.vector import Vector


class Unit:
    def __init__(self, pos, unit_type, elf_attack_power):
        self.pos = pos
        self.type = unit_type
        self.hp = 200
        self.attack = elf_attack_power if unit_type == "E" else 3

    def is_alive(self):
        return self.hp > 0


def read_input(elf_attack_power):
    grid = set()
    units = []
    for (j, l) in enumerate(open('input.txt').readlines()):
        for (i, c) in enumerate(l):
            if c in (".", "G", "E"):
                pos = Vector(j, i)
                grid.add(pos)
                if c != ".":
                    units.append(Unit(pos, c, elf_attack_power))

    return grid, units


def print_grid(grid, units):
    height = max(j for j, i in grid) + 1
    width = max(i for j, i in grid) + 1
    unit_grid = {
        unit.pos: unit.type
        for unit in units
    }
    for j in range(height):
        for i in range(width):
            v = Vector(j, i)
            if v in unit_grid:
                print(unit_grid[v], end="")
            elif v in grid:
                print(".", end="")
            else:
                print("#", end="")
        print()


def print_units(units):
    for u in units:
        print(u.type, u.hp)


def get_enemies(unit, units):
    return [
        u
        for u in units
        if u.type != unit.type
    ]


def get_outcome(round, units):
    return round * sum(
        unit.hp
        for unit in units
        if unit.is_alive()
    )


def get_adjacent(pos, grid):
    return tuple(
        pos + d
        for d in (
            Vector(-1, 0),
            Vector(0, -1),
            Vector(0, 1),
            Vector(1, 0)
        )
        if (pos + d) in grid
    )


def get_path(a, b, g):
    if a == b:
        return [a]
    visited = {a}
    paths = [[a]]

    while True:
        new_paths = []
        for path in paths:
            last = path[-1]
            for adj in get_adjacent(last, g):
                if adj not in visited:
                    new_path = path + [adj]
                    if adj == b:
                        return new_path
                    new_paths.append(path + [adj])
                    visited.add(adj)
        if not new_paths:
            return None
        paths = new_paths


def battle(grid, units, allow_dead_elves):
    round = 0
    while True:
        print(round)
        print_grid(grid, units)
        units.sort(key=lambda u: u.pos)
        for unit in units:
            if not unit.is_alive():
                continue
            enemies = tuple(
                e for e in get_enemies(unit, units)
                if e.is_alive()
            )
            if not enemies:
                return get_outcome(round, units)

            adj_pos = set(get_adjacent(unit.pos, grid))
            enemy_pos = {
                e.pos
                for e in enemies
                if e.is_alive()
            }
            if not enemy_pos.intersection(adj_pos):
                unit_pos = {
                    u.pos
                    for u in units
                    if u.is_alive()
                }
                candidates = {
                    p
                    for e in enemies
                    for p in get_adjacent(e.pos, grid)
                    if not p in unit_pos
                }
                movable = []
                for c in candidates:
                    movable_grid = grid - unit_pos
                    path = get_path(unit.pos, c, movable_grid)
                    if path:
                        movable.append((len(path), c, path))
                if movable:
                    fastest = min(movable)[2]
                    if len(fastest) > 1:
                        # Move
                        unit.pos = fastest[1]

            adj = get_adjacent(unit.pos, grid)
            attackable = [
                (e.hp, e)
                for e in enemies
                if e.pos in adj
            ]
            if attackable:
                target = min(attackable, key=lambda x: x[0])[1]
                target.hp -= unit.attack
                if target.type == "E" and target.hp <= 0 and not allow_dead_elves:
                    return -1
        units = [
            u for u in units
            if u.is_alive()
        ]
        round += 1


def part_1(grid, units):
    return battle(grid, units, allow_dead_elves=True)


def part_2(grid, units):
    return battle(grid, units, allow_dead_elves=False)


if __name__ == '__main__':
    print(f"Part 1: {part_1(*read_input(3))}")
    print(f"Part 2: {part_2(*read_input(34))}")
