

data = []
with open("input.txt", "r") as f:
    data = f.readlines()



class Variables:

    def __init__(self):
        self.accumulator = 0
        self.currentLine = 0
        self.executed_lines = []
        self.data = []

def executeCode(var:Variables):
    if var.currentLine in var.executed_lines:
        raise NameError("I just executed something again :<")

    if var.currentLine >= len(var.data):
        print("It worked, it finished!")
        print(f"Acc is: {var.accumulator}")
    else:
        instruction, value = getInstruction(var.data[var.currentLine])

        var.executed_lines.append(var.currentLine)
        if instruction == "acc":
            var.accumulator += value
            var.currentLine += 1
        elif instruction == "jmp":
            var.currentLine += value
        else:
            var.currentLine += 1
            pass

        executeCode(var)

def getInstruction(line):
    instruction, value = line.split(" ")
    return instruction, int(value.strip())

def changeNopJmp(line):
    if line == "jmp":
        return "nop"
    else:
        return "jmp"

lineToChange = 0
finished = False
while not finished:

    changedData = data.copy()
    instruction, value = getInstruction(changedData[lineToChange])
    if not instruction == "acc":
        changedData[lineToChange] = changeNopJmp(instruction) + " " + str(value)
    lineToChange += 1

    try:
        var = Variables()
        var.data = changedData
        executeCode(var)
        finished = True
    except Exception as e:
        pass