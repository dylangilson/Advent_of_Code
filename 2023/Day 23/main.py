P = complex
directions = (-1j, -1, 1, 1j)  # up, left, right, down
slopes = dict(zip("^<>v", directions))  # map slopes to directions

class Node:
    def __init__(self, pos, direction=None):
        self.pos = pos
        self.edges = {}
        self.direction = direction

class Graph:
    def __init__(self, grid, start, end, is_part1):
        self.nodes = {
            p: Node(p, slopes.get(v) if is_part1 else None) for p, v in grid.items() if v in '.^>v<'
        }

        self.start, self.end = self.nodes[start], self.nodes[end]
        
        # constructing edges, treating slopes as normal paths in part 2
        for p, node in self.nodes.items():
            for d in directions:
                if p + d in self.nodes:
                    adjacent = self.nodes[p + d]

                    if is_part1:
                        if node.direction in (None, d):
                            node.edges[adjacent] = 1
                    else:
                        node.edges[adjacent] = 1

        self.compress()
        
    def solve(self):
        stack = [(self.start, 0, set())]  # (node, distance, visited_nodes)
        max_dist = 0
        
        while stack:
            node, dist, visited = stack.pop()

            if node == self.end:
                max_dist = max(max_dist, dist)
            
            for neighbor in node.edges:
                if neighbor not in visited:
                    stack.append((neighbor, dist + node.edges[neighbor], visited | {neighbor}))
                    
        return max_dist

    def compress(self):
        # compress nodes that have no direction and exactly two neighbors
        for node in list(self.nodes.values()):
            if node.direction is None and len(node.edges) == 2:
                n1, n2 = list(node.edges.keys())
                
                if node in n1.edges and node in n2.edges:  # only compress if both nodes are connected
                    del n1.edges[node]
                    del n2.edges[node]

                    n1.edges[n2] = n2.edges[n1] = sum(node.edges.values())

def part_one(grid, start, end):
    print("Part One Solution: " + str(Graph(grid, start, end, is_part1=True).solve()))

def part_two(grid, start, end):
    print("Part Two Solution: " + str(Graph(grid, start, end, is_part1=False).solve()))

if __name__ == '__main__':
    lines = open('input.txt').read().splitlines()
    grid = {
        P(x, y): v for y, row in enumerate(lines) for x, v in enumerate(row)
    }
    start = next((P(x, 0) for x, v in enumerate(lines[0]) if v == '.'), None)
    end = next((P(x, len(lines)-1) for x, v in enumerate(lines[-1]) if v == '.'), None)

    part_one(grid, start, end)
    part_two(grid, start, end)
