# Sets 

set_1 = {1, 2, 3, 4, 5}
print(set_1)

set_2 = {1, 2, 3, 1}
print(set_2)    #a set does not print repeated values

a = {}          #empty dictionary, not set
b = set()       #empty set

print(type(a))
print(type(b))
print("\n-----------------------------\n")

# Set methods

a = set()
print(type(a))
print(a)

a.add(5)
print(a)

a.add(4)
a.add(5)
a.add(8)
a.add(1)
a.add(9)
a.add(9)
print(a)
#cannot add dictionary or list inside sets because sets can't be changed but dictionary and lists can be changed


print(len(a))    #prints the number of items in the set

a.remove(1)      #removes element
print(a)

print(a.pop())   #removes random element from the set
print(a.clear()) #empties the set
