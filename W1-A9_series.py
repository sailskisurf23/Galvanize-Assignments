#return nth term from series

#initialize variables
uservar = int(input("program returns nth item in series, enter integer"))
result = 1
counter = 0

#compute series elements up to nth element
while counter < uservar:
    result = 2*result + 1
    counter = counter + 1

#print result
print(result)
