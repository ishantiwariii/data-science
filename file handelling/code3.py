# Problem with w mode
# introducing append mode

# the w function will rewrite the txt file but the a mode will append the text in the file with the previous files 

f = open('sample.txt' , 'a')
f.write("\n hey i am recently added to the file ")
f.close()