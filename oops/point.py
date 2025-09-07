class Point:

  def __init__(self, x,y):
    self.x_cod = x
    self.y_cod = y

  def __str__(self):
    return f"<{self.x_cod},{self.y_cod}>"  
  
  def euclidean_method(self,other):
    """to check the euclidean distance """

    return ((self.x_cod - other.x_cod)**2 + (self.y_cod - other.y_cod)**2)**0.5
  
  def distance_from_origin(self):
    """to check the distance from origin """

    return (self.x_cod**2 + self.y_cod**2)**0.5
    # return self.euclidean_method(Point(0,0))
  
class Line:
  def __init__(self,A,B,C):
    self.A = A
    self.B = B
    self.C = C
  
  def __str__(self):
    return f"{self.A}x + {self.B}y + {self.C} = 0"
  
  def point_on_line(line , point):
    """to check whether a point lies on the line or not"""

    if line.A* point.x_cod + line.B* point.y_cod + line.C == 0:
      return "lies on the line"
    else:
      return "not lies on the line "
    
line1= Line(3,4,5)
p1=Point(2,4)

print(line1.point_on_line(p1))