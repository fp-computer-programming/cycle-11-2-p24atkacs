#Author: Andrew Tkacs

#Lab 11-5

def name_multiplication():
    names = [] #empty list the stores the names

    for i in range(5):                           #gets 5 names from user
        name = input("Enter a name: ") 
        names.append(name)

    for name in names:
        num_letters = len(name) #gets number of letters in the name

        for _ in range(num_letters):
            print(name)

        i = 0
        while i < num_letters:
            print(name)
            i += 1

name_multiplication()

