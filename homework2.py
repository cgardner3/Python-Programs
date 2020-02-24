'''
This program will display a menu that will allow the user to select between
the options of air, water, or steel. From there, they will input a distance
and the program will calculate how long it will take to travel in that medium.
Additionally, the program should make sure that the choice is one of the choices
and that no negative values are used for the distance.

Author: Cheryl Gardner
Course: ITM 313
'''

#Welcome the user to the new program
print("Welcome to the Speed of Sound")
#Ask the user to choose what type of medium they want the sound wave to travel through
choice = input("Please choose an option from our menu, A for air, B for water, or C for steel ")

#Show the user what medium they chose and assign the speed for that particular medium
if (choice == 'A' or choice == 'a'):
    print("You chose air as your medium")
    speed = 1100
elif (choice == 'B' or choice == 'b'):
    print("You chose water as your medium")
    speed = 4900
elif(choice == 'C' or choice == 'c'):
    print("You chose steel as your medium")
    speed = 16400

#If the user inputs an invalid choice, then tell them that they did not choose any of the options 
else:
    print("Sorry you did not select any of the available choices please try again")

#Only allow the user to input a distance if they selected a medium that is one of the three valid choices
if( choice == 'A' or choice == 'a' or choice == 'B' or choice == 'b' or choice == 'C' or choice == 'c'):  
    #Ask the user how far they want the sound wave to travel
    distance = eval(input("Please enter the distance that your sound wave is travelling in the selected medium in feet "))

    #Stop the user from entering a negative value for the distance
    if (distance < 0):
        print("Sorry but this distance is invalid, please try again")
    
    #If you enter a valid distance, then calculate the time it will take for that particular distance
    if(distance >= 0):
        #Calculate the time that it will take
        time = distance/speed

        #Display how much time it will take to travel through that sound wave
        print("The time that it will take to travel through the selected medium is %.4f" % time, "seconds")
        #Thank the user for using the program
        print("Thank you for using our sound wave program!")




