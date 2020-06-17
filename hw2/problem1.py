'''
Homework 1 - Problem 1:
You are provided indebtedness.csv, which describes the total debt owed by employees of various de-partments at given dates. 
Your task is to write a program that displays the total amount of debt at each date in the csv le. 
The output must be sorted by date, starting from the oldest entries (10/14/2011) and continuing to thepresent. 
The total amount owed should be displayed rounded to the nearest dollar with thousands separated by commas.
'''

# Cite: Matt Pozsgai and I checked our output from our individual codes against eachother's

import csv # csv file methods and functions (cite: https://docs.python.org/3/library/csv.html)
from datetime import datetime # does date formatting (cite: https://docs.python.org/3/library/datetime.html)
dates_totaldebt = []
with open('indebtedness.csv', newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader) # skips header (cite: https://evanhahn.com/python-skip-header-csv-reader/)
    for row in csvreader:
        counter = 0 # resets counter with each row read
        date = datetime.strptime(row[0], "%m/%d/%Y") # formats date
        value = row[6].strip("$,") # remove '$' and ',' from amount to convert to float later

        # if the date already exists in dates_totaldebt, add the debt amount to the existing entry
        # there are some entries that are blank for total debt amount - can pass over these since they do not add value to total debt amount and cannot be converted to float
        # if counter is 0 it means that the date does not exist in dates_totaldebt yet, so append first instance to it
        for dates in dates_totaldebt: 
            if date in dates and value != "": 
                dates[1] += float(value)
                counter += 1
        if counter == 0 and value != "": 
            dates_totaldebt.append([date,float(value)])
                
for dates in sorted(dates_totaldebt):
    print("{}: {:,}".format(dates[0].strftime("%m/%d/%Y"),int(round(dates[1],0))))




        
            




 
        
