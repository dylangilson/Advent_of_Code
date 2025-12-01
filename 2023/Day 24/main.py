import re

left, right = 200_000_000_000_000, 400_000_000_000_000

def intersect(one, two):
    b1x, b1y, _, v1x, v1y, _ = one
    b2x, b2y, _, v2x, v2y, _ = two
    
    # if the paths are parallel, no intersection
    if v1x * v2y - v2x * v1y == 0:
        return False
    
    # calculate intersection point (x, y)
    x = -(v1x * v2x * (b1y - b2y) + v1x * v2y * b2x - v2x * v1y * b1x) / (v2x * v1y - v1x * v2y)
    y = -(v1y * v2y * (b1x - b2x) + v1y * v2x * b2y - v2y * v1x * b1y) / (v2y * v1x - v1y * v2x)
    
    # check if the intersection is within bounds
    if not(left <= x <= right) or not(left <= y <= right):
        return False
    
    # ensure intersection occurs at valid times (not before t=0)
    return not ((v1x != 0 and (x - b1x) / v1x < 0) or (v2x != 0 and (x - b2x) / v2x < 0) or (v1y != 0 and (y - b1y) / v1y < 0) or (v2y != 0 and (y - b2y) / v2y < 0))

def part_one(hailstones):
    print("Part One Solution: " + str(sum(1 for i in range(len(hailstones) - 1) for j in range(i + 1, len(hailstones)) if intersect(hailstones[i], hailstones[j]))))

def gaussian_elimination(A, B):
    n = len(A)

    for i in range(n):
        factor = A[i][i]

        if factor == 0:
            continue

        A[i] = [x / factor for x in A[i]]
        B[i] /= factor

        for j in range(i + 1, n):
            factor = A[j][i]
            A[j] = [A[j][k] - A[i][k] * factor for k in range(n)]
            B[j] -= B[i] * factor

    x = [0] * n

    for i in range(n - 1, -1, -1):
        x[i] = B[i] - sum(A[i][j] * x[j] for j in range(i + 1, n))

    return x

def calculate_rows(x1, y1, dx1, dy1, x2, y2, dx2, dy2):
        return ([dy2 - dy1, dx1 - dx2, y2 - y1, x2 - x1], y1 * dx1 - y2 * dx2 + x2 * dy2 - x1 * dy1)

def part_two(hailstones):
    shift = min(x for y in hailstones[:8] for x in y[:3])

    # shift first 8 vectors
    for i in range(8):
        for j in range(3):
            hailstones[i][j] -= shift

    rows1, rows2, col1, col2 = [], [], [], []

    for i in range(0, 8, 2):
        row1, num1 = calculate_rows(*(hailstones[i][:2] + hailstones[i][3:5]), *(hailstones[i + 1][:2] + hailstones[i + 1][3:5]))
        row2, num2 = calculate_rows(*([hailstones[i][0], hailstones[i][2], hailstones[i][3], hailstones[i][5]]), 
                        *([hailstones[i + 1][0], hailstones[i + 1][2], hailstones[i + 1][3], hailstones[i + 1][5]]))
        
        rows1.append(row1)
        col1.append(num1)
        rows2.append(row2)
        col2.append(num2)

    ans1 = gaussian_elimination(rows1, col1)
    ans2 = gaussian_elimination(rows2, col2)

    print("Part Two Solution: " + str(round(ans1[0]) + round(ans1[1]) + round(ans2[1]) + 3 * shift))

if __name__ == '__main__':
    hailstones = [[int(y) for y in re.findall(r'-?[0-9]+', x)] for x in open('input.txt').read().split('\n')]

    part_one(hailstones)
    part_two(hailstones)
