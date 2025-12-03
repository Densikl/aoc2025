def num_length(num: int):
    return len(str(num))

result = 0
with open("input.txt") as file:
    line = file.read()
    data = [tuple(map(int, nums_range.split('-'))) for nums_range in line.split(',')]

    for id_range in data:
        first = id_range[0]
        second = id_range[1]
        first_length = num_length(first)
        second_length = num_length(second)
        if first_length == second_length and first_length % 2 != 0:
            continue
        if first_length % 2 != 0:
            first = 10**(first_length)
        if second_length % 2 != 0:
            second = 10**(second_length - 1) - 1

        for id in range(first, second + 1):
            mid = num_length(id) // 2
            id_str = str(id)
            if id_str[:mid] == id_str[mid:]:
                result += id

print(result)