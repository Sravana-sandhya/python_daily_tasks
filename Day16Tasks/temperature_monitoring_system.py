#Q4 : Temperature Monitoring System 
# Scenario: 
# temps = np.array([28, 30, 32, 35, 33, 31, 29]) 
# days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"] 
# Task: 
# ● Create DataFrame 
# ● Plot: 
# ○ Line graph → daily temperature trend 
# ○ Bar chart → day-wise temperature 
# ○ Pie chart → proportion of high (>30) vs low temps 
# ○ Histogram → temperature frequency 
# ○ Scatter plot → day index vs temperature
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt 
temps = np.array([28, 30, 32, 35, 33, 31, 29]) 
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
df = pd.DataFrame({"Days" : days,"Temps" : temps})
fig,ax = plt.subplots(2,3,figsize = (15,10))
# Line graph
ax[0, 0].plot(df["Days"], df["Temps"])
ax[0, 0].set_title("Daily Temperature Trend")
# Bar chart
ax[0, 1].bar(df["Days"], df["Temps"])
ax[0, 1].set_title("Day-wise Temps")
# Pie chart
high_count = len(temps[temps > 30])
low_count = len(temps[temps <= 30])
ax[0, 2].pie([high_count, low_count],labels=["High", "Low"])
ax[0, 2].set_title("High vs Low Temperature")
# Histogram
ax[1, 0].hist(df["Temps"])
ax[1, 0].set_title("Temperature Frequency")
# Scatter plot
ax[1, 1].scatter(df.index, df["Temps"])
ax[1, 1].set_title("Day Index vs Temperature")
plt.show()