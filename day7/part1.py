
OURBACKCOLOR = "shiny gold"

def getBag(rule):
    rule = rule.strip()
    rule = rule.replace("bag.", "bags.")
    rule = rule.replace("bag ", "bags ")
    rule = rule.replace("bag,", "bags,")
    rule = rule.replace("bags ", "")
    rule = rule.replace("bags.", "")
    containingBag, contents = rule.split("contain ")
    innerBags = {}

    if contents.strip() == "no other":
        return ("", {})

    allInnerBags = contents.split("bags, ")

    for bag in allInnerBags:
        amount = int(bag.split(" ")[0])
        color = " ".join(bag.split(" ")[1:-1])

        innerBags[color.strip()] = amount

    return (containingBag.strip(), innerBags)

def containsOurBag(bagColor, bagList):
    totalAmountShiny = 0

    if bagColor in bagList.keys():
        for bag in bagList[bagColor].keys():
            amount = bagList[bagColor][bag]
            if bag == OURBACKCOLOR:
                totalAmountShiny += amount
            else:
                totalAmountShiny += containsOurBag(bag, bagList)
    return totalAmountShiny

if __name__ == "__main__":

    # should look like {"bagColor":{
    #   "bagColor":amount
    #   "Sec,bg":amount
    # }}
    bagsToContent = {}
    with open("input.txt", "r") as f:
        content = f.readlines()
    for line in content:
        key, value = getBag(line)
        if key != "":
            bagsToContent[key] = value

    totalAmount = 0
    for bagColor in bagsToContent.keys():
        if containsOurBag(bagColor, bagsToContent) != 0:
            totalAmount += 1
    print(f"Total Amount: {totalAmount}")