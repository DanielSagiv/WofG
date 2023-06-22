
#ex 1
var = 1


while var <= 10:
    print(var)
    var += var
#end of ex 1
    
#ex2
lines = int(input("Number of lines: "))

# Print the pattern
for x in range(lines):
    for y in range(x + 1):
        print(y, end=" ")
    print()
#end of ex 2


#ex 3
# Get the number 
userNumber = int(input("Enter a number: "))
var = 0

# Calculate 
for x in range(1, userNumber + 1):
    var += x

# Print 
print("The sum of all numbers from 1 to", userNumber, "is", var)
#end of ex 3

#ex 4

theList = [10, 20, 30, 40, 50]

# Print the list in reverse order
for x in range(len(theList) - 1, -1, -1):
    print(theList[x])
#end of ex 4