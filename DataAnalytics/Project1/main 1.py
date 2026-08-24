import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np

# Scenario 1: Basic Data Loading & Cleaning
df = pd.read_csv("railway_gauges.csv")
print("First 5 rows:")
print(df.head()) # print rows
print("\nColumn names:")
print(df.columns) # print columns
print(df.isnull().sum()) # to find missing values
df = df.fillna(0) # replace missing value with 0
gauge_columns = ["Broad Gauge","Metre Gauge","Narrow Gauge","Total"]
df[gauge_columns] = df[gauge_columns].apply(pd.to_numeric) # change to numeric value
print(df.dtypes)

#Scenario 2: Simple Visualization 
year_total = df[["Year","Total"]]
print(year_total)
plt.plot(year_total["Year"],year_total["Total"])# Create a line graph
plt.title("Total Railway Tracks Over Years")
plt.xlabel("Years")
plt.ylabel("Total Tracks")
plt.xticks(rotation = 50)# Rotate year labels for clear visibility
plt.savefig("graphs/railway_growth.png")# Save the graph as an image
plt.show()
if year_total["Total"].iloc[-1] > year_total["Total"].iloc[0]:
    print("Trend :Increasing")
elif year_total["Total"].iloc[-1] > year_total["Total"].iloc[0]:
    print("Trend : Decreasing")# Print if final value is greater than first value
else:
    print("Trend : No change")# Print if both values are equal

#Scenario 3: Filtering + Bar Chart
df["Start Year"] = df["Year"].str[:4].astype(int)# Extract starting year and convert it to integer
recent_data = df[df["Start Year"] > 2000] # Filter only years after 2000
gauge_columns = ["Broad Gauge", "Metre Gauge", "Narrow Gauge"]# Select the three gauge columns
recent_data.plot(x = "Start Year",y = gauge_columns, kind = "bar",figsize = (10,6)) #Create grouped bar chart
plt.title("Railway Gauge Comparison After 2000")
plt.xlabel("Year")
plt.ylabel("Track Length")
plt.legend()# Display gauge names
plt.savefig("graphs/guage_comparision_after_2000years.png")# Save graph as an image
plt.show()
gauge_totals = recent_data[gauge_columns].sum()# Calculate total of each gauge after 2000
print("Total for each gauge:", gauge_totals)
print("Dominant Gauge:", gauge_totals.idxmax())# Find and display the gauge with the highest total

#Scenario 4: Feature Engineering + Pie Chart 
gauge_totals = df[["Broad Gauge", "Metre Gauge", "Narrow Gauge"]].sum()
print(gauge_totals)
plt.pie(gauge_totals,labels = gauge_totals.index,autopct="%1.1f%%")# Create pie chart with gauge names and percentages
plt.title("Contribution of Each Railway Gauge")
plt.savefig("graphs/gauge_type_contribution")# Save graph as an image
plt.show()
print("Gauge with highest contribution:", gauge_totals.idxmax())

#Scenario 5: Advanced Analysis + Multiple Graphs
#You are asked to perform a complete analysis of railway trends.
# 1. Create Start Year
df["Start Year"] = df["Year"].str[:4].astype(int)
df["% Broad Gauge"] = (df["Broad Gauge"] / df["Total"]) * 100  # Calculate Broad Gauge percentage
df["% Metre Gauge"] = (df["Metre Gauge"] / df["Total"]) * 100  # Calculate Metre Gauge percentage
df["% Narrow Gauge"] = (df["Narrow Gauge"] / df["Total"]) * 100 # Calculate Narrow Gauge percentage
# 2. Calculate yearly growth using NumPy
growth = np.diff(df["Total"])  # Calculate change in Total tracks between years
print(growth)
# 3. Line graph for all gauges
plt.plot(df["Start Year"], df["Broad Gauge"], label="Broad Gauge")# Plot Broad Gauge
plt.plot(df["Start Year"], df["Metre Gauge"], label="Metre Gauge")# Plot Metre  Gauge
plt.plot(df["Start Year"], df["Narrow Gauge"], label="Narrow Gauge")# Plot Narrow Gauge
plt.title("Railway Gauge Trends")
plt.xlabel("Year")
plt.ylabel("Track Length")
plt.legend()
plt.savefig("graphs/railway_gauge_trends.png")# Save graph as an image
plt.show()
# Stacked bar chart
plt.bar(df["Start Year"], df["Broad Gauge"], label="Broad Gauge")  # Plot Broad Gauge bars
plt.bar(df["Start Year"], df["Metre Gauge"],bottom=df["Broad Gauge"], label="Metre Gauge") # Add Metre Gauge on top of Broad Gauge
plt.bar(df["Start Year"], df["Narrow Gauge"],bottom=df["Broad Gauge"] + df["Metre Gauge"],label="Narrow Gauge")
plt.title("Railway Gauge Composition")
plt.xlabel("Year")
plt.ylabel("Track Length")
plt.legend()
plt.savefig("graphs/all_gauges.png")# Save graph as an image
plt.show()
# 4. Year with highest growth
for gauge in["Broad Gauge", "Metre Gauge", "Narrow Gauge"]:
    decline = df[gauge].diff() < 0
    if decline.any():
        print(gauge, "has a decline")
    else:
        print(gauge, "has no decline")
    
# 5. Final conclusion
if df["% Broad Gauge"].iloc[-1] > df["% Broad Gauge"].iloc[0]:
    print("Conclusion: The railway system is shifting towards Broad Gauge.")
else:
    print("Conclusion: The railway system is not shifting towards Broad Gauge.")
