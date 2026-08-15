#Q5 : Product Sales & Profit Analysis 
# Scenario: 
# sales = np.array([200, 300, 250, 400, 350]) 
# profit = np.array([50, 70, 60, 90, 80]) 
# products = ["A", "B", "C", "D", "E"] 
# Task: 
# ● Create DataFrame 
# ● Plot: 
# ○ Line graph → sales trend 
# ○ Bar chart → product vs sales 
# ○ Pie chart → sales contribution 
# ○ Histogram → profit distribution 
# ○ Scatter plot → sales vs profit
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
sales = np.array([200, 300, 250, 400, 350]) 
profit = np.array([50, 70, 60, 90, 80]) 
products = ["A", "B", "C", "D", "E"] 
df = pd.DataFrame({"Product": products,"Sales": sales,"Profit": profit})
fig, ax = plt.subplots(2, 3, figsize=(15, 10))
# Line graph
ax[0, 0].plot(df["Product"], df["Sales"])
ax[0, 0].set_title("Sales Trend")
# Bar chart
ax[0, 1].bar(df["Product"], df["Sales"])
ax[0, 1].set_title("Product vs Sales")
# Pie chart
ax[0, 2].pie(df["Sales"], labels=df["Product"])
ax[0, 2].set_title("Sales Contribution")
# Histogram
ax[1, 0].hist(df["Profit"])
ax[1, 0].set_title("Profit Distribution")
# Scatter plot
ax[1, 1].scatter(df["Sales"], df["Profit"])
ax[1, 1].set_title("Sales vs Profit")
plt.tight_layout()
plt.show()
