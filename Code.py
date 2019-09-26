word=input("Enter a word you want to reverse: ")
w=list(word)
u=''
for i in w:
    u=i+u
print('The reversed word is: ',u)
