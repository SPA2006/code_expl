n = int(input())
have = {input().strip() for _ in range(n)}

m = int(input())
can = []

for _ in range(m):
    dish = input().strip()
    k = int(input())
    need = {input().strip() for _ in range(k)}
    if need.issubset(have):
        can.append(dish)

can.sort()

if can:
    print("\n".join(can))
else:
    print("Готовить нечего")
