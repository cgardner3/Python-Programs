'''
Write a program that will ask the user to enter how much their package weighs and
from there write code that will change the shipping rate based on how much it weighs.
After figuring out the shipping rate, display the shipping rate to the user.

Author: Cheryl Gardner
Course: ITM 313
'''

#Welcome the user to the shipping company
print("Welcome to the Fast Freight Shipping Company!!")
#Ask the user for the weight or their package
weight = eval(input("Please enter the weight of your package "))

#Assign the shipping charge depending on how much the package weighs
if (weight <= 2):
    charge = 1.10
elif(weight > 2 and weight <= 6):
    charge = 2.20
elif(weight > 6 and weight <= 10):
    charge = 3.70
else:
    charge = 3.80

#Add a space between the input and output
print("")
#Display the shipping charge to the user
print("The shipping charge for your package is $%.2f" % charge, "per pound")
#Thank them for their service
print("Thank you for coming! Come again soon!!!")
