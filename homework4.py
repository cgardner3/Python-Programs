'''
Write a program that will allow the user to input any number into the program.
The program will continue to run until the user enters the number -999999.
Once that number is entered, the program will then display the average as well
as both the smallest and largest numbers that were entered.

Author: Cheryl Gardner
Course: ITM 313
'''

total = 0
count = 0

num = eval(input("Enter any integer or enter -999999 to end the program: "))

while (num != -999999):

    total  += num
    count += 1

    if (count != 0):

            num = eval(input("Enter any integer or enter -999999 to end the program: "))

if (count == 0):
    print("The only number entered was -999999")

if(count != 0):
    average = total/count
    print("The average of all the numbers entered is: ", average)
