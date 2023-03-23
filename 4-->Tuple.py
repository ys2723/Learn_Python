# Tuple

a = (9, 1, 4, 7, 8, 44)
print(a)

b = ()
print(b) # empy tuple

c = (1)
print(c) # not a tuple with single element, not a tuple, its a number

d = (1,)
print(d) # this is a tuple with single element
# tuple with only one element needs a comma

# Tuple methods

print(a.count(4)) # will return the number of times '4' occured
print(a.index(4)) # will return the index of first occurance of '4'

print(sum(a)) # sums all elements in tuple a
