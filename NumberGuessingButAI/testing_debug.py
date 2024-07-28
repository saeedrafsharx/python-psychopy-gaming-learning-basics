def f1(x, y):
  return x / y
  
def f2(x, y):
  x = x + 5
  y = y * 2
  return f1(x, y)
  
z = f2(4, 2)
print(z)