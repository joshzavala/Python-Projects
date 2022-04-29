# Function for type checking integer variables
def only_ints (x, y):
    if type (x) == type (1) and type (y) == type (1):
        return True
    else:
        return False    

print (only_ints (1, 2))