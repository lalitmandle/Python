# create a file to store characters
f = open('myfile.txt','w')
#enter characters from keyboard
str = input('Enter text:')

#write the string into file
f.write(str)

#close the file 
f.close()

# Read characters from a file
f = open('myfile.txt','r')
#read all characters from file
str = f.read()

#display them on screen 
print(str)

#close the file
f.close()