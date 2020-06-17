'''
Homework 2 - Problem 2:
fill_completions(filename) takes a lename as input and returns a dictionary.
find_completions(prefix, c_dict) returns a set of strings.
main(), the test driver

See specifc specifications in HW2 PDF
'''

# Cite: Matt Pozsgai and I shared lists of prefixes and expected output for those prefixes based on our respective codes as a checking exercise.

from string import punctuation # cite: https://stackoverflow.com/questions/265960/best-way-to-strip-punctuation-from-a-string-in-python

# finds every (index, letter) from every word in the file and finds all words from the file that contain that (index, letter) -- appends (index, letter) : [words] to dictionary
# removes leading and ending punctuation and spaces from words but keeps internal punctuation
# ignores single letter words and words that contain non-alphabetic characters 
def fill_completions(filename):
    with open(filename, "r") as file:
        d = {} 
        for line in file:
            words = line.strip().split(" ")
            for word in words:
                word = word.casefold().strip().strip(punctuation)
                if len(word) != 1 and word.isalpha(): # ignore words that are one letter or that contain non-alphabetic characters
                    for i, letter in enumerate(word, 0):
                        if (i, letter) not in d:
                            d[(i, letter)] = {word}
                        else:
                            d[(i, letter)].add(word)
    return(d)


# find every word from c_dict that can complete a prefix
def find_completions(prefix, c_dict):
    l = [] # nested list where each list within the master list are the words available for each (i, letter)
    s = set()
    prefix = prefix.casefold().strip() # casefolds and strips white space in case user added spaces before or after the prefix
    for i, letter in enumerate(prefix, 0): # find prefix tuples to lookup in c_dict
        if (i, letter) in c_dict:
            l.append(c_dict[(i, letter)])
    if len(l) != 0: # if length of the prefix is 0 we want to return no completions
        for word in l[0]: # word for first (index, letter) of prefix needs to be in the list of words for every (index, letter) of the prefix
            counter = 1
            for i in range(1, len(l)): # the words that contain each tuple need to be in each list to be words that can complete the prefix
                if word in l[i]:
                    counter += 1
            if counter == len(prefix): # if the counter for the word equals the length of the prefix it means the word contains the prefix
                s.add(word) # cite: https://www.programiz.com/python-programming/methods/set/add
    return(s)


# test driver
# note: the file articles.txt has words that contain non-ASCII characters - such words are ignored - and words where the spacing is not correct (i.e. "...end.I believe..." - code separates words by spaces so recognizes "end.i" as a word)
def main():
    while True:
        prefix = input("Enter prefix: ")
        if prefix == "quit":
            print("Goodbye!")
            break
        completions = find_completions(prefix,fill_completions("articles.txt"))
        if completions == set():
            print("No completions")
        else:
            for completion in sorted(completions):
                print(completion)

                
# call test driver
if __name__ == "__main__":
    main()


        
                    
                    
                    
                    
        

