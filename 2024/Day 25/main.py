def part_one(lines):
    print("Part One Solution: " + str(sum(not k & line for k in lines for line in lines) // 2))

if __name__ == '__main__':
    lines = [{i for i, c in enumerate(item) if c == '#'} for item in open('input.txt').read().split('\n\n')]

    part_one(lines)
