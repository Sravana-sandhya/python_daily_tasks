#Q4 : Student Marks DataFrame Analysis 
# A DataFrame: 
# data = pd.DataFrame({ 
# "Name": ["A", "B", "C"], 
# "Math": [80, 70, 60], 
# "Science": [90, 60, 70] 
# }) 
# Task: 
# ● Add a new column Total = Math + Science 
# ● Find the student with the highest total marks
import pandas as pd
data = pd.DataFrame({ "Name": ["A", "B", "C"], "Math": [80, 70, 60], "Science": [90, 60, 70] }) 
data["Total"] = data["Math"] + data["Science"]
highest = data["Total"].max()
print(data)
print(data[data["Total"] == highest])