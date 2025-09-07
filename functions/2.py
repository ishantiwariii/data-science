#here is the use of args and kwargs 
# if we want n numbers in a functions then we use this args 

def product_n (*args):
  product = 1 

  for i in args:
    product *=i

  print(args)
  return product 

print(product_n(1,2,3,4,5,6,7,8,6))


#here is the kwargs 

def countries (**kwargs):

  for (key, value) in kwargs.items():  #we use item to access the key and value of dictionary 
    print(f"{key} -> {value}")

  return

countries(india="delhi", pakistan="islamabad", us="washington DC")