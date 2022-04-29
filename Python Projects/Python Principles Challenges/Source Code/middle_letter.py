# Function for finding the middle letter in a string and returning it
def mid (x):
    not_even = ""
    even = len (x) % 2
    mid_number = len (x) // 2
    
    if even == 0:
        return not_even
    else:
        return x [mid_number]

# User input
user_input = input ("Type: ")

# Calling the function with user input
print (mid (user_input))