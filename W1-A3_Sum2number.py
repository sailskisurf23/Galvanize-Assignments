uservar = int(input("Enter an integer you would like to sum to: "))

def sumtonum(var1):
    """Returns the factorial of var1"""
    counter = 1
    result = 0
    while counter <= var1:
        result = result + counter
        counter = counter + 1
    return result

print("The sum of the numbers 1 to "+str(uservar)+" is " + str(sumtonum(uservar)))
