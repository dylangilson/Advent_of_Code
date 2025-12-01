from operator import xor as XOR, or_ as OR, and_ as AND

def part_one(lines):
    ops = {"XOR": XOR, "AND": AND, "OR": OR}
    signals = {}

    for line in lines:
        if '->' in line:
            parts = line.split()
            if len(parts) == 5:
                a, op, b, _, c = parts
                signals[c] = lambda a=a, b=b, op=op: ops[op](signals[a](), signals[b]())
        elif ':' in line:
            name, expr = map(str.strip, line.split(':', 1))
            value = int(expr)
            signals[name] = lambda v=value: v

    print("Part One Solution: " + str(sum(signals[f'z{i:02}']() << i for i in range(46))))

def part_two(lines):
    gates = [line.split() for line in lines if '->' in line and len(line.split()) == 5]
    r = lambda c, t: any(g == t and c in (a, b) for a, g, b, _, _ in gates)

    print("Part Two Solution: " + ",".join(sorted(
        c for a, op, b, _, c in gates if (
            (op == "XOR" and all(k[0] not in 'xyz' for k in (a, b, c))) or
            (op == "AND" and "x00" not in (a, b) and r(c, 'XOR')) or
            (op == "XOR" and "x00" not in (a, b) and r(c, 'OR')) or
            (op != "XOR" and c.startswith('z') and c != "z45")
        )
    )))

if __name__ == '__main__':
    lines = [line.strip() for line in open('input.txt') if line.strip()]

    part_one(lines)
    part_two(lines)
