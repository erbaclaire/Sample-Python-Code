'''
Homework 1 - Problem 1:
Write a program that asks the user for two lists of integers separated by commas and prints out a list of
integers that appear in both lists and have the digit 2 in them. There should be no duplicates in the output
list. Make sure the program works when the lists have different lengths
'''

while True:
    xs = input("Enter first list of integers: ")
    if xs == "exit": # will exit if enter "exit" for first list
        print("Goodbye!")
        break
    ys = input("Enter second list of integers: ")
    lxs = xs.replace(" ","").split(",") # replace spaces with blanks in case user added spaces to the list 
    lys = ys.replace(" ","").split(",") # replace spaces with blanks in case user added spaces to the list
    l_new = [] # generate empty lists to append 

    # only need to check if x is in lys because value needs to be in both lists so only need to check one against the other    
    for x in lxs: # if x is in lys and has the digit 2 and is not already in l_new then append x to l_new
        if ("2" in x) and (x in lys) and (int(x) not in l_new):
            l_new.append(int(x))
    l_new.sort()
    print(l_new)
                                                                                                                                                                         
