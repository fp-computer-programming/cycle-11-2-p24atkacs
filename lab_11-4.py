#Author: Andrew Tkacs

#Lab 11-4

def fibonacci(n):                                         #fibonacci function
    if n < 2 or n > 100:
        print("Please enter a number between 2 and 100.")
        return None

    fib_sequence = [0, 1]

    for int in range(2, n):                                                    #takes the users input (n) and gives the values based on my fib sequence
        next_number = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_number)

    print(f"Fibonacci Sequence with {n} values: {fib_sequence}")  #fib sequence prints

    sum_fibonacci = sum(fib_sequence)

    return sum_fibonacci  #adds all the numbers in the fib sequence based on the users value input

user_input = int(input("Enter a number between 2 and 100: "))

result = fibonacci(user_input)
if result is not None:
    print(f"Sum of the Fibonacci sequence: {result}")  #added number prints

    #done
