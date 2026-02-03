for i in range(1, 783):
  # строим двоичную запись числа N
  bin_i = bin(i)[2:]

  # второй шаг работы алгоритма
  if i % 5 == 0:
    bin_r = bin_i + "11"
  else:
    q = i // 5
    bin_q = bin(q)[2:]
    bin_r = bin_i + bin_q
  
  r = int(bin_r, 2)
  if (r >= 896 and i % 2 == 0):
    print(i)
    break

  
