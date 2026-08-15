#Q2 : Monthly Sales Analysis 
# Scenario: 
# sales = np.array([100, 150, 200, 180, 220, 300]) 
# months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"] 
# Task: 
# ● Create DataFrame 
# ● Plot: 
# ○ Line graph → sales trend 
# ○ Bar chart → month-wise comparison 
# ○ Pie chart → contribution of each month 
# ○ Histogram → frequency of sales values 
# ○ Scatter plot → month index vs sales 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
sales = np.array([100, 150, 200, 180, 220, 300]) 
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
df = pd.DataFrame({"Month": months,"Sales": sales})
fig, ax = plt.subplots(2, 3, figsize=(15, 10))
# Line graph
ax[0, 0].plot(df["Month"], df["Sales"])
ax[0, 0].set_title("Sales Trend")
# Bar chart
ax[0, 1].bar(df["Month"], df["Sales"])
ax[0, 1].set_title("Month-wise comparison")
# Pie chart
ax[0, 2].pie(df["Sales"], labels=df["Month"])
ax[0, 2].set_title("contribution of each month")
# Histogram
ax[1, 0].hist(df["Sales"])
ax[1, 0].set_title("frequency of sales values")
# Scatter plot
ax[1, 1].scatter(df.index, df["Sales"])
ax[1, 1].set_title("Month Index vs Sales")
plt.show()

