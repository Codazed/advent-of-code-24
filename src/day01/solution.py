with open("input.txt", "r") as f:
    lines = f.readlines()

list_a, list_b = [], []

for line in lines:
    split_line = line.split()
    list_a.append(int(split_line[0]))
    list_b.append(int(split_line[1]))

list_a = sorted(list_a)
list_b = sorted(list_b)

distances = []
for i in range(len(list_a)):
    distances.append(abs(list_a[i] - list_b[i]))

print("Part 1 Answer:", sum(distances))
