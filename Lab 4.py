'''
This program counts the number of positive or negative numbers entered.
Print sum and average of numbers.
Debugging a program Assignment.
Name: Cheryl Gardner
'''

#Initialize all of the variables 
countpositive = 0
countnegative = 0
total = 0
count = 0

#Ask the user for their first number
num = eval(input("Enter an integer. Enter 0 to end input: "))

#As long as the number is not equal to 0, then keep running the loop
while (num != 0):

    #If the number is positive, then add one to the positive counter
    if (num > 0):
        countpositive = countpositive + 1

     #If the number is negative, then add one to the negative counter   
    elif (num < 0):
        countnegative +=1

    #Add that number to the total    
    total +=num
    #Add one to the count value
    count += 1

    #If the count value is not equal to 0, then ask for another number    
    if (count != 0):
        #Read the next number
        num = eval(input("Enter an integer. Enter 0 to end input: "))
        
#If count is equal to 0, then say that the only number entered is 0
if (count == 0):
    print("No numbers are entered except 0")



if(count != 0):
    #Display to the user how many positive, negative numbers there are, as well as the total and average value.   
    print("The number of positives is", countpositive)
    print("The number of negatives is", countnegative)
    print("The total is", total)
    print("The average is", (total / count))
