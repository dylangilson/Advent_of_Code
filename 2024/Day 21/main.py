from functools import lru_cache

n = ["789", "456", "123", " 0A"]
d = [" ^A", "<v>"]

def find_path(grid, start, end):
    sx, sy = next((x, y) for y, row in enumerate(grid) for x, c in enumerate(row) if c == start)
    ex, ey = next((x, y) for y, row in enumerate(grid) for x, c in enumerate(row) if c == end)

    def dfs(x, y, path):
        if (x, y) == (ex, ey): yield path + 'A'
        if ex < x and grid[y][x - 1] != ' ': yield from dfs(x - 1, y, path + '<')
        if ey < y and grid[y - 1][x] != ' ': yield from dfs(x, y - 1, path + '^')
        if ey > y and grid[y + 1][x] != ' ': yield from dfs(x, y + 1, path + 'v')
        if ex > x and grid[y][x + 1] != ' ': yield from dfs(x + 1, y, path + '>')

    return min(dfs(sx, sy, ""), key=lambda p: sum(a != b for a, b in zip(p, p[1:])))

@lru_cache(None)
def solve(path, level, min_level):
    if level > min_level: return len(path)
    
    return sum(solve(find_path(d if level else n, f, t), level + 1, min_level) for f, t in zip('A' + path, path))

def part_one(lst):
    print("Part One Solution: " + str(sum(solve(line.strip(), 0, 2) * int(line[:3]) for line in lst)))

def part_two(lst):
    print("Part Two Solution: " + str(sum(solve(line.strip(), 0, 25) * int(line[:3]) for line in lst)))

if __name__ == '__main__':
    lst = open('input.txt').read().splitlines()

    part_one(lst)
    part_two(lst)
