n = int(input())
cnt = {}

for _ in range(n):
    s = input().strip()
    cnt[s] = cnt.get(s, 0) + 1

result = sum(c for c in cnt.values() if c > 1)
print(result)
