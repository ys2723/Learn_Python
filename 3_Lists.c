# List

a = [1, 2, 3, 40, 5]
print(a)
print(a[2])
print(a[3])
a[2] = 89
print(a)

b = [2.56, "India", 45]
print(b)

# List slicing 

c = ["New Delhi", "Tokyo", "Beijing", "Berlin", "London", "Moscow"]
print(c)
print(c[0:4])
print(c[:6])
print(c[0:])
print(c[-5:])

# List Methods 

list = [1, 5, 3, 7, 11, 9]
print(list)
list_sorted = list.sort() 
print(list_sorted)
print(list)
# list.sort() sorts the original list, no need to store

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
