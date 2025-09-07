# write lines

L = ["hello\n" , "hii\n" , "bye\n" , "bye\n"]
f = open('new.txt' , 'w')
f.writelines(L)
f.close()