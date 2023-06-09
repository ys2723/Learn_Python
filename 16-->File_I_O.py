# File I/O

f = open('sample.txt', 'r') # opens file in reading mode
# default mode is r

data1 = f.read() # reads the entire file 
data2 = f.read(5) # reads the first 5 characters of the file
data3 = f.readline() # reads only 1 line from the file

print(data1)
print(data2)
print(data3)
f.close() #necessary to close file

# r = open for reading
# w = open for writing
# a = open for appending 
# + = open for updating

# Readline function

f = open('Sample text')

#reads first line
data = f.readline() # reads only 1 line from the file
print(data)

#reads second line
data = f.readline() # reads only 1 line from the file
print(data)

#reads third line 
data = f.readline() # reads only 1 line from the file
print(data)

#reads forth line
data = f.readline() # reads only 1 line from the file
print(data)

f.close()



Modes of opening a file: 

r = open for reading
w = open for writing
a = open for appending      (helps in adding text)
+ = open for updating         ('+' does the work of both 'r' and 'w')

'rb' will open for read in binary mode.
'rt' will open for read in text mode. ('t' is by default)

# Writing and Appending

f = open('sample.txt', 'w') 
f.write('This line is added to the file') 
f.close()

g = open('another.txt', 'a')
g.write('Appending') 
#this line will keep getting added the number of times we hit 'run'
g.close()

# With statement

with open('file.txt', 'r') as c:
    c.read() 
# no need to write close here because w
