# Program to find Smallest divisor of a number.

# Taking an input from the user. 
n=int(input("Enter an integer:"))

a=[]

# Setting up the range.
for i in range(2,n+1):
    if(n%i==0):
        a.append(i)
a.sort()

# Printing the statement
print("Smallest divisor is:",a[0])
