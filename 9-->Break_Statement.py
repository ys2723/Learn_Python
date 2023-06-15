# Break Statement

# Else statement is not executed because loop didn't run fully (not a successful termination)

for i in range(8):
    print(i)
    if i == 5:
        break
# The loop would terminate when i becomes equal to 5. 
    
else:
    print("Line Completed") 
