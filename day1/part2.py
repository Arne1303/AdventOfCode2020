flag = 0
numbers = []


with open("input.txt", "r") as f:
    numbers = f.readlines()


for number in numbers:
    for test_number in numbers:
        for test_number_final in numbers:
            num1 = int(number)
            num2 = int(test_number)
            num3 = int(test_number_final)
            if (num1 + num2 + num3) == 2020:
                flag = num1 * num2 * num3
print(flag)