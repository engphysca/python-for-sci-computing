# ==============================================================================
# Author: Eddie Guo
# Date: November 6, 2021
#
# Author's notes:
# You may share and modify (and do whatever you want) with this code.
# I hope this helps you with your assignments :)
#
# This script creates a linear regression model and plots the output.
# ==============================================================================

import matplotlib.pyplot as plt  # for plotting
import numpy as np               # for arrays
import pandas as pd              # for data manipulation

# Ordinary Least Squares (OLS): y = A + Bx
def Delta(x):
	# N \sum x^2 - \left( \sum x \right)^2
	return len(x) * np.sum(x**2) - np.sum(x)**2

def A(x, y):
	# A = \frac{(\sum x^2 \sum y - \sum x \sum xy)}{\Delta}
	return (np.sum(x**2)*np.sum(y)-np.sum(x)*np.sum(x*y)) / Delta(x)

def B(x, y):
	# B = \frac{N \sum xy - \sum x \sum y}{\Delta}
	return (len(x)*np.sum(x*y)-np.sum(x)*np.sum(y)) / Delta(x)


# Step 1. Read in the data.
df = pd.read_csv('cheese_and_deaths.csv')
print(df.head())

# Step 2. Visualize the data and verify a linear relationship.
plt.scatter(df['year'], df['deaths'])
plt.show()

# Step 3. Create the OLS model.
intercept = A(df['year'], df['deaths'])
slope = B(df['year'], df['deaths'])
# I love Python f-strings
# https://www.geeksforgeeks.org/formatted-string-literals-f-strings-python/
print(f'The slope is {slope} and the intercept is {intercept}.')

# Step 4. Re-visualize with your model.
x = np.linspace(2000, 2010, 10)  # 10 equally spaced points btw 2000 and 2010
y = slope*x + intercept
plt.scatter(df['year'], df['deaths'], color='black')
plt.plot(x, y, color='black')
plt.xlabel('Year')
plt.ylabel('Bedide tanglies (deaths)')
# Uncomment the line below to save the figure.
# plt.savefig('my_figs_name.png', dpi=250)
plt.show()


# Fun aside ====================================================================
# Question: What is the correlation between per capita cheese consumption and
# number of people who die by becoming tangled in their bedsheets?

# Answer: Let's visualize it!
intercept_cheese = A(df['year'], df['cheese_consumption'])
slope_cheese = B(df['year'], df['cheese_consumption'])
y1 = slope_cheese*x + intercept_cheese

fig, ax1 = plt.subplots()
ax2 = ax1.twinx()
ax1.plot(x, y, color='red')
ax2.plot(x, y1, color='black')

ax1.scatter(df['year'], df['deaths'], color='red')
ax2.scatter(df['year'], df['cheese_consumption'], color='black')

ax1.set_xlabel('Year')
ax1.set_ylabel('Besheet tanglies (deaths)', color='red')
ax2.set_ylabel('Cheese consumed (lbs)')
plt.tight_layout()
plt.show()

# Answer 2: r = 0.9471 (or 94.71%)
# Correlation != causation (or does it... haha)
