from collections import defaultdict, deque
from math import lcm

def parse_modules(lines):
    module_states, output_connections = {}, defaultdict(list)

    for line in lines:
        left_side, right_side = line.split(' -> ')
        module_type = left_side[0] if left_side[0] in '%&' else ''
        module_name = left_side[1:] if module_type else left_side
        module_states[module_name] = ({}, module_type) if module_type == '&' else (['off'], module_type)

        for destination in right_side.split(', '):
            output_connections[module_name].append(destination)

    for module_name, (state, module_type) in module_states.items():
        if module_type == '&':
            for source_module, destinations in output_connections.items():
                if module_name in destinations:
                    state[source_module] = 0

    return module_states, output_connections

def simulate_button_press(module_states, output_connections):
    pulse_queue = deque([('button', 'broadcaster', 0)])
    low_pulse_count, high_pulse_count = 0, 0

    while pulse_queue:
        sender, receiver, pulse_value = pulse_queue.popleft()

        if pulse_value == 0:
            low_pulse_count += 1
        else:
            high_pulse_count += 1

        if receiver not in module_states:
            continue
        
        state, module_type = module_states[receiver]

        if module_type == '%':
            if pulse_value:
                continue
            
            state[0] = 'on' if state[0] == 'off' else 'off'
            output_pulse = state[0] == 'on'
        elif module_type == '&':
            state[sender] = pulse_value
            output_pulse = not all(state.values())
        else:
            output_pulse = pulse_value

        for destination in output_connections[receiver]:
            pulse_queue.append((receiver, destination, int(output_pulse)))

    return low_pulse_count, high_pulse_count

def part_one(lines):
    module_states, output_connections = parse_modules(lines)
    total_low_pulses = total_high_pulses = 0

    for _ in range(1000):
        low_pulses, high_pulses = simulate_button_press(module_states, output_connections)
        total_low_pulses += low_pulses
        total_high_pulses += high_pulses

    print("Part One Solution: " + str(total_low_pulses * total_high_pulses))

def part_two(lines):
    modules, connections = parse_modules(lines)

    for module_name, destinations in connections.items():
        if 'rx' in destinations:
            pre_rx_module = module_name
            break

    required_inputs = set(source for source, dests in connections.items() if pre_rx_module in dests)
    seen = {}
    button_presses = 0

    while len(seen) < len(required_inputs):
        button_presses += 1
        pulse_queue = deque([('button', 'broadcaster', 0)])

        while pulse_queue:
            sender, receiver, pulse = pulse_queue.popleft()

            if receiver == pre_rx_module and pulse == 1 and sender in required_inputs:
                if sender not in seen:
                    seen[sender] = button_presses

            if receiver not in modules:
                continue

            state, module_type = modules[receiver]

            if module_type == '%':
                if pulse:
                    continue
                
                state[0] = 'on' if state[0] == 'off' else 'off'
                out_pulse = state[0] == 'on'
            elif module_type == '&':
                state[sender] = pulse
                out_pulse = not all(state.values())
            else:
                out_pulse = pulse

            for dest in connections[receiver]:
                pulse_queue.append((receiver, dest, int(out_pulse)))

    print("Part Two Solution: " + str(lcm(*seen.values())))

if __name__ == '__main__':
    lines = open('input.txt').read().splitlines()

    part_one(lines)
    part_two(lines)
