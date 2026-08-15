#Q1: Student Performance Dashboard 
# Scenario: 
# A school records marks of students in one subject: 
# marks = np.array([45, 67, 89, 56, 72, 91, 38]) 
# students = ["A", "B", "C", "D", "E", "F", "G"] 
# Task: 
# ● Convert to Pandas DataFrame 
# ● Plot: 
# ○ Line graph → trend of marks 
# ○ Bar chart → student vs marks 
# ○ Pie chart → Pass (>50) vs Fail 
# ○ Histogram → distribution of marks 
# ○ Scatter plot → index vs marks
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
marks = np.array([45, 67, 89, 56, 72, 91, 38]) 
students = ["A", "B", "C", "D", "E", "F", "G"] 
df = pd.DataFrame({"Students":students,"Marks" : marks})
fif, ax = plt.subplots(2, 3, figsize =(15,10))
#Line Graph
ax[0,0].plot(df["Students"],df["Marks"])
ax[0, 0].set_title("Trend Of Marks")
#Bar Char
ax[0, 1].bar(df["Students"], df["Marks"])
ax[0, 1].set_title("Student vs Marks")
#pie chart
pass_count = len(marks[marks > 50])
fail_count = len(marks[marks <= 50])
ax[0, 2].pie([pass_count, fail_count],labels=["Pass", "Fail"],)
ax[0, 2].set_title("Pass vs Fail")
#Histogram
ax[1, 0].hist(df["Marks"])
ax[1, 0].set_title("Marks Distribution")
ax[1, 0].set_xlabel("Marks")
ax[1, 0].set_ylabel("Frequency")
#Scatter Plot
ax[1, 1].scatter(df.index, df["Marks"])
ax[1, 1].set_title("Index vs Marks")
ax[1, 1].set_xlabel("Index")
ax[1, 1].set_ylabel("Marks")
plt.show()




