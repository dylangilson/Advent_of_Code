def part_one(lines):
    position = [50]

    print("Part One Solution: " + str(sum([(position.__setitem__(0, (position[0] + (int(line[1:]) if line[0] == 'R' else -int(line[1:]))) % 100) or True) and position[0] == 0 for line in lines])))

def part_two(lines):
    position = [50]

    print(sum([(lambda step:(position.__setitem__(0, (position[0] + step) % 100), position[0] == 0)[1])((1 if line[0] == 'R' else -1)) for line in lines for _ in range(int(line[1:]))]))

if __name__ == '__main__':
    lines = open('input.txt').read().strip().split('\n')

    part_one(lines)
    part_two(lines)
