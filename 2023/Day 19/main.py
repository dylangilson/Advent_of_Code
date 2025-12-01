import re
import operator
from math import prod

ops = {'<': operator.lt, '>': operator.gt}

def eval_condition(cond, part):
    if cond == 'True':
        return True
    
    var, op, val = cond[0], cond[1], int(cond[2:])
    
    return ops[op](part[var], val)

def run(part, flows):
    flow = 'in'

    while flow not in {'A', 'R'}:
        flow = next(dest for cond, dest in flows[flow] if eval_condition(cond, part))

    return flow

def part_one(parts, flows):
  print("Part One Solution: " + str(sum(sum(part.values()) for part in parts if run(part, flows) == 'A')))

def part_two(flows):
    def dfs(flow_name, var_ranges):
        if flow_name == 'R':
            return 0
        if flow_name == 'A':
            return prod(hi - lo + 1 for lo, hi in var_ranges.values())
        
        total = 0

        for condition, next_flow in flows[flow_name]:
            if condition == 'True':
                return total + dfs(next_flow, var_ranges)
            
            var, op, val = condition[0], condition[1], int(condition[2:])
            lo, hi = var_ranges[var]

            if op == '<':
                if lo < val:
                    total += dfs(next_flow, {**var_ranges, var: (lo, min(val - 1, hi))})

                if hi >= val:
                    var_ranges[var] = (max(lo, val), hi)
            else:  # op == '>'
                if hi > val:
                    total += dfs(next_flow, {**var_ranges, var: (max(lo, val + 1), hi)})

                if lo <= val:
                    var_ranges[var] = (lo, min(hi, val))

        return total

    print("Part Two Solution: " + str(dfs('in', {var: (1, 4000) for var in 'xmas'})))

if __name__ == '__main__':
    flows_raw, parts_raw = open('input.txt').read().split('\n\n')
    parts = [dict((k, int(v)) for k, v in re.findall(r'(\w)=(\d+)', line)) for line in parts_raw.strip().splitlines()]
    flows = {
        name: [(cond if ':' in rule else 'True', dest if ':' in rule else rule) for rule in rules.split(',') for cond, dest in [rule.split(':') if ':' in rule else (rule, rule)]]
        for name, rules in (line.rstrip('}').split('{') for line in flows_raw.strip().splitlines())
    }

    part_one(parts, flows)
    part_two(flows)
