# Function for finding CAPITAL letters in a string and returning the index
def capital_indexes (x):
    return_list = []
    capital_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range (0, len (x)):
        for l in range (0, len (capital_letters)):
            if x [i] == capital_letters [l]:
                return_list.append (i)
    return return_list

# User input
user_input = input ("Type: ")

# Output of the index list
print (capital_indexes (user_input))