import re


def formatter(line:str):
    if line.startswith("mask"):
        mask = line.split("=")
        return ("mask", mask[1].strip())
    else:
        r = r"\[(\d+)\]"
        address = re.search(r, line).group(0).replace("[","").replace("]","")
        mem = line.split("=")
        return ("mem", int(address), int(mem[1].strip()))

data = []
memory = {}
with open("input.txt", "r") as f:
    data = list(map(formatter, f.readlines()))

current_mask = ""
allCurrentMasks = ""

def intBuilder(memValue):
    strTotal = "0b"
    for v in memValue:
        strTotal += str(v)
    return int(strTotal, 2)

def get_all_addresses(address, current_mask):
    addresses = [[]]
    binary_address = bin(address).replace("0b","")

    i = len(current_mask)
    b_len = len(binary_address)

    while i > 0:
        binary = False
        if b_len > 0:
            binary = binary_address[b_len-1]
        mask_value = current_mask[i-1]

        if (mask_value == "0") and binary != False:
            for adp in addresses:
                adp.append(binary)
        elif (mask_value == "X"):
            st_add = addresses.copy()
            addresses = []
            for ad in st_add:
                a1 = ad[:]
                a2 = ad[:]
                a1.append("0")
                a2.append("1")
                addresses.append(a1)
                addresses.append(a2)
        else:
            for eachAddress in addresses:
                eachAddress.append(mask_value)
        b_len -= 1
        i -= 1
    return list(map(intBuilder, addresses))

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
        all_addresses = get_all_addresses(address, current_mask)
        value = i[2]
        binary_value = bin(value).replace("0b","")

        for mem_address in all_addresses:
            memory[mem_address] = get_new_mem()

            i = len(memory[mem_address])
            b_len = len(binary_value)

            while i > 0:
                binary = False
                if b_len > 0:
                    binary = binary_value[b_len-1]
                mask_value = current_mask[i-1]

                if binary != False:
                    memory[mem_address][i-1] = binary

                """
                if (mask_value != "X"):
                    memory[mem_address][i-1] = mask_value
                elif binary != False:
                    memory[mem_address][i-1] = binary"""

                b_len -= 1
                i -= 1

total = 0
for value in memory.values():
    total += intBuilder(value)

print(f"Total: {total}")