'''
Homework 7 - Problem 3
'''

import pandas as pd
import numpy as np

rainfall = pd.read_csv('hw7_data/Seattle2014.csv')['PRCP'].values
inches = rainfall / 254.0

# 1. For rainy (more than 0 inches), what was the average and stddev of rainfall
print("2014 average Seattle rainfall on rainy days: {} inches".format(np.mean(inches[inches>0])))
print("2014 standard deviation of Seattle rainfall on rainy days: {} inches".format(np.std(inches[inches>0])))

# 2. Though we don't have labels for days of the week, we do know that datapoints separated by 7 days will be the same day of the week. For example, inches[::7] will be the rainfall for one day of the week, inches[1::7] will be another day of the week, and so on. (a) For each of the 7 days of the week what was the average/stddev of rainfall, (b) For each of the 7 days, what was the ration of rainy days (more than 0 inches) to total days?
days_of_week = inches[:364].reshape(-1,7)
print("Average rainfall (inches) in Seattle on [Day1, Day2, Day3, Day4, Day5, Day6, Day7] of the week in 2014:\n {}".format(np.mean(days_of_week, axis=0)))
print("Standard deviation (inches) of rainfall in Seattle on [Day1, Day2, Day3, Day4, Day5, Day6, Day7] of the week in 2014:\n {}".format(np.std(days_of_week, axis=0)))
print("Ratio of rainy days to total days on [Day1, Day2, Day3, Day4, Day5, Day6, Day7] of the week in Seattle in 2014:\n {}".format(np.sum(days_of_week>0, axis=0)/(days_of_week.size/7))) 

# 3. In each 7-day period, what was the total rainfall? (There should be 52 values here: one value for each 7-day period)
weeks_of_year = inches[:364].reshape(52,-1)
print("Total rainfall (inches) in Seattle in week [Week1 ... Week52] of the year in 2014:\n {}".format(np.sum(weeks_of_year, axis=1)))

