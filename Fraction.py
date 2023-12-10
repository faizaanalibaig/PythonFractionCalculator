# In Python, there isn't a built-in data type for fractions like (4/5).
# Let's create a custom datatype that can store values as fractions.

class Fraction:
  def __init__(self,n,d):
    self.num = n
    self.den = d

  def __str__(self):
    return '{}/{}'.format(self.num,self.den)

  def __add__(self,other):
    n_num = self.num*other.den + self.den*other.num
    d_num = self.den*other.den
    return '{}/{}'.format(n_num,d_num)

  def __sub__(self,other):
    n_num = self.num*other.den - self.den*other.num
    d_num = self.den*other.den
    return '{}/{}'.format(n_num,d_num)

  def __mul__(self.other):
    n_num = self.num*other.num
    d_num = self.den*other.den
    return '{}/{}'.format(n_num,d_num)

  def __truediv__(self.other):
    n_num = self.num*other.den
    d_num = self.den*other.num
    return '{}/{}'.format(n_num,d_num)

# Constructing an object of this class that takes two arguments which are numerator and denominator
# let it be X

X = Fraction(4,5)

print(X)
# when we print X the output should be like -----> 4/5

