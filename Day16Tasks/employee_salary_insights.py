#Q3 : Employee Salary Insights 
# Scenario: 
# salaries = np.array([25000, 30000, 28000, 40000, 50000, 35000]) 
# departments = ["HR", "IT", "HR", "IT", "Sales", "Sales"] 
# Task: 
# ● Convert into DataFrame 
# ● Plot: 
# ○ Line graph → salary trend 
# ○ Bar chart → department-wise salary comparison 
# ○ Pie chart → department distribution 
# ○ Histogram → salary distribution 
# ○ Scatter plot → index vs salary
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
salaries = np.array([25000, 30000, 28000, 40000, 50000, 35000])
departments = ["HR", "IT", "HR", "IT", "Sales", "Sales"]
df = pd.DataFrame({"Department": departments,"Salary": salaries})
fig, ax = plt.subplots(2, 3, figsize=(15, 10))
# Line graph
ax[0, 0].plot(df["Department"], df["Salary"])
ax[0, 0].set_title("Salary Trend")
# Bar chart
ax[0, 1].bar(df["Department"], df["Salary"])
ax[0, 1].set_title("Department-wise Salary Comparison")
# Pie chart
ax[0, 2].pie(df["Salary"], labels=df["Department"])
ax[0, 2].set_title("Department Distribution")
# Histogram
ax[1, 0].hist(df["Salary"])
ax[1, 0].set_title("Salary Distribution")
# Scatter plot
ax[1, 1].scatter(df.index, df["Salary"])
ax[1, 1].set_title("Index vs Salary")
plt.show()