a = "0123456789ABCDEF"
n = 0

for x1 in a:
  for x2 in a:
    for x3 in a:
      for x4 in a:
        for x5 in a:
          for x6 in a:
            s = x1 + x2 + x3 + x4 + x5 + x6
            k = 0
            for t in s:
              if t == "5":
                k += 1

            # flag of number containing more than two numbers with condition of > 12
            f = None
            m = 0
            for i in range(0, len(s)):
              if int(s[i], 16) > 12:
                m += 1
              if (m == 2) and (int(s[i - 1], 16) > 12):
                f = True
              if m == 3:
                f = False

            if (k >= 1) and f:
              n += 1

print(n)
