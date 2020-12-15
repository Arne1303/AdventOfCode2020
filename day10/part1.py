

if __name__ == "__main__":
    data = []
    joltage = 0
    with open("input.txt", "r") as f:
        data = f.readlines()
        data = list(map(int, data))
    data.sort()
    taplet_adapter = data[-1] + 3
    data.append(taplet_adapter)

    one_jol_diff = 0
    three_jol_diff = 0
    for adapter in data:
        diff = adapter - joltage
        if diff == 1:
            one_jol_diff += 1
        elif diff == 3:
            three_jol_diff += 1
        joltage = adapter

    print(f"We have {one_jol_diff} one jol diff and {three_jol_diff} Three jol diff")
    print(f"One jol diff times three jol diff: {one_jol_diff * three_jol_diff}")