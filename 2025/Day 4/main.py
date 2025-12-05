def part_one(lines):    
    print("Part One Solution: " + str(sum(1 for r, row in enumerate(lines) for c, cell in enumerate(row) if cell == '@' and sum(0 <= nr < len(lines) and 0 <= nc < len(row) 
                                        and lines[nr][nc] == '@' for nr in range(r - 1, r + 2) for nc in range(c - 1, c + 2) if (nr, nc) != (r, c)) < 4)))

def part_two(lines):
    rows = len(lines)
    cols = len(lines[0])
    total_removed = 0

    while True:
        accessible = [(row, col) for row in range(rows) for col in range(cols) if lines[row][col] == '@' and sum(0 <= nr < rows and 0 <= nc < cols and lines[nr][nc] == '@'
                                        for nr in range(row - 1, row + 2) for nc in range(col - 1, col + 2) if (nr, nc) != (row, col)) < 4]
        
        if not accessible: 
            break

        [lines.__setitem__(row, lines[row][:col] + ['.'] + lines[row][col + 1:]) for row, col in accessible]
        total_removed += len(accessible)

    print("Part Two Solution: " + str(total_removed))

if __name__ == '__main__':
    lines = open('input.txt').read().strip().split('\n')

    part_one(lines)
    part_two([list(line) for line in lines])
