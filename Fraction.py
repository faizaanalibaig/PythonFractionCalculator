# In Python, there isn't a built-in data type for fractions like (4/5).
# Let's create a custom datatype that can store values as fractions.

class Fraction:
  # Constructor method to initialize the fraction with numerator (n) and denominator (d)
  def __init__(self,n,d):
    self.num = n
    self.den = d

  # __str__ is a special method that gets called when you use the str() function or object of this class is placed inside a print statement
  def __str__(self):
    # Return a string representation of the fraction in the form of 'numerator/denominator'
    return '{}/{}'.format(self.num,self.den)

  # __add__ is a special method for addition of fractions
  def __add__(self,other):
    n_num = self.num*other.den + self.den*other.num
    d_num = self.den*other.den
    return '{}/{}'.format(n_num,d_num)

  # __sub__ is a special method for subtraction of fractions
  def __sub__(self,other):
    n_num = self.num*other.den - self.den*other.num
    d_num = self.den*other.den
    return '{}/{}'.format(n_num,d_num)

  # __mul__ is a special method for multiplication of fractions
  def __mul__(self.other):
    n_num = self.num*other.num
    d_num = self.den*other.den
    return '{}/{}'.format(n_num,d_num)

  # __truediv__ is a special method for division of fractions
  def __truediv__(self.other):
    n_num = self.num*other.den
    d_num = self.den*other.num
    return '{}/{}'.format(n_num,d_num)

# Constructing an object of this class that takes two arguments which are numerator and denominator
# let it be X

X = Fraction(4,5)

print(X)
# when we print X the output should be like -----> 4/5

