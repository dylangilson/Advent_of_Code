def part_one(grid):
    wrap = lambda z: complex(z.real % 131, z.imag % 131)
    positions = {pos for pos in grid if grid[pos] == 'S'}

    for _ in range(64):
        positions = {p + d for p in positions for d in (1, -1, 1j, -1j) if wrap(p + d) in grid}

    print("Part One Solution: " + str(len(positions)))

def part_two(grid):
    wrap = lambda z: complex(z.real % 131, z.imag % 131)
    positions = {pos for pos in grid if grid[pos] == 'S'}
    counts = []

    for step in range(3 * 131):
        if step % 131 == 65:
            counts.append(len(positions))

        positions = {p + d for p in positions for d in (1, -1, 1j, -1j) if wrap(p + d) in grid}

    a, b, c = counts
    n = 26501365 // 131
    
    print("Part Two Solution: " + str(a + n * (b - a + (n - 1) * (c - 2 * b + a) // 2)))  # quadratic interpolation: f(n) = a + n * (b - a + (n - 1) * (c - 2b + a) // 2)


if __name__ == '__main__':
    grid = {complex(r, c): ch for r, line in enumerate(open('input.txt')) for c, ch in enumerate(line) if ch in '.S'}

    part_one(grid)
    part_two(grid)
