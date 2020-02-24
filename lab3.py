'''
Write a program that will ask the user a multiplication problem from random numbers.
The program will make them keep trying until they get it right and then when they finally
do, ask them if they want to attempt another multiplication problem. If they say yes,
then they will be asked another math question, otherwise the program will end.

Author: Cheryl Gardner
Course: ITM 313
'''

#import random so a random number generator can be used
import random

#Set the values of guess and choice so that the loop will start and the answer to guess cannot be right
guess = -1
choice = 'y'

#Create a first random number that is between 1 and 9
number1 = random.randint(1,9)
#Create a second random number that is between 1 and 9
number2 = random.randint(1,9)

#Calculate the answer of the two random numbers
answer = number1 * number2

#Ask the user what number1 times number 2 is 
print("How much is",number1,"times",number2)

#Have the user guess what they think the value is
guess = int(input("Enter your guess: "))

#Keep the loop running while the value of choice is equal to y
while (choice == 'y'):

  #As long as the answer is wrong keep running this loo[
    while(guess != answer):
        #Print a buffer, then tell the user that their answer is not right and give them another guess
        print("")
        print("I am sorry that is not right. Please try again.")
        guess = int(input("Enter your guess: "))

    #Do this if they guess the correct answer to the problem
    if (guess == answer):
            #Print a buffer and then tell them congratulations and that they did a good job
            print("")
            print("Congratulations! That is the correct answer! Very Good!")

    #Ask the user whether or not they want to play the multiplication game again
    choice = input("Do you want to play again y or n? ")

    #If they want another problem, then repeat this loop until they want to stop
    if (choice == 'y'):
            #Create a first random number that is between 1 and 9
            number1 = random.randint(1,9)
            #Create a second random number that is between 1 and 9
            number2 = random.randint(1,9)

            #Calculate the product of the two random numbers
            answer = number1 * number2
            #Create another buffer and then ask the user another math question
            print("")
            print("How much is",number1,"times",number2)

            #Have the user put in a guess for the new multiplication problem
            guess = int(input("Enter your guess: "))

 #Create one last space buffer and thank the user for playing the game           
print("")
print("Thank you for playing, come again soon!")
       
        
