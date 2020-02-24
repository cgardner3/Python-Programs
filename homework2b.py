'''
Write a program that will ask the user to input the grades of their two courses
as well as the number of credits for each course. Following that, it will display the
grades in terms of descending order and then calculate the GPA. If the GPA is too
low it will display a warning message and if it is very high then it will congratulate
that student.

Author: Cheryl Gardner
Course: ITM 313
'''

#Welcome the user to the program
print("Welcome to the GPA Calculator!!!")
#Ask the user to enter their first grade on the 4.0 scale and store it as grade1
grade1 = eval(input("Please enter your grade for course 1 on the 4.0 scale. "))
#Ask the user to enter how many credits that course is and store it as credit1
credit1 = eval(input("Please enter the number of credits for course 1. "))
#Ask the user to enter their second grade on the 4.0 scale and then store it as grade2
grade2 = eval(input("Please enter your grade for course 2 on the 4.0 scale. "))
#Ask the user to enter how many credits the second course is and store it as credit2
credit2 = eval(input("Please enter the number of credits for course 2. "))

#Add a buffer in between display and input
print("")

#Display the two grades with the higher one going first
if(grade1 < grade2):
    print("The lower grade is",grade1)
    print("The other grade is", grade2)
elif(grade1 > grade2):
    print("The lower grade is",grade2)
    print("The other grade is",grade1)
#If the two courses are equal in grade, then tell the user that both grades are the same and then just display Grade 1 and 2
else:
   print("Both grades are the exact same")
   print("Grade 1 is",grade1)
   print("Grade 2 is",grade2)

#Calculate the GPA for that student
gpa = ((credit1 * grade1)+(credit2 * grade2))/(credit1 + credit2)

#Display the GPA to the student who is calculating their GPA
print("Your GPA for the semester is %.2f"%gpa)

#Add a space buffer
print("")

#Display a warning message if the GPA is below 2.0
if (gpa < 2.0):
    print("Your GPA is way too low you need to get it up")
#Display a congratulatory message if the GPA is greater than or equal to 3.5
if (gpa >= 3.5):
    print("Wow! You are doing incredible. Congrats! Keep it up!")

