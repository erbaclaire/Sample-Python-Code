'''
Homework 1 - Problem 2:
Write a program that asks the user for a comma-separated list of integers or integer ranges, and prints out 
a sorted list of all the integers with the ranges expanded into individual integers. You can assume that all
the integers entered as input are positive.
'''

while True:
    x  = input("Enter comma-separated list of integers or interger ranges: ")
    if x == "exit":
        print("Goodbye!")
        break
    l = x.replace(" ","").split(",") # replace spaces with blanks in case user added spaces in standard input
    l_new = [] # create a new list to append values to
    for value in l:
        if "-" in value: # if a range, add all values in the range to l_new as long as they are not already in l_new
            for v in range(int(value.split("-")[0]),int(value.split("-")[1])+1):
                if v not in l_new:
                    l_new.append(v)
        else: # if not a range, add value to l_new as long as it is not already in l_new
            if int(value) not in l_new:
                l_new.append(int(value))
    l_new.sort()
    print(l_new) 
