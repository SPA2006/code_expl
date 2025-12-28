n = int(input())
m = int(input())

cnt = {}
for _ in range(n + m):
    name = input().strip()
    cnt[name] = cnt.get(name, 0) + 1

only_one = sorted(name for name, c in cnt.items() if c == 1)

if only_one:
    print("\n".join(only_one))
else:
    print("Таких нет")
