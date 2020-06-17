'''
Homework 7 - Problem 4
'''

import numpy as np
np.set_printoptions(suppress=True, precision=5) # cite: https://docs.scipy.org/doc/numpy/reference/generated/numpy.set_printoptions.html
import pandas as pd

fish = pd.read_csv('hw7_data/SnorkelSurveyExtract.csv')
fish_density = fish['Estimated density (fish/mi)'].values
water_temp = fish['Water temperature (C)'].values
water_depth = fish['Average water depth (ft)'].values
fdensity_clean = fish_density[~np.isnan(fish_density) & ~np.isnan(water_temp) & ~np.isnan(water_depth)]
wtemp_clean = water_temp[~np.isnan(fish_density) & ~np.isnan(water_temp) & ~np.isnan(water_depth)]
wdepth_clean = water_depth[~np.isnan(fish_density) & ~np.isnan(water_temp) & ~np.isnan(water_depth)]

print("What are the average fish densities for these water temperature intervals: \n(a) Very cold water: less than 10 C?")
print("{} fish/mi".format(np.mean(fdensity_clean[wtemp_clean < 10])))
print("(b) Cold water: between 10C and 20C?")
print("{} fish/mi".format(np.mean(fdensity_clean[(wtemp_clean >= 10) & (wtemp_clean < 20)])))
print("(c) Warm water: greater than 20C?")
print("{} fish/mi".format(np.mean(fdensity_clean[wtemp_clean > 20])))

print("\nWhat are the average fish densities for these water depth intervals?: \n(a)Shallow water: less than 4 ft?")
print("{} fish/mi".format(np.mean(fdensity_clean[wdepth_clean < 4])))
print("(b) Mid-depth water: between 4 and 8 ft")
print("{} fish/mi".format(np.mean(fdensity_clean[(wdepth_clean >= 4) & (wdepth_clean < 8)])))
print("(c) Deep water: greater than 8 ft")
print("{} fish/mi".format(np.mean(fdensity_clean[wdepth_clean > 8])))

print("\nFor each of the 10 most-dense fish samples, show: (a) Fish density, (b) Water temperature, (c) Water depth")
most_dense = np.sort(fdensity_clean)[-10:]
is_in = np.isin(fdensity_clean, most_dense)
print("[fish density (fish/mi), water temp (C), water depth (ft)]")
summary = np.hstack([fdensity_clean[is_in].reshape(-1,1), wtemp_clean[is_in].reshape(-1,1), wdepth_clean[is_in].reshape(-1,1)])
print(summary[summary[:,0].argsort()[::-1]]) # cite: https://docs.scipy.org/doc/numpy-1.15.1/reference/generated/numpy.argsort.html

print("\nFor each of the 10 least-dense fish samples, show: (a) Fish density, (b) Water temperature, (c) Water depth")
least_dense = np.sort(fdensity_clean)[0:10]
is_in = np.isin(fdensity_clean, least_dense)
print("[fish density (fish/mi), water temp (C), water depth (ft)]")
summary = np.hstack([fdensity_clean[is_in].reshape(-1,1), wtemp_clean[is_in].reshape(-1,1), wdepth_clean[is_in].reshape(-1,1)])
print(summary[summary[:,0].argsort()]) # cite: https://docs.scipy.org/doc/numpy-1.15.1/reference/generated/numpy.argsort.html


