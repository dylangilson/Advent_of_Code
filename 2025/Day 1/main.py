def part_one(rotations):
    position = [50]

    print("Part One Solution: " + str(sum([(position.__setitem__(0, (position[0] + (int(rotation[1:]) if rotation[0] == 'R' else -int(rotation[1:]))) % 100) or True) 
                                        and position[0] == 0 for rotation in rotations])))

def part_two(rotations):
    position = [50]

    print("Part Two Solution: " + str(sum([(lambda step:(position.__setitem__(0, (position[0] + step) % 100), position[0] == 0)[1])((1 if rotation[0] == 'R' else -1)) 
                                        for rotation in rotations for _ in range(int(rotation[1:]))])))

if __name__ == '__main__':
    rotations = open('input.txt').read().strip().split('\n')

    part_one(rotations)
    part_two(rotations)
