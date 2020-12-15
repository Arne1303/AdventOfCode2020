
def removeInvalid(seats:list) -> list:
    return_value = []
    for seat in seats:
        if seat == "#":
            return_value.append(seat)
    return return_value

def getAdjacentOccupiedSeat(row:int, column: int, data:list) -> list:
    seats = []
    if row > 0:
        seats.append(data[row-1][column])
        if column > 0:
            seats.append(data[row-1][column-1])
        if column + 1 < len(data[row]):
            seats.append(data[row-1][column+1])


    if row + 1 < len(data):
        seats.append(data[row+1][column])
        if column > 0:
            seats.append(data[row+1][column-1])
        if column + 1 < len(data[row]):
            seats.append(data[row+1][column+1])


    if column > 0:
        seats.append(data[row][column-1])
    if column + 1 < len(data[row]):
        seats.append(data[row][column+1])
    return removeInvalid(seats)

def flipSeat(seat:str)->str:
    if seat == "L":
        return "#"
    elif seat == "#":
        return "L"
    else:
        return "."

def stripText(t:str) -> str:
    return t.strip()

if __name__ == "__main__":
    data = []
    with open("input.txt", "r") as f:
        data = list(map(stripText ,f.readlines()))

    row_amount = len(data)
    column_amount = len(data[0])

    seats_to_flip = [0]

    working_data = []
    for row in range(row_amount):
        working_data.append([])
        for column in range(column_amount):
            working_data[row].append(data[row][column])

    last_wd = []
    iteration = 0
    while len(seats_to_flip) != 0:
        seats_to_flip = []
        iteration += 1

        for row in range(row_amount):
            for column in range(column_amount):
                seat = working_data[row][column]
                if seat == "L" and len(getAdjacentOccupiedSeat(row, column, working_data)) == 0:
                    seats_to_flip.append((row, column))
                elif seat == "#" and len(getAdjacentOccupiedSeat(row, column, working_data)) >= 4:
                    seats_to_flip.append((row, column))

        for coordinates in seats_to_flip:
            row = coordinates[0]
            column = coordinates[1]
            original_seat = working_data[row][column]
            working_data[row][column] = flipSeat(original_seat)
        print(f"Flipped Seats: {len(seats_to_flip)}     ", end="\r")

    print()
    print(f"Iterations: {iteration}")
    total_occupied = 0
    for row in working_data:
        for seat in row:
            if seat == "#":
                total_occupied += 1
    print(f"Total Occupied: {total_occupied}")