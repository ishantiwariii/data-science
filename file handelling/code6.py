# reading upto n chars

f= open('sample.txt' , 'r')
s = f.read(10) #by the use of 10 inside the bracket it would only read 10 characters 
f.close()

print(s)