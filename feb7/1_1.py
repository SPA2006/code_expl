a = "ОДСАЦЛФЩ"
b = len(a)

for i1, x1 in enumerate(a):
  for i2, x2 in enumerate(a):
    for i3, x3 in enumerate(a):
      for i4, x4 in enumerate(a):
        s = x1 + x2 + x3 + x4

        m = 0
        for t in s:
          if t == "Л":
            m += 1

        k = i1 * b ** 3 + i2 * b ** 2 + i3 * b + i4 + 1
        if k % 2 == 1 and m >= 3 and s[0] != "А" and s[-1] != "А":
          print(k)
          break
