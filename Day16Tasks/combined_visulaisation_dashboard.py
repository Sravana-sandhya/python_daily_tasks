#Q9 : Combined Visualization Dashboard 
# Scenario: 
# sales = np.array([100, 200, 150, 300]) 
# products = ["A", "B", "C", "D"] 
# Task: 
# ● Create DataFrame 
# ● Plot: 
# ○ Line graph (trend) 
# ○ Bar chart (comparison) 
# ○ Pie chart (distribution) 
# ● Show all in single figure (subplots)
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
sales = np.array([100, 200, 150, 300]) 
products = ["A", "B", "C", "D"] 
df = pd.DataFrame({"Products":products,"Sales":sales})
fig, ax = plt.subplots(1,3, figsize=(15, 5))
ax[0].plot(df["Products"], df["Sales"], marker="o")
ax[0].set_title("Sales Trend")
ax[0].set_xlabel("Product")
ax[0].set_ylabel("Sales")
ax[1].bar(df["Products"], df["Sales"])
ax[1].set_title("Sales Comparison")
ax[1].set_xlabel("Products")
ax[1].set_ylabel("Sales")
ax[2].pie(df["Sales"], labels=df["Products"])
ax[2].set_title("Sales Distribution")
plt.show()
