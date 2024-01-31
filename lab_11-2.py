#Author: Andrew Tkacs

#Lab 11-2

def is_palindrome(s):  #works with spaces and mixed capitols, as long as the letters make a palindrome.  
    s = ''.join(s.split()).lower()
    
    return s == s[::-1]

input_string = "race cAr" #example with spaces and weird capitals, still prints true.
result = is_palindrome(input_string) #result takes my input and runs it through the function.
print(result)  #printed true, works.

