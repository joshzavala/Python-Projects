# Function for multiples of 3
def m3 (r1, r2):
    multi3 = []
    for i in range (r1, r2):
        count3 = 3 * i
        if count3 <= 50:
            multi3.append(count3)
    return (multi3)

# Function for multiples of 7
def m7 (r1, r2):
    multi7 = []
    for j in range (r1, r2):
        count7 = 7 * j
        if count7 <= 50:
            multi7.append(count7)
    return (multi7)

# Function for multiples of 3 and 7
def m37 (list3, list7):
    multi37 = list(set(list3) & set(list7))
    multi37.sort()
    return (multi37)

# Function for iterating from 1 to 50
def iterate(r1, r2):
    iteratelist = []
    for o in range (r1, r2):
        if o <= 50:
            iteratelist.append(o)
    return (iteratelist)

# Function to replace multiples of 3 into text
def replace3 (iteratel, list3):
    for u in range (0, len(list3)):
        for l in range(0, len(iteratel)):
            if list3[u] == iteratel[l]:
                iteratel[l] = iteratel[l].replace(list3[u], "Cloud")
    return (iteratel)

# Function to replace multiples of 7 into text
def replace7 (iteratel, list7):
    for u in range (0, len(list7)):
        for l in range(0, len(iteratel)):
            if list7[u] == iteratel[l]:
                iteratel[l] = iteratel[l].replace(list7[u], "Computing")
    return (iteratel)

# Function to replace multiples of 3 and 7 into text
def replace37 (iteratel, list37):
    for u in range (0, len(list37)):
        for l in range(0, len(iteratel)):
            if list37[u] == iteratel[l]:
                iteratel[l] = iteratel[l].replace(list37[u], "CloudComputing")
    return (iteratel)

# Function to replace an integer list to string list
def strlist (strlistr):
    strlistr = list(map(str, strlistr))
    return (strlistr)

# Variables for modularity of range
r1 = 1
r2 = 51

# List variables for easier management of data
list3 = strlist(m3(r1, r2))
list7 = strlist(m7(r1, r2))
list37 = strlist(m37(list3, list7))
listi = strlist(iterate(r1, r2))
listr = replace7(replace3(replace37(listi, list37), list3), list7)

# Iteration of the completed list
for num in range (len(listr)):
    print (listr[num])