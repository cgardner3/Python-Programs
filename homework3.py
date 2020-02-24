'''
Write a program that will ask the user which structure they want to choose,
an I-Beam, rectangular beam or a cylindrical beam. From there, the user will then
be asked all of the dimensions for that beam and then the program will calculate
the moment of interia. Following that, the program will ask you want to go again
and if so will loop back and start over.

Author: Cheryl Gardner
Course: ITM 313
'''

print("Welcome to the Moment of Intertia Calculator")

choice = 'y'

selection = input("What type of beam do you want calculated, A for I-Beam B for rectangular beam or C for cylindrical beam ")

while (choice == 'y'):

    if(selection == 'a' or selection == 'A'):
       B = eval(input("Enter the value of the base, B "))
       H = eval(input("Enter the value of the height, H "))
       b = eval(input("Enter the value of the little base, b/2 "))
       h = eval(input("Enter the value of the little height, h "))
       intertia = ((B*H*H*H)-(2*b*h*h*h))/12

    if(selection == 'b' or selection == 'B'):
        b = eval(input("Enter the value of the base, b "))
        h = eval(input("Enter the value of the height, h "))
        intertia = (b*h*h*h)/12

    if(selection == 'c' or selection == 'C'):
        r = eval(input("Enter the value of the radius, r "))
        intertia = (3.14*r*r*r*r)/4

    print("")
    print("The value of the moment of intertia for the given shape is %.4f"%intertia)
    print("")

    choice = input("Do you want to do the calculation for another shape? Enter y or n ")

    if(choice == 'y'):

        selection = input("What type of beam do you want calculated, A for I-Beam B for rectangular beam or C for cylindrical beam ")

print("")
print("Thank you for using our calculator! Come again soon!")


        
