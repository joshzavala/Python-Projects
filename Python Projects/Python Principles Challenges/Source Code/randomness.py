# Importing the random function in order to use it in the code
import random

# Function for finding random numbers between 1 and 100
def random_number (x, y):
    random_num = random.randint (x, y)
    return (random_num)

# User input for start number and end number range for random_number() function
start, end = int (input ("Type start #: ")), int (input ("Type end #: "))

# Calling random_number() function for use in the code
print (random_number (start, end))