import math
# f(x) = 7x^2 + 2x
def f(x):
  y = 7 * (x ** 2) + (2 * x)
  return y

def g(x, y):
  z = (x ** 2) + (y ** 2)
  return z

def hypotenuse(x, y):
  h = math.sqrt((x ** 2) + (y ** 2))
  return h

def is_positive(x):
  return x > 0

