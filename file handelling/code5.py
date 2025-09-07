# reading from files
# -> using read()

f= open('sample.txt' , 'r')
s = f.read()
f.close()

print(s)