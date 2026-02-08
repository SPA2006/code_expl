def transform(M):
  tern = []
  n = M
  # перевод в троичную систему счисления
  if n == 0:
    tern = [0]
  while n > 0:
    tern.append(n % 3)
    n //= 3
  tern = tern[::-1]

  # применение преобразования к числу
  transformed = []
  for digit in tern:
    if digit == 0:
      transformed.append(2)
    elif digit == 2:
      transformed.append(0)
    else:
      transformed.append(1)

  while transformed and transformed[0] == 0:
    # removing the last element in list
    # transformed.pop()
    transformed.pop(0)

  # 173_10
  # ((0 * 10 + 1) * 10 + 7) * 10 + 3 == 100 * 1 + 10 * 7 + 1 * 3 == 173

  # 10111_2 == 23_10
  # ((1 * 2 + 0) * 2 + 0
  # (((((0 * 2 + 1) * 2 + 0) * 2 + 1) * 2) + 1) * 2 + 1 == 23

  # получаем 10-ную запись преобразованного числа
  N = 0
  for d in transformed:
    N = N * 3 + d
  #N = int("".join(transformed), 3)

  return abs(M - N)

K = 1864246

N = 1
while True:
  if transform(N) == K:
    print("min N:", N)
    break
  N += 1
