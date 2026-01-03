from itertools import combinations, pairwise
from collections import defaultdict

def rectangle_area(a, b):
    return (abs(a[0] - b[0]) + 1) * (abs(a[1] - b[1]) + 1)

def part_one(lines):
    print("Part One Solution:", max(rectangle_area(a, b) for a, b in combinations([tuple(map(int, line.split(','))) for line in lines if line.strip()], 2)))

def build_boundaries(red_tiles):
    vertical_segments = defaultdict(list)
    horizontal_segments = defaultdict(list)

    for (x1, y1), (x2, y2) in pairwise(red_tiles + [red_tiles[0]]):
        if x1 == x2:
            vertical_segments[x1].append((min(y1, y2), max(y1, y2)))
        else:
            horizontal_segments[y1].append((min(x1, x2), max(x1, x2)))

    horizontal_points = defaultdict(set)

    for y in horizontal_segments:
        horizontal_points[y] = { x for x1, x2 in horizontal_segments[y] for x in range(x1, x2 + 1) }

    vertical_points = defaultdict(set)

    for x in vertical_segments:
        vertical_points[x] = { y for y1, y2 in vertical_segments[x] for y in range(y1, y2 + 1) }

    return vertical_segments, horizontal_segments, horizontal_points, vertical_points

def part_two(lines):
    red_tiles = [tuple(map(int, line.split(','))) for line in lines if line.strip()]

    distances = sorted(((rectangle_area(a, b), (a, b)) for a, b in combinations(red_tiles, 2)), reverse=True)

    vertical_segments, horizontal_segments, hx, vy = build_boundaries(red_tiles)

    def point_on_boundary(x, y):
        return x in hx[y] or y in vy[x]

    def rectangle_clear(x1, y1, x2, y2):
        x_range = range(min(x1, x2) + 1, max(x1, x2))
        y_range = range(min(y1, y2) + 1, max(y1, y2))

        for y in horizontal_segments:
            if y in y_range:
                for xa, xb in horizontal_segments[y]:
                    if any(x in x_range for x in range(xa + 1, xb)):
                        return False

        for x in vertical_segments:
            if x in x_range:
                for ya, yb in vertical_segments[x]:
                    if any(y in y_range for y in range(ya + 1, yb)):
                        return False

        return True

    for area, ((x1, y1), (x2, y2)) in distances:
        if point_on_boundary(x1, y2) or point_on_boundary(x2, y1):
            if rectangle_clear(x1, y1, x2, y2):
                print("Part Two Solution:", area)
                return

if __name__ == "__main__":
    lines = open('input.txt').read().strip().split('\n')

    part_one(lines)
    part_two(lines)
