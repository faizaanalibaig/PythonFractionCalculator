# "In Python, there isn't a built-in data type for directly storing fractions in their fractional form, such as 4/5."
# Let's create a custom datatype that can store values as fractions.

class Fraction:
  # __init__ is a Constructor method to initialize the fraction with numerator (n) and denominator (d)
  def __init__(self,n,d):
    self.num = n
    self.den = d

  # __str__ is a special method that gets called when you use the str() function or object of this class is placed inside a print statement
  def __str__(self):
    # Return a string representation of the fraction in the form of 'numerator/denominator'
    return '{}/{}'.format(self.num,self.den)

  # __add__ is a special method for addition of fractions
  def __add__(self,other):
    # Addition of fractions: (a/b) + (c/d) = (ad + bc) / bd
    n_num = self.num*other.den + self.den*other.num
    d_num = self.den*other.den
    return '{}/{}'.format(n_num,d_num)

  # __sub__ is a special method for subtraction of fractions
  def __sub__(self,other):
    # Subtraction of fractions: (a/b) - (c/d) = (ad - bc) / bd
    n_num = self.num*other.den - self.den*other.num
    d_num = self.den*other.den
    return '{}/{}'.format(n_num,d_num)

  # __mul__ is a special method for multiplication of fractions
  def __mul__(self.other):
    # Multiplication of fractions: (a/b) * (c/d) = ac / bd
    n_num = self.num*other.num
    d_num = self.den*other.den
    return '{}/{}'.format(n_num,d_num)

  # __truediv__ is a special method for the division of fractions
  def __truediv__(self.other):
    # Division of fractions: (a/b) / (c/d) = ad / bc
    n_num = self.num*other.den
    d_num = self.den*other.num
    return '{}/{}'.format(n_num,d_num)

# Create instances of the Fraction class that take two arguments which are numerator and denominator
x = Fraction(4, 5)
y = Fraction(7, 3)

# Display the fractions
print("Fraction X:", x)
print("Fraction Y:", y)

# Perform addition
result_addition = x + y
print("Addition (X + Y):", result_addition)

# Perform subtraction
result_subtraction = x - y
print("Subtraction (X - Y):", result_subtraction)

# Perform multiplication
result_multiplication = x * y
print("Multiplication (X * Y):", result_multiplication)

# Perform division
result_division = x / y
print("Division (X / Y):", result_division)
