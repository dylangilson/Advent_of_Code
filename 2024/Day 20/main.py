from itertools import combinations

def part_one(grid):
    start = next(p for p in grid if grid[p] == 'S')
    dist, todo = {start: 0}, [start]
    
    for pos in todo:
        todo += [new for new in [pos - 1, pos + 1, pos - 1j, pos + 1j] if new in grid and new not in dist and not dist.update({new: dist[pos] + 1})]
    
    print("Part One Solution: " + str(sum(1 for (p, i), (q, j) 
                                          in combinations(dist.items(), 2) if abs((p - q).real) + abs((p - q).imag) == 2 and j - i - abs((p - q).real) - abs((p - q).imag) >= 100)))

def part_two(grid):
    start = next(p for p in grid if grid[p] == 'S')
    dist, todo = {start: 0}, [start]
    
    for pos in todo:
        todo += [new for new in [pos - 1, pos + 1, pos - 1j, pos + 1j] if new in grid and new not in dist and not dist.update({new: dist[pos] + 1})]
    
    print("Part Two Solution: " + str(sum(1 for (p, i), (q, j)
                                          in combinations(dist.items(), 2) if abs((p - q).real) + abs((p - q).imag) < 21 and j - i - abs((p - q).real) - abs((p - q).imag) >= 100)))

if __name__ == '__main__':
    grid = {i + j * 1j: c for i, r in enumerate(open('input.txt')) for j, c in enumerate(r) if c != '#'}
    
    part_one(grid)
    part_two(grid)
