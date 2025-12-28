n = int(input())
# список блюд, которые можно приготовить в столовой
today = {input().strip() for _ in range(n)}

m = int(input())
cooked = set()

for _ in range(m):
    k = int(input())
    for _ in range(k):
        cooked.add(input().strip())

new_dishes = sorted(today - cooked)

if new_dishes:
    print("\n".join(new_dishes))
else:
    print("Готовить нечего")
