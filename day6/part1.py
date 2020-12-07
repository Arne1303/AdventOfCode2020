


if __name__ == "__main__":
    input = []
    groups = [[]]
    with open("input.txt", "r") as f:
        input = f.readlines()
    group_id = 0
    for i in input:
        if i == "\n":
            group_id += 1
            groups.append([])
        else:
            groups[group_id].append(i.strip())

    all_awnsers = 0
    for group in groups:
        total_group_awnsers = []
        for awnsers in group:
            for awnser in awnsers:
                if not awnser in total_group_awnsers:
                    total_group_awnsers.append(awnser)
        all_awnsers += len(total_group_awnsers)
    print(f"Total amount of Awnsers: {all_awnsers}")