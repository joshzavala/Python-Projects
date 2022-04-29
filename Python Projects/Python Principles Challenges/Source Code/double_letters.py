# Importing a function for easier counting of objects
import collections

# Function for finding double letters in a row in a string
def double_letters (string_name):
    
    # Variables:
    count = 0
    
    # Calling imported function for creating a dictionary that counts # of times the letters are in the string
    # Saves the letters as keys and the # of times counted as values
    d = collections.defaultdict(int)
    for char in string_name:
        d[char] += 1
    
    # Creating a list from the values of the dictionary values
    counter = list (d.values ())
    
    # Itterating through the list to see if a value is more than 1
    # If value more than 1 then break from the loop and add 1 to count variable
    for i in range (0, len (counter)):
        if counter[i] > 1:
            count += 1
            break
    
    # If count is more than 0 then the function returns True or if not then returns False
    if count > 0:
        return True
    else:
        return False
# End of Function

# Calling the function
print (double_letters ("hello"))
print (double_letters ("helo"))
print (double_letters ("hell"))
print (double_letters ("elo"))
print (double_letters ("ello"))
print (double_letters ("l"))
print (double_letters ("nono"))