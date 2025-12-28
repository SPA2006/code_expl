counts = {}

while True:
    line = input()
    if line == "":
        break
    for w in line.split():
        counts[w] = counts.get(w, 0) + 1

for w, c in counts.items():
    print(w, c)
