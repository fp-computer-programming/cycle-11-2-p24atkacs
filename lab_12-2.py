#Author: Andrew Tkacs

#Lab 11-7

numbers = [1, 3, 7, 9, 12, 15, 18, 21, 25, 30]  #I used a number list

index = 0

while index < len(numbers):
    current_number = numbers[index]   #gets the numbers from the list

    if current_number % 3 != 0:   #checks if number is a multiple of three
        index += 1
        continue

    print(current_number)  #prints the number if it is a multiple of 3

    index += 1  #moves to the next index of the list.

#works.

