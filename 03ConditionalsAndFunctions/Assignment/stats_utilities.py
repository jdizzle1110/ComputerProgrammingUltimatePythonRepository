def range(n1, n2, n3):
  a = max=(n1,n2, n3)
  c = min(n1, n2, n3)
  return a - c
print(range(3, 1, 5))
print(range(-1, 0, -1))
print(range(7, 7, 7))


print("##############")
def median(n1, n2, n3):
  a = max(n1, n2, n3)
  c = min(n1, n2, n3)
  if a == n1 and c == n2 or a == n2 and c == n1:
    return n3
  if a == n1 and c == n3 or a == n3 and c == n1:
    return n2 
  else:
    return n1
print(median(-6, -2, -4))
print(median(1, 3, 1))
print(median(0, -2, 1))