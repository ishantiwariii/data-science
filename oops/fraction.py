class fraction :
  """
  here is the class for operating with function 

  """
  def __init__(self,x,y):
    self.num = x
    self.den = y

  def __str__(self):
    return f"{self.num}/{self.den}"
  
  def __mul__(self,other):
    new_num = self.num*other.num
    new_den = self.den*other.den
    return f"{new_num}/{new_den}"
  
  def __add__(self,other):
    new_num = self.num*other.den + other.num*self.den
    new_den = self.den*other.den
    return f"{new_num}/{new_den}"
  
  def __sub__(self,other):
    new_num = self.num*other.den - other.num*self.den
    new_den = self.den*other.den
    return f"{new_num}/{new_den}"    
  
  def __truediv__(self,other):
    new_num = self.num*other.den
    new_den = self.den*other.num    
    return f"{new_num}/{new_den}"
  
# here is the way to input the data from user

x1 = int(input("enter the first numerator "))
x2 = int(input("enter the second numerator "))
y1 = int(input("enter the first denominator "))
y2 = int(input("enter the second denominator "))

frac1 = fraction(x1,y1)
frac2 = fraction(x2,y2)

print("Addition of the two fractions",frac1+frac2)
print("Multiplication of the two fractions",frac1*frac2)
print("Subtraction of the two fractions",frac1-frac2)
print("Division of the two fraction",frac1/frac2)