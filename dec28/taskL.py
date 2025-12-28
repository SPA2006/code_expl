n = int(input())
cnt = {}

for _ in range(n):
    s = input().strip()
    cnt[s] = cnt.get(s, 0) + 1

# list(tuple(str, int))
dups = sorted((name, c) for name, c in cnt.items() if c > 1)

if not dups:
    print("Однофамильцев нет")
else:
    for name, c in dups:
        print(f"{name} - {c}")
