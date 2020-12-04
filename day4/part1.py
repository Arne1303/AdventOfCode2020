
valid_passwords = 0
v2 = 0

all_passwords = []
current_password = {}
lines = []

with open("input.txt","r") as f:
    lines = f.readlines()

for line in lines:
    if line == "\n":
        all_passwords.append(current_password)
        current_password = {}
    else:
        fields = line.split(" ")
        for field in fields:
            key, value = field.split(":")
            current_password[key.strip()] = value.strip()
all_passwords.append(current_password)


needed_keys = ["byr", "iyr", "eyr", "hgt", "ecl", "hcl", "pid"]
for password in all_passwords:
    needed = set(needed_keys)
    has = set(password.keys())
    if needed.issubset(has):
        valid_passwords += 1

print(f"Valid Passwords: {valid_passwords}")