from itertools import combinations
from math import dist, prod

def part_one(lines):
    nodes = [tuple(map(int, line.split(','))) for line in lines if line.strip()]
    edges = sorted(combinations(nodes, 2), key=lambda x: dist(x[0], x[1]))

    parent = {u : u for u in nodes}
    size = {u : 1 for u in nodes}

    def find(u):
        path = []

        while parent[u] != u:
            path.append(u)
            u = parent[u]

        for p in path:
            parent[p] = u

        return u

    for u, v in edges[:1000]:
        pu, pv = find(u), find(v)

        if pu != pv:
            parent[pv] = pu
            size[pu] += size[pv]

    roots = {find(u) for u in nodes}
    s = sorted(size[r] for r in roots)

    print("Part One Solution: " + str(prod(s[-3:])))

def part_two(lines):
    nodes = [tuple(map(int, line.split(','))) for line in lines if line.strip()]
    edges = sorted(combinations(nodes, 2), key=lambda x: dist(x[0], x[1]))
    parent = {u : u for u in nodes}
    size = {u : 1 for u in nodes}
    components = len(nodes)

    def find(u):
        if parent[u] != u:
            parent[u] = find(parent[u])
        
        return parent[u]

    for u, v in edges:
        pu, pv = find(u), find(v)

        if pu != pv:
            parent[pv] = pu
            size[pu] += size[pv]
            components -= 1
            
            if components == 1:
                print("Part Two Solution: " + str(u[0] * v[0]))
                break

if __name__ == '__main__':
    lines = open('input.txt').read().strip().split('\n')

    part_one(lines)
    part_two(lines)
