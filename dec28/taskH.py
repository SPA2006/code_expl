n = int(input())
kids = []

# tuple == кортеж
# list(tuple(str, set))

for _ in range(n):
    ws = input().split()
    sn = ws[0]
    # список каш, которые любят дети
    ps = set(ws[1:])
    kids.append((sn, ps))

loved = input().strip()
ans = sorted(sn for sn, ps in kids if loved in ps)

if ans:
    print("\n".join(ans))
else:
    print("Таких нет")
