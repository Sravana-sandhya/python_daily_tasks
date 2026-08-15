# Q10: Data Cleaning + Visualization 
# Scenario: 
# data = np.array([100, np.nan, 200, 150, np.nan, 300]) 
# Task: 
# 1. Convert to Pandas Series 
# 2. Replace NaN with mean 
# 3. Plot: 
# ○ Line graph of cleaned data 
# ○ Bar chart of values > average
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
data = np.array([100, np.nan, 200, 150, np.nan, 300])
series = pd.Series(data)
mean = series.mean() 
s = series.fillna(mean)
plt.plot(s)
plt.title("Cleaned Data")
plt.show()
average = s.mean()
filtered = s[s > average]
plt.bar(filtered.index, filtered.values)
plt.title("Values Greater Than Average")
plt.xlabel("Index")
plt.ylabel("Value")
plt.show()
