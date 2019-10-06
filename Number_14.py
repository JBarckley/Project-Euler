def collatz():
    total_sequences = []
    starting_values = []
    max = 0
    max_val = 0
    for i in range(2, 1000000):
        current_num = i
        collatz = []
        while current_num > 1:
            if (current_num < i) & (current_num != 1):
                for k in total_sequences[starting_values.index(current_num)]:
                    collatz.append(k)
                break
            else:
                collatz.append(current_num)
                if current_num % 2 == 0:
                    current_num = int(current_num / 2)
                else:
                    current_num = int((3 * current_num) + 1)
        print(collatz)
        if len(collatz) > max:
            max = len(collatz)
            max_val = collatz[0]
            print(max_val)
        total_sequences.append(collatz)
        starting_values.append(collatz[0])
    print(max)
    print(max_val)
    return total_sequences


def main():
    return collatz()


print(main())
