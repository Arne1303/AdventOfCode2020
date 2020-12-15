
def is_valid_next_number(preamble, number):
    for num in preamble:
        for n in preamble:
            if num + n == number:
                return True
    return False

def test_numbers(all_numbers, start, end, target):
    tst = all_numbers[start: end]
    total = 0
    for num in tst:
        total += num
    return total == target

if __name__ == "__main__":

    data = []
    preamble = []
    preamble_length = 25

    corrupted_value = 0


    with open("input.txt", "r") as f:
        data = f.readlines()
    all_data =list(map(int, data.copy()))

    next_num = int(data.pop(0).strip())
    while len(data) > 0:
        while len(preamble) < preamble_length:
            preamble.append(next_num)
            next_num = int(data.pop(0).strip())

        if not is_valid_next_number(preamble, next_num):
            corrupted_value = next_num
        preamble.pop(0)

    all_data.remove(corrupted_value)

    spacing = 2
    step = 0
    found = False
    num = []
    while spacing < len(all_data) and not found:
        while (step + spacing) < len(all_data):
            if test_numbers(all_data, step, step + spacing, corrupted_value):
                num = all_data[step: step + spacing]
                found = True
                break
            step += 1
        step = 0
        spacing += 1

    total = 0
    low = num[0]
    high = 0
    for n in num:
        if n < low:
            low = n
        if n > high:
            high = n
        total += n
    print(f"Total: {total}")
    print(f"Low: {low} High: {high}")
    print(f"Encryption weakness: {low + high}")

print("Done")