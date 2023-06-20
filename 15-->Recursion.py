# Recursion concept 
# Recursion is a function which calls itself

def fact(a):
    product = 1
    for i in range(a):
        product = product * (i+1)
    return product
    
def fact_recursive(a):
    if a == 1 or a == 0:
        return 1
    return a * fact_recursive(a-1)
    
print(fact(5))
