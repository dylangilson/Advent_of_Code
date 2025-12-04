def part_one(banks):    
    print("Part One Solution: " + str(sum(max(int(bank[i] + bank[j]) for i in range(len(bank)) for j in range(i + 1, len(bank))) for bank in banks)))

def part_two(banks):
    def max_subsequence_as_int(bank, length=12):
        subsequence = []
        start_index = 0
        bank_length = len(bank)

        for remaining_digits in range(length, 0, -1):
            end_index = bank_length - remaining_digits + 1
            best_index = start_index

            for current_index in range(start_index, end_index):
                if bank[current_index] > bank[best_index]:
                    best_index = current_index

            subsequence.append(bank[best_index])
            start_index = best_index + 1

        return int(''.join(subsequence))

    print("Part Two Solution: " + str(sum(max_subsequence_as_int(bank) for bank in banks)))

if __name__ == '__main__':
    banks = open('input.txt').read().strip().split('\n')

    part_one(banks)
    part_two(banks)
