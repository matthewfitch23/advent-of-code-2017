test_input = '14	0	15	12	11	11	3	5	1	6	8	4	9	1	8	4'

cycles = 0
seen_configurations = {}
current_configuration = map(int, test_input.split('	'))


def redistribute_values(configuration):
    max_val = max(configuration)
    current_pos = configuration.index(max_val)
    configuration[current_pos] = 0
    while max_val > 0:
        current_pos += 1
        if current_pos >= len(configuration):
            current_pos = 0
        configuration[current_pos] += 1
        max_val -= 1
    return configuration


while str(current_configuration) not in seen_configurations.keys():
    seen_configurations[str(current_configuration)] = True
    current_configuration = redistribute_values(current_configuration)
    cycles += 1

print cycles
