


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
        group_size = 0
        total_group_awnsers = {}
        for awnsers in group:
            group_size += 1
            for awnser in awnsers:
                if not awnser in total_group_awnsers.keys():
                    total_group_awnsers[awnser] = 1
                else:
                    total_group_awnsers[awnser] += 1

        for awnser in total_group_awnsers:
            if total_group_awnsers[awnser] == group_size:
                all_awnsers += 1
    print(f"Total amount of Awnsers: {all_awnsers}")