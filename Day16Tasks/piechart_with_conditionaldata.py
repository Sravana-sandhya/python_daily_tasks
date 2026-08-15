#Q8 : Pie Chart with Conditional Data 
# Scenario: 
# scores = np.array([40, 60, 80, 30, 90]) 
# Task: 
# ● Categorize into: 
# ○ Pass (>50) 
# ○ Fail (<=50) 
# ● Count using NumPy/Pandas 
# ● Plot pie chart for Pass vs Fail
import numpy as np
import matplotlib.pyplot as plt
scores = np.array([40, 60, 80, 30, 90]) 
pass_count = len(scores[scores > 50])
fail_count = len(scores[scores <= 50])
labels = ["pass","fail"]
counts = [pass_count,fail_count]
print("Pass:", pass_count)
print("Fail:", fail_count)
plt.pie(counts, labels = labels)
plt.title("Pass vs Fail")
plt.show()