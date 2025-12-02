def part_one(ranges):
    print("Part One Solution: " + str(sum(value for start, end in [map(int, range.split('-')) for range in ranges.split(',')] for value in range(start, end + 1) 
                                        if (lambda val:len(val) % 2 < 1 and val[:len(val) // 2] * 2 == val)(str(value)))))

def part_two(ranges):
    print("Part Two Solution: " + str(sum(value for start, end in [map(int, range.split('-')) for range in ranges.split(',')] for value in range(start, end + 1)
                                        if (lambda val: any(val == val[:i] * (len(val) // i) for i in range(1, len(val) // 2 + 1) if len(val) % i < 1))(str(value)))))

if __name__ == '__main__':
    ranges = open('input.txt').read().strip()

    part_one(ranges)
    part_two(ranges)
