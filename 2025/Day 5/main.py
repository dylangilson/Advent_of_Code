def part_one(lines):    
    print("Part One Solution: " + str(sum(any(start <= ingredient <= end for start, end in [tuple(map(int, range.split('-'))) for range in lines.split('\n\n')[0].split()]) 
                                        for ingredient in map(int, lines.split('\n\n')[1].split()))))

def part_two(lines):
    ranges = sorted(tuple(map(int, range.split('-'))) for range in lines.split('\n\n')[0].split())
    merged = []

    [merged.append([start, end]) if not merged or start > merged[-1][1] + 1 else merged.__setitem__(-1, [merged[-1][0], max(merged[-1][1], end)]) for start, end in ranges]

    print("Part Two Solution: " + str(sum(end - start + 1 for start, end in merged)))

if __name__ == '__main__':
    lines = open('input.txt').read().strip()

    part_one(lines)
    part_two(lines)
