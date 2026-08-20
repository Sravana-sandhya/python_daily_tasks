import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

#SCENARIO 1: Data Loading & Preprocessing
data = pd.read_csv("ign.csv")
print("Displaying first five rows:") #Display first 5 rows
print(data.head())
print("Display the last 5 rows:")#Display last 5 rows
print(data.tail())
print(data.shape) # shape of the data set
print("Removed the column unnamed!!")
data.drop(columns=['Unnamed: 0'], inplace=True, errors='ignore')
print("Removed the column Unnamed: 0")
missing_values = data[['score', 'genre', 'platform']].isnull().sum() # Check missing values in score, genre, and platform columns
print("\nMissing Values:")
print(missing_values)
data["score"] = pd.to_numeric(data["score"], errors="coerce") # Convert score column to numeric
data["score"] = data["score"].fillna(data["score"].mean())
data["genre"] = data["genre"].fillna(data["genre"].mode()[0])
data["platform"] = data["platform"].fillna(data["platform"].mode()[0])
# Convert release date columns to integer
data["release_year"] = data["release_year"].astype(int)
data["release_month"] = data["release_month"].astype(int)
data["release_day"] = data["release_day"].astype(int)
print("\nData types:")
print(data.dtypes)
print("\nMissing values after cleaning:")# Check missing values after cleaning
print(data[["score", "genre", "platform"]].isnull().sum())

#SCENARIO 2: Line Graph (Score Trend) + Save
grouped_year = data.groupby("release_year")["score"].mean() #Calculating average score per year using pandas
print(grouped_year)
years = np.array(grouped_year.index) #converting into numpy arrays
average_scores = np.array(grouped_year.values)
plt.figure()# plot line graph
plt.plot(years,average_scores,marker = 'o')
plt.title("Average Game Score Over Years")
plt.xlabel("release_year")
plt.ylabel("average_score")
plt.tight_layout() #adjust the spacing in a Matplotlib graph.
plt.savefig("graphs/avg_score_trend.png")
plt.show()

#Scenario 3: Filtering + Bar Chart + Save
filtered_data =data[data["score"] > 7] #filtering data score >7
top_rated_games = filtered_data.groupby("platform")['title'].count() #count number of high rated games
print(top_rated_games)
top_10 = top_rated_games.sort_values(ascending=False).head(10)
print(top_10)
platforms = np.array(top_10.index) #convert to numpy arrays
counts = np.array(top_10.values)
print(platforms)
print(counts)
plt.figure() #plotting bar chart
plt.bar(platforms,counts)
plt.title("Top 10 Platforms by High-Rated Games")
plt.xlabel("Platform")
plt.ylabel("Number of Games")
plt.xticks(rotation = 45) #rotate xaxis
plt.tight_layout() #adjust the spacing in a Matplotlib graph.
plt.savefig("graphs/top_platforms_bar.png")
plt.show()

#SCENARIO 4: Aggregation + Pie Chart + Save
genre_counts = data['genre'].value_counts() #counting number of genre
print("The number of games per genre are:")
print(genre_counts)
top_5 = genre_counts.head(5) # Select top 5 genres
print(top_5)
genres = top_5.index.to_numpy() #prepare labels and values
counts = top_5.values
plt.figure() #plot pie chart
plt.pie(counts, labels=genres, autopct='%1.1f%%')
plt.title("Genre Distribution")
plt.tight_layout()
plt.savefig("graphs/genre_distribution.png")
plt.show()

#SCENARIO 5: Advanced Analysis + Multiple Graphs
#Part 1 : Feature Engineering
data["score_category"] = np.where(data["score"] > 9, "Excellent", np.where(data["score"] >= 7, "Good","Average")) #Create score_category column
data["editors_choice"] = data["editors_choice"].map({"Y": 1,"N": 0}) #Convert editors_choice column (Y → 1, N → 0)
#part2 : Numpy Analysis
yearly_avg_score = data.groupby("release_year")["score"].mean()
years = np.array(yearly_avg_score.index)
average_scores = np.array(yearly_avg_score.values)
yearly_growth = np.diff(average_scores) #calculate yearly growth
print(yearly_growth)
#Part3 : Visualisation
#1. line graph(score trend)
plt.figure() #line grapg(score trend)
plt.plot(years, yearly_avg_score, marker='o')
plt.title("Average Score Trend Over Years")
plt.xlabel("Release Year")
plt.ylabel("Average Score")
plt.tight_layout()
plt.savefig("graphs/score_trend.png")
plt.show()

#2. Stacked Graph(store category per year)
category_counts = data.pivot_table(index='release_year',columns='score_category',aggfunc='size',fill_value=0)
category_counts.plot(kind = "bar", stacked = True)
plt.title("Score Category Distribution per Year")
plt.xlabel("Release Year")
plt.ylabel("Number of Games")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("graphs/score_category_stacked.png")
plt.show()

#3 . Histogram(score Distrubution)
plt.figure()
plt.hist(data["score"], bins=20)
plt.title("Score Distribution")
plt.xlabel("Score")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("graphs/score_distribution.png")
plt.show()

#part5 : Insights # Year with highest average score
max_year = yearly_avg_score.idxmax()
max_score = yearly_avg_score.max()
print(f"Year with highest average score: {max_year} ({max_score:.2f})")
# Check whether high scores increased over time
first_year_score = average_scores[0]
last_year_score = average_scores[-1]
if last_year_score > first_year_score:
    print("High scores increased over time.")
else:
    print("High scores did not increase over time.")
# Check editors_choice correlation with high scores
high_score = data[data["score"] >= 7]
editor_choice_average = high_score["editors_choice"].mean()
print("Editors choice average for high-rated games:",
      editor_choice_average)