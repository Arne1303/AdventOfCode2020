
class Ship(object):
    def __init__(self):
        self.facing = 1
        self.position = {
            "N":0,
            "E":0,
            "S":0,
            "W":0
        }
        self.directions = ["N", "E", "S", "W"]


    def getFacing(self):
        return self.directions[self.facing % 4]

    def doTurn(self, turn):
        turnDegrees = turn[1] // 90
        if turn[0] == "R":
            self.facing += turnDegrees
        elif turn[0] == "L":
            self.facing -= turnDegrees

    def move(self, turn):
        if turn[0] == "F":
            self.position[self.getFacing()] += turn[1]
        elif turn[0] in self.directions:
            self.position[turn[0]] += turn[1]
        else:
            self.doTurn(turn)

    def printValues(self):
        print(self.position)
        x = 0
        y = 0

        if self.position["N"] > self.position["S"]:
            y = self.position["N"] - self.position["S"]
        else:
            y = self.position["S"] - self.position["N"]


        if self.position["W"] > self.position["E"]:
            x = self.position["W"] - self.position["E"]
        else:
            x = self.position["E"] - self.position["W"]

        print(f"Total: {x + y}")

def processInput(line:str) -> str:
    line = line.strip()
    return (line[0], int(line[1:]))

if __name__ == "__main__":
    data = []
    with open("input.txt", "r") as f:
        data = list(map(processInput, f.readlines()))

    ship = Ship()
    for action in data:
        ship.move(action)
    ship.printValues()
