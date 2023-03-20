# Below is a code to show string concatenation 

greeting = "Good evening, "
name = "Yash"
print(greeting + name)


# Below is a code to show indexing and slicing in strings

a = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
print(a[5]) #indexing 
print(a[0:9]) #slicing
print(a[0:])
print(a[:8])
print(a[-1]) #negative indexing


# Slicing with skip value

print(a[0:4:2]) # print 0 to 3 BUT print every second character
print(a[0:20:4]) # print 0 to 19 BUT print every fourth character


# String length 

b = "The city of Istanbul was earlier called Constantinople"
c = "Yash"
d = "hello"
print(len(b))
print(len(c))


# Other string operations

print(b.endswith("Constantinople"))
print(c.endswith("h")) #checks whether the string ends with 'h' or not
print(c.endswith("a"))

print(b.count("a")) #counts total number of 'a'
print(b.count("was")) #counts total number of 'was'

print(d.capitalize()) #capitalizes first letter of the string

print(b.find("was")) #finds posiion of 'was'
print(b.find("Yash")) #output is "-1" because not present in string b

print(b.replace("Constantinople","what?")) #replaces all occurances the old word with new word


# escaape sequence 

e = "The Lousiana purcahse was \tdone on\n30 April 1803"
print(e) 
#\n for next line
#\t for tab (space)
#\' for single quote
#\\ for backslash




# Replacing a letter with user input

letter = '''Dear <|NAME|>,
Greetings from ABC coding house. I am happy to tell you about your selection
You are selected!
Have a great day ahead!
Thanks and regards,
Bill
Date: <|DATE|>
'''
name = input("Enter Your Name\n")
date = input("Enter Date\n")
letter = letter.replace("<|NAME|>", name)
letter = letter.replace("<|DATE|>", date)
print(letter)




st = "This is a string with double  spaces"

doubleSpaces = st.find("  ")
print(doubleSpaces)


