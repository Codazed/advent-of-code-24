with open("input.txt", "r") as f:
    lines = f.readlines()

list_a, list_b = [], []

for line in lines:
    split_line = line.split()
    list_a.append(int(split_line[0]))
    list_b.append(int(split_line[1]))

def part_01_solution(x: list[int], y: list[int]) -> int:
    x = sorted(x)
    y = sorted(y)

    distances = []
    for i in range(len(x)):
        distances.append(abs(x[i] - y[i]))
    return sum(distances)

print("Part 1 Answer:", part_01_solution(list_a, list_b))
