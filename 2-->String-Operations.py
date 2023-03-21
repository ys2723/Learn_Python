# Below is a code to show string concatenation 

greeting = "Good evening, "
name = "Yash"
print(greeting + name)
print("\n--------------------\n")



# Below is a code to show indexing and slicing in strings

a = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
print(a[5])           #indexing, would print thr 6th element
print(a[0:9])         #slicing, would print 0 to 8, first 9 elements
print(a[0:])          #would print 0 to end i.e. all elements
print(a[:8])          #would print 0 to 7, first 8 elements
print(a[-1])          #negative indexing, elements are marked from (-1) to (-n) from right to left
print("\n--------------------\n")



# Slicing with skip value

print(a[0:4:2])       # print 0 to 3 BUT print every second character
print(a[0:20:4])      # print 0 to 19 BUT print every fourth character
print("\n--------------------\n")


# String length 

b = "The city of Istanbul was earlier called Constantinople"
c = "Yash"
d = "hello"
print(len(b)) 
print(len(c))
print("\n--------------------\n")


# Other string operations

print(b.endswith("Constantinople"))
print(c.endswith("h"))                     #checks whether the string ends with 'h' or not
print(c.endswith("a"))
print("---------")

print(b.count("a"))                        #counts total number of 'a'
print(b.count("was"))                      #counts total number of 'was'
print("---------")

print(d.capitalize())                      #capitalizes first letter of the string
print("---------")

print(b.find("was"))                       #finds posiion of 'was'
print(b.find("Yash"))                      #output is "-1" because not present in string b
print("---------")

print(b.replace("Constantinople","what?")) #replaces all occurances of the old word with new word
print("\n--------------------\n")


# escaape sequence 

e = "The Lousiana purcahse was \tdone on\n30 April 1803"
print(e) 
#\n for next line
#\t for tab (space)
#\' for single quote
#\\ for backslash
print("\n--------------------\n")


st = "This  is a string with double spaces"

doubleSpaces = st.find("  ") # prints the location of double spaces
print(doubleSpaces)
