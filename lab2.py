'''
This program will ask the user how many credits they have completed,
and then using that number determine what grade they are currently in
and then display what grade they are.

Author: Cheryl Gardner
Course: ITM 313

'''

#Welcome the user to the program that will calculate their grade
print("Hello, welcome to the Grade Level Calculator")

#Ask the user how many credit hours they have completed so far
credits = eval(input("Please enter the number of credits that you have completed. "))

#Create a space between the user's input and the output given by the computer
print("")

#If their credit hours is less then 32, then tell the user that they are a Freshman
if (credits < 32):
    print("You are currently a Freshman in college.")

#If their credit hours is between 32 and 63, then tell the user that they are a Sophomore
if(credits >= 32 and credits <= 63):
    print("You are currently a Sophomore in college.")

#If their credit hours is between 64 and 95, then tell the user that they are a Junior
if(credits > 63 and credits <= 95):
    print("You are currently a Junior in college.")

#If their credit hours are greater than 96, then tell the user that they are a Senior
if(credits > 95):
    print("You are currently a Senior in college.")

#Thank them for entering their credit hours
print("Thank you for entering your credit hours into the grade level calculator today, have a nice day!")

