# Basic Dictionary syntax

Dict = { "Yash": "Hello"}
print(Dict['Yash'])

Dict_2 = {
    "Name": "Yash",
    "Today's Date": "22 December 2022",
    "Today's Time": "1635 hrs",
    "Marks": [1,4,56]
}
print(Dict_2['Name'])
print(Dict_2["Today's Date"])
print(Dict_2["Today's Time"])
print(Dict_2['Marks'])
Dict_2['Marks'] = [34, 56, 89]     # update marks
print(Dict_2['Marks'])
print("\n--------------------------------\n")



# Dictionary inside a dictionary, nested dictionary

Dictionary = { 
    "Germany": "Berlin",
    "Another_Dictionary": {"West Germany": "Bonn"}
}
print(Dictionary['Germany'])
print(Dictionary['Another_Dictionary'])
print(Dictionary['Another_Dictionary']['West Germany'])
print("\n--------------------------------\n")


# Dictionary methods

Di = {
    "East Germany": "East Berlin",
    "West Germany": "Bonn",
    "Czechoslovakia": "Prague",
    "Yugoslavia": "Belgrade",
    "Soviet Union": "Moscow",
    45:56
}

print(Di.keys()) #prints the keys of the dictionary
print(list(Di.keys())) #prints the keys in list form

print(Di.values()) #prints the values of the dictionary
print(list(Di.values())) #prints the velues in list form

print(Di.items()) #returs both keys and values in the form of tuple
print("\n-------\n")

new_Di = { "Safavid Empire": 'Isfahan'}

Di.update(new_Di) #updates new key and value pair to old dictionary
print(Di)

print(Di.get('Yugoslavia'))
print(Di['Yugoslavia'])

#.get would retunr 'none' if word isn't present in dicionary but print di would throw an error
print(Di.get('Prussia')) # returns 'None'
print(Di['Prussia']) # returns an error
