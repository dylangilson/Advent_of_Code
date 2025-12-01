from collections import defaultdict

def sum_iterations(n):
    for _ in range(2000):
        n = (n ^ (n << 6)) % 16777216
        n = (n ^ (n >> 5)) % 16777216
        n = (n ^ (n << 11)) % 16777216

    return n

def part_one(lst):
    print("Part One Solution: " + str(sum(map(sum_iterations, lst))))

def part_two(lst):
    total = defaultdict(int)

    for n in lst:
        seqs = {}
        seq = (0, 0, 0, 0)

        for i in range(2000):
            prev = n % 10
            n = (n ^ (n << 6)) % 16777216
            n = (n ^ (n >> 5)) % 16777216
            n = (n ^ (n << 11)) % 16777216
            seq = (*seq[1:], n % 10 - prev)

            if i >= 3 and seq not in seqs:
                seqs[seq] = n % 10
       
        for s in seqs:
            total[s] += seqs[s]

    max_profit, max_seq = max(((v, k) for k, v in total.items()), key=lambda x: x[0])

    print("Part Two Solution: " + str(max_profit) + " " + str(max_seq))

if __name__ == '__main__':
    lst = [int(line) for line in open('input.txt').readlines()]

    part_one(lst)
    part_two(lst)
