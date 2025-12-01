from itertools import combinations
from collections import defaultdict, deque

def part_one(connections):    
    network = {}

    for a, b in connections:
        network.setdefault(a, set()).add(b)
        network.setdefault(b, set()).add(a)
    
    print("Part One Solution: " + str(sum(1 for a, b, c in combinations(network, 3) 
                                          if b in network[a] and c in network[a] and c in network[b] and any(computer.startswith('t') for computer in (a, b, c)))))

def part_two(connections):
    visited, pairs = set(), set()

    for a, b in connections:
        visited.update([a, b])
        pairs.update([(a, b), (b, a)])

    networks = [{c} for c in visited]

    for network in networks:
        [network.add(c) for c in visited if all((c, d) in pairs for d in network)]
            
    print("Part Two Solution:", ",".join(sorted(max(networks, key=len))))

if __name__ == "__main__":
    connections = [line.strip().split('-') for line in open('input.txt').readlines()]

    part_one(connections)
    part_two(connections)
