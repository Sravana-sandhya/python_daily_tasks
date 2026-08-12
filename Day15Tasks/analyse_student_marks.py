# Q6 : Data Analysis Tool (NumPy + Pandas) 
# Scenario: 
# Analyze student marks. 
# Task: 
# ● Generate marks using NumPy 
# ● Convert into Pandas DataFrame 
# ● Use conditions to filter passing students 
# ● Calculate mean using math/NumPy 
# ● Use loop to print results
import numpy as np 
import pandas as pd 
marks = np.array([45,75,32,90,65])
df = pd.DataFrame({"Marks":marks})
passed = df[df["Marks"] >= 50]
average = np.mean(marks)
print("All Student Marks:")
print(df)
print("\nPassing Students:")
for mark in passed["Marks"]:
    print(mark)
print("\nAverage Marks:", average)


