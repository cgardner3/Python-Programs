'''
Write a program that will ask for a user's full name,following the input the program should greet the user,
then the user will input a radius and from there, the program will calculate the volume and surface area
and display them to the user.

Author: Cheryl Gardner
Course: ITM 313
'''
#ask the user for their name
name = input("Hello, welcome to my program, please enter your name ")
#greet the user and tell them what the program is about 
print("Hello",name,"this program's purpose is to calculate the volume and surface area of a sphere from its radius, given as input.")

#ask the user for a radius
radius = eval(input("Please enter the radius of your sphere "))
#calculate the volume 
volume = (4/3) * 3.142 * radius * radius * radius
#calculate the surface area
area = 4 * 3.142 * radius * radius

#display the surface area
print("The surface area of a sphere with radius %.3f, is %.3f" % (radius,area))
#display the volume
print("The volume of a sphere with radius %.3f, is %.3f" % (radius,volume))
