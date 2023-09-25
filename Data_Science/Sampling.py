# Sampling with replacement using numpy
import numpy as np
import pandas as pd
import time

np.random.seed(3)
# a parameter: generate a list of unique random numbers (from 0 to 11)
# size parameter: how many samples we want (12)
# replace = True: sample with replacement
r_nums = np.random.choice(a=12, size=12, replace=True)
print("Sampling with replacement by numpy: ", r_nums)
# Using time
seed = int(time.time())
np.random.seed(seed)
r_nums_time = np.random.choice(a=12, size=12, replace=True)
print("Sampling with replacement by numpy using time: ", r_nums_time)

# Sampling with replacment using pandas
# Load dataset
url = 'https://raw.githubusercontent.com/mGalarnyk/Tutorial_Data/master/King_County/kingCountyHouseData.csv'
df = pd.read_csv(url)
# Selecting columns I am interested in
columns = ['bedrooms', 'bathrooms',
           'sqft_living', 'sqft_lot', 'floors', 'price']
df = df.loc[:, columns]
# Only want to use 15 rows of the dataset for illustrative purposes.
df = df.head(15)
# Notice how we have 3 rows with the index label 8
samples = df.sample(n=15, replace=True, random_state=2)
print("Sampling with replacement by pandas\n", samples)

# Sampling without Replacement
np.random.seed(3)
List_a = []
for i in range(1, 13):
    List_a.append(i)
# a parameter: generate a list of unique random numbers (from 0 to 11)
# size parameter: how many samples we want (12)
# replace = False: sample without replacement
# np.random.choice(List_a, size=12, replace=False)
r_nums_no = np.random.choice(a=12, size=12, replace=False)
print("Sampling without Replacement: ", r_nums_no)
