from collections import defaultdict
import re

def drop(bricks, skip_index=None, is_part1=True):
    heights = defaultdict(int)
    total_falls = 0

    for i, (left, bottom, top_height, right, top, drop_height) in enumerate(bricks):
        if i == skip_index:
           continue

        area = [(x, y) for x in range(left, right + 1) for y in range(bottom, top + 1)]
        max_height = max(heights[coord] for coord in area) + 1

        for coord in area:
            heights[coord] = max_height + drop_height - top_height

        bricks[i] = (left, bottom, max_height, right, top, max_height + drop_height - top_height)
        total_falls += max_height < top_height

    return not total_falls if is_part1 else total_falls

def part_one(bricks):
    print("Part One Solution: " + str(sum([drop(bricks.copy(), skip_index=i, is_part1=True) for i in range(len(bricks))])))

def part_two(bricks):
    print("Part Two Solution: " + str(sum([drop(bricks.copy(), skip_index=i, is_part1=False) for i in range(len(bricks))])))

if __name__ == '__main__':
    bricks = sorted([[*map(int, re.findall(r'\d+', line))] for line in open('input.txt')], key=lambda block: block[2])

    drop(bricks)

    part_one(bricks)
    part_two(bricks)
