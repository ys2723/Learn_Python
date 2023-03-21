# List

a = [1, 2, 3, 40, 5]
print(a)
print(a[2])
print(a[3])
a[2] = 89      # changes value because lists are mutable
print(a)
print("\n------------------------\n")

# A list can consist of any kind of data types

b = [2.56, "India", 45]
print(b)
print("\n------------------------\n")

# List slicing 

c = ["New Delhi", "Tokyo", "Beijing", "Berlin", "London", "Moscow"]
print(c)
print(c[0:4])
print(c[:6])
print(c[0:])
print(c[-5:])
print("\n------------------------\n")

# List Methods 

list = [1, 5, 3, 7, 11, 9]
print(list)
list_sorted = list.sort()      # list.sort() sorts the original list, no need to store
print(list_sorted)
print(list)
# list.sort() sorts the original list, no need to store
print("\n------------------------\n")

list.reverse()
print(list)

list.append(67) # will put '67' at the end of the list
print(list)

list.insert(2,5) # will insert '5' at the second position
print(list)

list.pop(3) # will remove element from position third
print(list)

list.remove(1) # will remove element
print(list)
