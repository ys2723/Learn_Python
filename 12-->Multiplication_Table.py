# Any number's table

num = int(input("Enter a number: "))
i = 0 
while i<11:
    print(num*i)
    i = i + 1

# Different method

hell = int(input("Enter a second number: "))
for t in range (1,11):
    print(str(num) + " " + "x" + " " + str(t) + " " + "=" + " " + str(num*t))
