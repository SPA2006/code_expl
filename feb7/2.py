def to_ternary(n):
  if n == 0:
    return "0"
  s = ""
  while n > 0:
    s = str(n % 3) + s
    n //= 3
  return s

def compute_K(N):
  t = to_ternary(N)
  if N % 3 == 0:
    t_new = t + t[-2:]
  else:
    s = sum(int(c) for c in t)
    t_new = t + to_ternary(3 * s)

  return int(t_new, 3)

target = 826
best_K = None
best_diff = float("inf")

for N in range(1, 1000):
  K = compute_K(N)
  diff = abs(K - target)

  if diff < best_diff:
    best_diff = diff
    best_K = K

print("K: ", best_K)
#print("diff: ", best_diff)
