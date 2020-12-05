
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

def get_missing_row(rows):
    row_amount = {}
    print(row_amount)


if __name__ == "__main__":
    seats = []
    seat_ids = []
    with open("input.txt", "r") as f:
        seats = f.readlines()

    row_amount = {}
    column_amount = {}

    for i in seats:
        row = get_row_number(i)
        column = get_seat_number(i)
        seat_id = row * 8 + column
        seat_ids.append(seat_id)

        if row in row_amount.keys():
            row_amount[row] += 1
        else:
            row_amount[row] = 1

        if row in column_amount.keys():
            column_amount[row].append(column)
        else:
            column_amount[row] = [column]

    seat_ids.sort()

    seating_row = 0
    seating_column = 0

    for k in row_amount.keys():
        if row_amount[k] != 8:
            seating_row = k
            break

    for i in range(8):
        if not i in column_amount[seating_row]:
            seating_column = i
            break

    print(f"Row Column: {seating_row} {seating_column}")
    our_seat_id = seating_row * 8 + seating_column
    print(f"Lets sit in: {our_seat_id}")