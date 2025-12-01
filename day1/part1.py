codes = tuple(range(0, 100))
state = 50
result = 0

with open('./input.txt') as file:
    for line in file:
        sign = -1 if line[0] == "L" else 1
        clicks = sign * int(line[1:])
        state = abs((clicks + state) % 100)
        result += 1 if state == 0 else 0


print(f"{result=}")