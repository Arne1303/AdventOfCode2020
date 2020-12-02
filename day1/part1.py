flag = 0
numbers = []


with open("input.txt", "r") as f:
    numbers = f.readlines()
    
for number in numbers:
    for test_number in numbers:
        num1 = int(number)
        num2 = int(test_number)
        if (num1 + num2) == 2020:
            flag = num1 * num2

print(flag)
