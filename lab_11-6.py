#Author: Andrew Tkacs

#Lab 11-6

sum_of_numbers = 0 #sum of numbers is 0

while True:
    user_input = input("Enter a number (or -1 to end): ")  #user to input number, tells them -1 to end it so they can see the added sum of all the numbers they added.

    try:                                          #I added this to ensure the user enters a number, a displays a message so they know no letters                                             #checks if the user entered a number
        number = float(user_input)
    except ValueError:
        print("Invalid input. Please enter a valid number.")     #if user doesnt enter a number, I errored so it repeats and asks for the user input again with a message.
        continue

    if number == -1:        #if the user inputs -1, it ends the code
        break

    sum_of_numbers += number  #adds all the numbers before the code ended from the person entering -1

print("Sum of all numbers entered:", sum_of_numbers)  #prints added numbers

#works