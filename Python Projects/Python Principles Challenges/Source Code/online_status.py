# Function for finding how many user[s] are online and offline
def online_count (x):
    values_list = list (x.values ())
    count_on = 0
    count_off = 0
    for i in range (0, len (values_list)):
        if values_list [i] == "online":
            count_on = count_on + 1
        elif values_list [i] == "offline":
            count_off = count_off + 1
            
    print ("Online: ", count_on)
    print ("Offline: ", count_off)
        
# Dictionary for online statuses 
statuses = {
    "Alice": "online",
    "Bob": "offline",
    "Eve": "online",
    }
    
online_count (statuses)