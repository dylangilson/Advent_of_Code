from functools import reduce
from operator import add, mul
from itertools import groupby

def part_one(lines):   
    rows = [line.split() for line in lines]
    
    print("Part One Solution:", sum(sum(map(int, col)) if op == "+" else reduce(mul, map(int, col)) for col, op in zip(zip(*rows[:-1]), rows[-1])))

def part_two(lines):
    ops = {"+": add, "*": mul}
    grid = list(zip(*[line.ljust(max(len(l) for l in lines)) for line in lines]))
    operators = [col[-1] for col in grid if col[-1] in ops]
    nums = ["".join(col[:-1]).rstrip() for col in grid]
    groups = [[int(n) for n in g] for k, g in groupby(nums, bool) if k]
    
    print("Part Two Solution: " + str(sum(reduce(ops[op], grp) for op, grp in zip(operators[::-1], groups[::-1]))))

if __name__ == '__main__':
    lines = open('input.txt').read().strip().split('\n')

    part_one(lines)
    part_two(lines)
