'''
Homework 3 - Problem 2:
Write a generator function that mimics the Unix grep command

See HW3 PDF for specific specifications
'''

# Cite: Matt Pozsgai and I checked our output from our individual codes against eachother's as a check on our own codes

def grep(pattern, lines, ignore_case = "False"):
    for line in lines:
        if (pattern.casefold() in line.casefold() and ignore_case == "True") or (pattern in line and ignore_case == "False"):  
            yield line

'''
# test1 - list of strings
print("\ntest1-1 - list of strings 1 - 'went' - case matters")
lines1 = ['I went to Poland.', 'He went to Spain.', 'She is very happy.']
for line in grep('went', lines1):
    print(line)
print("\ntest1-2 - list of strings 2 - 'i' - case does not matter")
for line in grep('i', lines1):
    print(line)
print('\nFind "i", case insensitive: ')
for line in grep('i', lines1, ignore_case="True"):
    print(line)

# test2 - file object
print("\ntest2-1 - articles.txt - 'prep' - case matters")
with open("articles.txt", 'r') as lines2:
    for line in grep('prep', lines2):
        print(line)
print("\ntest2-2 - articles.txt - 'KiL' - case does not matter")
with open("articles.txt", 'r') as lines2:
    for line in grep('KiL', lines2, ignore_case = "True"):
        print(line)

# test3 - generator
print("\ntest3-1 - generator from test2-1 - 'mus' - case matters")
with open("articles.txt", 'r') as lines2:
    for line in grep('mus', grep('prep', lines2)):
        print(line)
print("\ntest3-2 - generator from test2-1 - 'DeL' - case does not matter")
with open("articles.txt", 'r') as lines2:
    for line in grep('DeL', grep('prep', lines2), ignore_case = "True"):
        print(line)
'''
    
        
    
