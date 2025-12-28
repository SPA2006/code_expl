n = int(input())
m = int(input())

mann = {input().strip() for _ in range(n)}
ovs = {input().strip() for _ in range(m)}

both = mann & ovs

if both:
    print(len(both))
else:
    print("Таких нет")
