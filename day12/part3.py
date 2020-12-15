
class Ship(object):
    def __init__(self):
        self.waypointPosX = 10
        self.waypointPosY = 1

        self.posX = 0
        self.posY = 0

    def doTurn(self, turn):
        turnDegrees = turn[1]
        turnDirection = turn[0]

        if turnDirection == "L":
            turnDegrees = 360 - turnDegrees
            turnDirection = "R"

        if turnDirection == "R":
            while turnDegrees:
                self.waypointPosX, self.waypointPosY = self.waypointPosY, -self.waypointPosX
                turnDegrees -= 90

    def move(self, turn):
        action, amount = turn
        if action == "F":
            self.posY += self.waypointPosY * amount
            self.posX += self.waypointPosX * amount
        elif action == "N":
            self.waypointPosY += amount
        elif action == "S":
            self.waypointPosY -= amount
        elif action == "W":
            self.waypointPosX -= amount
        elif action == "E":
            self.waypointPosX += amount
        else:
            self.doTurn(turn)

    def betrag(self, x):
        if x < 0:
            x = -x
        return x

    def printValues(self):
        print(self.betrag(self.posX) + self.betrag(self.posY))

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
