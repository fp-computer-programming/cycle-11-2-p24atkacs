#Author: Andrew Tkacs

#lab 11-1

def find_evens(num_A, num_B):
    even_numbers = [] #empty list to store evens

    for num in range(num_A, num_B):
        if num % 2 == 0:                #check if even
            even_numbers.append(num)

    return even_numbers

#Sets num a and num b equal to a number and finds the evens within those numbers, then prints result.
num_A = 10
num_B = 20
result = find_evens(num_A, num_B)
print(result)
