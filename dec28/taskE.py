n = int(input())
m = int(input())

"""
mann = {input().strip() for _ in range(n)}
ovs = {input().strip() for _ in range(m)}
"""

cnt = {}
for _ in range(n + m):
    name = input().strip()
    cnt[name] = cnt.get(name, 0) + 1

only_one = sum(1 for v in cnt.values() if v == 1)

if only_one:
    print(only_one)
else:
    print("Таких нет")

"""
if mann ^ ovs:
    print(len(mann ^ ovs))
else:
    print("Таких нет")
"""
