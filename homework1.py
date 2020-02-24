'''
This program's goal is to make a program that will allow the user to input information about a book
including the code, cost, number of volumes you have, how many peeple will be in the class,
whether or not the book is requred and if its been used in the past. After that it will give the customer
all of the data, as well as how many books need to be ordered, how much it will cost and the profit.

Author: Cheryl Gardner
Course: ITM 313
'''

#Ask for the book code for the book
bookcode = input("What is the book code for your book? ")
#Ask for the book cost
bookcost = eval(input("What is the single copy cost for the book? "))
#Ask how many volumes you have
volumes = eval(input("How many volumes of the specified book do you currently have on hand? "))
#Ask how many people are expected to be in the class
classenrollment = eval(input("What is your prospective class enrollment for this class? "))
#Ask if the book is required or recommended
booktype = input("Is it a recommended or required book for the course? ")
#Ask if the book has been used in the past
pastuse = input("Has this book been used in the past? Answer with either Yes/No ")

#Calculate the number of books that need to be ordered 
bordered = classenrollment-volumes
#Calculate the cost of those books that need to be ordered
costofbooks = bordered * bookcost
#Calculate the profit that needs to be made
expectedprofit = .2 * costofbooks

#Add a buffer between the user input and the data that will be displayed
print("")

#Display all of the data for the data that the user inputed.
print("The book code for your book is:",bookcode)
print("The single copy cost for your book is $%.2f"%bookcost)
print("You have", volumes, "volumes of that book with your entered book code currently on hand")
print("Your prospective class enrollment for the class using this book is", classenrollment)
print("Your book listed is ",booktype, "book for that course")
print(pastuse, "this book has been used in the past")

#Add a space buffer betweeen the displayed data of the user's input and the calculation numbers
print("")

#Tell the user how many books need to be ordered
print("The number of books that needs to be ordered is", bordered)
#Tell the user how much it will cost to buy all of the books they need
print("The cost of those books is $%.2f"%costofbooks)
#Tell the store how much profit they are expected to make, only having to pay 80 percent for the books
print("The expected profit for the store is $%.2f"%expectedprofit)




