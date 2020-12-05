
def get_row_number(input):
    current_range = [0, 127]
    for i in range(7):
        char = input[i]
        if char == "F":
            current_range[1] -= ((current_range[1] - (current_range[0] + 1)) / 2) + 1
        else:
            current_range[0] += (((current_range[1] + 1) - (current_range[0])) / 2)
    return int(current_range[0])


def get_seat_number(input):
    current_range = [0, 7]
    for i in range(3):
        char = input[i+7]
        if char == "L":
            current_range[1] -= ((current_range[1] - (current_range[0] + 1)) / 2) + 1
        else:
            current_range[0] += (((current_range[1] + 1) - (current_range[0])) / 2)
    return int(current_range[0])



if __name__ == "__main__":
    seats = []
    seat_ids = []
    with open("input.txt", "r") as f:
        seats = f.readlines()

    columns = []

    for i in seats:
        row = get_row_number(i)
        column = get_seat_number(i)
        seat_id = row * 8 + column
        seat_ids.append(seat_id)
    seat_ids.sort()


    print(f"Lowest: {seat_ids[0]}")
    print(f"Highest: {seat_ids[-1]}")