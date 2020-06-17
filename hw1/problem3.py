'''
Homework 1 - Problem 3:
What digits (1 through 9) can replace the letters P and E such that the following equation is true? PEEP = PP^(E) 
Write a program that checks each combination of digits and prints out the equation if it is satisfied.
'''

for i in range(1,10): # i is P
    for j in range(1,10): # j is E
        lhs = int(str(i) + str(j) + str(j) + str(i)) # cast PEEP as a string and then convert to an int for calculation
        rhs = int(str(i) + str(i)) # cast PP as a string and then convert to an int for calculation
        if lhs == rhs**j:
            print("{} = ({})^{}".format(lhs, rhs, j))

                                                    
