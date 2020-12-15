import re


def formatter(line:str):
    if line.startswith("mask"):
        mask = line.split("=")
        return ("mask", mask[1].strip())
    else:
        r = r"\[(\d+)\]"
        address = re.search(r, line).group(0).replace("[","").replace("]","")
        mem = line.split("=")
        return ("mem", address, int(mem[1].strip()))

data = []
memory = {}
with open("input.txt", "r") as f:
    data = list(map(formatter, f.readlines()))

current_mask = ""
def get_new_mem():
    current_value = []
    for i in range(36):
        current_value.append(0)
    return current_value

for i in data:
    if i[0] == "mask":
        current_mask = i[1]
    else:
        address = i[1]
        value = i[2]
        binary_value = bin(value).replace("0b","")

        memory[address] = get_new_mem()

        i = len(memory[address])
        b_len = len(binary_value)

        while i > 0:
            binary = False
            if b_len > 0:
                binary = binary_value[b_len-1]
            mask_value = current_mask[i-1]


            if (mask_value != "X"):
                memory[address][i-1] = mask_value
            elif binary != False:
                memory[address][i-1] = binary

            b_len -= 1
            i -= 1

def intBuilder(memValue):
    strTotal = "0b"
    for v in memValue:
        strTotal += str(v)
    return int(strTotal, 2)

total = 0
for value in memory.values():
    total += intBuilder(value)

print(f"Total: {total}")