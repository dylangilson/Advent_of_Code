from collections import defaultdict

def part_one(grid):   
    start_row, start_col = next((index, row.index('S')) for index, row in enumerate(grid) if 'S' in row)
    beams, splits = {start_col}, 0

    for row in range(start_row + 1, len(grid)):
        splits += sum(grid[row][col] == '^' for col in beams if 0 <= col < len(grid[0])); 
        beams = {new_col for col in beams if 0 <= col < len(grid[0]) for new_col in ((col - 1, col + 1) if grid[row][col]=='^' else (col, ))}

    print("Part One Solution: " + str(splits))

def part_two(grid):
    row_index, col_index = next((i, row.index('S')) for i, row in enumerate(grid) if 'S' in row)
    col = {col_index:1}

    for i in range(row_index + 1, len(grid)):
        emission = [(x - (grid[i][x] == '^'), n) for x, n in col.items() if 0 <= x < len(grid[0])] + [(x + 1, n) for x, n in col.items() if 0 <= x < len(grid[0]) and grid[i][x] == '^']
        counts = defaultdict(int)

        [counts.__setitem__(x, counts[x] + n) for x, n in emission]

        col = counts

    print("Part Two Solution: " + str(sum(col.values())))

if __name__ == '__main__':
    grid = open('input.txt').read().strip().split('\n')

    part_one(grid)
    part_two(grid)
