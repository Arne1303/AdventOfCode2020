def processInput(line:str) -> str:
    line = line.strip()
    return (line[0], int(line[1:]))

def betrag(x):
    if x < 0:
        x = -x
    return x

if __name__ == "__main__":
    data = []
    with open("input.txt", "r") as f:
        data = list(map(processInput, f.readlines()))

    x = 0
    y = 0

    wx = 10
    wy = 1

    for a in data:
        op, val = a
        if op == 'L':
            val = 360 - val
            op = 'R'

        if op == 'R':
            while val:
                wx, wy = wy, -wx
                val -= 90
        elif op == 'F':
            y += wy * val
            x += wx * val
        elif op == 'N':
            wy += val
        elif op == 'S':
            wy -= val
        elif op == 'E':
            wx += val
        elif op == 'W':
            wx -= val

    print(abs(x) + abs(y))
