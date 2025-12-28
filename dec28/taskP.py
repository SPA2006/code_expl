near = set()

while True:
    line = input()
    if line == "":
        break
    
    # (0, березка) (1, елочка) (2, зайка) (3, волк) (4, березка)
    words = line.split()
    for i, w in enumerate(words):
        if w == "зайка":
            if i > 0:
                near.add(words[i - 1])
            if i + 1 < len(words):
                near.add(words[i + 1])

for x in near:
    print(x)
