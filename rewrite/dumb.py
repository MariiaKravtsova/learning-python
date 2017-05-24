s = "mamaaaap"

def nonRepeated(s):
  counter = 0;
  for l in s:
    if s.count(l) == 1:
      return s

print(nonRepeated(s))

def getIntegerComplement (n):
    b = (1 << n.bit_length()) - 1
    return n ^ b

m = set([1, 2, 9, 1,2, 3, 1, 4, 1, 5, 7])

print(getIntegerComplement(50))

nonRepeated(s)


print(m)

