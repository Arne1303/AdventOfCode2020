

if __name__ == "__main__":

    data = []
    with open("input.txt", "r") as f:
        data = f.readlines()
        data = list(map(int, data))

    data.sort()
    data.insert(0, 0)
    data.append(data[-1] + 3)

    total = []
    while len(total) < max(data) + 1:
        total.append(0)
    total[0] = 1

    for d in data:
        to_add = 0
        for i in range(4):
            index = d - i
            if index >= 0:
                to_add += total[index]
        total[d] = to_add

    print(f"Asdalksmdoaskmfokasnmdffgoimsdf {total[-1]}")


