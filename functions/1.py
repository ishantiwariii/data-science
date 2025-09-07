def is_even(n):
  if type(n)==int:
    if n % 2 == 0:
      print ("even hai ")
    else:
      print("odd hai ")
  else:
    print("pagal hai kya")

n = int (input("enter the number to check: "))

print(f"here is the result of the given number {is_even(n)}")