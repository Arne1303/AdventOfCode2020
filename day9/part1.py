
def is_valid_next_number(preamble, number):
    for num in preamble:
        for n in preamble:
            if num + n == number:
                return True
    return False

if __name__ == "__main__":

    data = []
    preamble = []
    preamble_length = 25


    with open("input.txt", "r") as f:
        data = f.readlines()

    next_num = int(data.pop(0).strip())
    while len(data) > 0:
        while len(preamble) < preamble_length:
            preamble.append(next_num)
            next_num = int(data.pop(0).strip())

        if not is_valid_next_number(preamble, next_num):
            print(f"error: {next_num}")
            exit()

        preamble.pop(0)
    pass

print("Done")