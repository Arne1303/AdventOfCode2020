

data = []
with open("input.txt", "r") as f:
    data = f.readlines()



class Variables:
    accumulator = 0
    currentLine = 0
    executed_lines = []

def executeCode(var:Variables):
    if var.currentLine in var.executed_lines:
        print("Would Execute again")
        print(f"Acc is: {var.accumulator}")
        exit()

    instruction, value = getInstruction(data[var.currentLine])

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


var = Variables()
executeCode(var)