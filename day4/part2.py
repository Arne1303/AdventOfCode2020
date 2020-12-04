
valid_passwords = 0

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
        valid = True

        try:
            byr = int(password['byr'])
            iyr = int(password['iyr'])
            eyr = int(password['eyr'])
            hgt = password['hgt']
            hcl = password['hcl']
            ecl = password['ecl']
            pid = password['pid']

            if byr < 1920 or byr > 2002:
                valid = False
            if iyr < 2010 or iyr > 2020:
                valid = False
            if eyr < 2020 or eyr > 2030:
                valid = False

            if "cm" in hgt:
                num = int(hgt.replace("cm", ""))
                if num < 150 or num > 193:
                    valid = False
            elif "in" in hgt:
                num = int(hgt.replace("in", ""))
                if num < 59 or num > 76:
                    valid = False
            else:
                valid = False

            if hcl[0] == "#" and len(hcl) == 7:
                valid_chars = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]
                for i in range(6):
                    if not hcl[i+1] in valid_chars:
                        valid = False
            else:
                valid = False

            valid_eye_colors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
            if not ecl in valid_eye_colors:
                valid = False

            if not len(str(pid)) == 9:
                valid = False
        except Exception as e:
            valid = False


        if valid:
            valid_passwords += 1

print(f"Valid Passwords: {valid_passwords}")