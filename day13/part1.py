

def formatter(data:str):
    r = []
    d = data.split(",")
    for s in d:
        if r != "X":
            r.append(s.strip())
    return r

start_timestamp = 0
timestamp = 0
buses = []
with open("input.txt", "r") as f:
    data = f.readlines()
    start_timestamp = int(data[0])
    buses = formatter(data[1])

timestamp = start_timestamp
best_bus = ""
while best_bus == "":
    timestamp += 1
    for bus in buses:
        if bus != "x" and (timestamp%int(bus)) == 0:
            best_bus = bus

waiting_time = timestamp - start_timestamp
print(f"Waiting time: {waiting_time}")
print(f"Best Bus: {best_bus}")
print(f"Flag: {int(best_bus) * waiting_time}")