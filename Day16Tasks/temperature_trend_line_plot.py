#Q4 : Temperature Trend Line Plot 
# Scenario: 
# Daily temperatures: 
# temps = np.array([28, 30, 32, 31, 29]) 
# Task: 
# ● Convert into Pandas Series 
# ● Plot a line graph 
# ● Add title and grid
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
temps = np.array([28, 30, 32, 31, 29])
temperature = pd.Series(temps)
print(temperature)
plt.plot(temperature)
plt.title("Daily Temperature")
plt.grid()
plt.show()

