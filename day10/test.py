
def is_valid(array) -> bool:
    joltage = 0
    for adapter in array:
        diff = adapter - joltage
        if diff > 3:
            return False
        joltage = adapter
    return True

if __name__ == "__main__":
    data = []
    with open("input.txt", "r") as f:
        data = f.readlines()
        data = list(map(int, data))
    data.sort()
    taplet_adapter = data[-1] + 3
    data.append(taplet_adapter)

    diffrent_ways = []

    print(f"We have {one_jol_diff} one jol diff and {three_jol_diff} Three jol diff")
    print(f"One jol diff times three jol diff: {one_jol_diff * three_jol_diff}")