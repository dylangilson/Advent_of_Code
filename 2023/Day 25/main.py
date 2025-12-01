from collections import defaultdict

def part_one(graph):
    nodes = set(graph)

    while sum(len(graph[v] - nodes) for v in nodes) != 3:
        nodes.remove(max(nodes, key=lambda v: len(graph[v] - nodes)))

    print("Part One Solution: " + str(len(nodes) * len(set(graph) - nodes)))

if __name__ == '__main__':
    graph = defaultdict(set)
    [graph[node].add(neighbour) or graph[neighbour].add(node) for line in open('input.txt') for node, *neighbours in [line.replace(':', '').split()] for neighbour in neighbours]

    part_one(graph)
