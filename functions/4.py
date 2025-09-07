def total_sum (*args):
  """
  here this is a function to provide the sum of all the given value in aurguments

  """
  sum = 1 

  for i in args:
    sum +=i

  return sum

print(total_sum.__doc__)

print(total_sum(1,2,3,4,5,6,6))

# we also can delete the functions using del functions 
# functions are first class citizens in python 
# it is immutable 

