#Author: Andrew Tkacs

#Lab 11-8

def length_multiples(input_list):
    new_list = [value * index for index, value in enumerate(input_list)]
    return new_list

# Test Case 1: Contains only integers

test_case_1 = [1, 2, 3, 4, 5]
result_1 = length_multiples(test_case_1)
print(f"Test Case 1 Result: {result_1}")

# Test Case 2: Contains integer and float values

test_case_2 = [1, 2.5, 3, 4.7, 5]
result_2 = length_multiples(test_case_2)
print(f"Test Case 2 Result: {result_2}")

# Test Case 3: Contains only strings

test_case_3 = ["a", "bb", "ccc", "dddd", "eeeee"]
result_3 = length_multiples(test_case_3)
print(f"Test Case 3 Result: {result_3}")
