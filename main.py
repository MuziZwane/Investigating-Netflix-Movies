# Importing pandas and matplotlib
import pandas as pd
import matplotlib.pyplot as plt

# Read in the Netflix CSV as a DataFrame
netflix_df = pd.read_csv("netflix_data.csv")

# Subset the DataFrame for type "Movie"
netflix_subset = netflix_df[netflix_df["type"] == "Movie"]

# Filter to keep only movies released in the 1990s
# Start by filtering out movies that were released before 1990
subset = netflix_subset[(netflix_subset["release_year"] >= 1990)]
# And then do the same to filter out movies released on or after 2000
movies_1990s = subset[(subset["release_year"] < 2000)]

# Visualize the duration column of your filtered data to see the distribution of movie durations
plt.hist(movies_1990s["duration"])
plt.title('Distribution of Movie Durations in the 1990s')
plt.xlabel('Duration (minutes)')
plt.ylabel('Number of Movies')
plt.show()

# Calculate the most frequent movie duration in the 1990s
duration = int(movies_1990s["duration"].mode().iloc[0])

# Filter the data again to keep only the Action movies
action_movies_1990s = movies_1990s[movies_1990s["genre"] == "Action"]

# Use a for loop and a counter to count how many short action movies there were in the 1990s
# Start the counter
short_movie_count = 0

# Iterate over the labels and rows of the DataFrame and check if the duration is less than 90
for label, row in action_movies_1990s.iterrows():
    if row["duration"] < 90:
        short_movie_count = short_movie_count + 1
    else:
        short_movie_count = short_movie_count

print(f"The most frequent movie duration in the 1990s: {duration} minutes")
print(f"Number of short action movies in the 1990s: {short_movie_count}")

# A quicker way of counting values in a column is to use .sum() on the desired column

short_movie_count = (action_movies_1990s["duration"] < 90).sum()
