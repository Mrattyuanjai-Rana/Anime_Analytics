import pandas as pd

# Importing dataset ready for analysis

ready_data = pd.read_csv("ready_data.csv")
print("\nFirst Five Rows : \n", ready_data.head())


# General Overview

total_anime = len(ready_data)

print("\nTotal Number of Animes : \n", total_anime)
print("\nUnique Types : \n", ready_data["Type"].unique())
print("\nUnique Sources : \n", ready_data["Source"].unique())


# Rating Analysis

scores = ready_data["Score"].dropna()
print("\nMean Rating : \n", scores.mean())

lowest_score = scores.min()
lowest_anime = ready_data[ready_data["Score"]==lowest_score]
print("\nLowest Rated Anime : \n", lowest_anime)
print("\nGenres : \n", lowest_anime["Genres"])

highest_score = scores.max()
highest_anime = ready_data[ready_data["Score"]==highest_score]
print("\nHighest Rated Anime : \n", highest_anime)
print("\nGenres : \n", highest_anime["Genres"])

average_by_type = ready_data.groupby("Type")["Score"].mean()
average_by_type = average_by_type.sort_values(ascending=False)
print("\nAverage Rating by Type : \n", average_by_type)

average_by_source = ready_data.groupby("Source")["Score"].mean()
average_by_source = average_by_source.sort_values(ascending=False)
print("\nAverage Rating by Source : \n", average_by_source)


# Genre Analysis

ready_data["Genres"] = ready_data["Genres"].str.split(", ")
genre_data = ready_data.explode("Genres")

average_by_genre = genre_data.groupby("Genres")["Score"].mean()
average_by_genre = average_by_genre.sort_values(ascending=False)
print("\nAverage Rating by Genre : \n", average_by_genre)

anime_count_by_genre = genre_data.groupby("Genres").size()
print("\nAnime Count by Genre : \n", anime_count_by_genre)


# Popularity Analysis

top_5_members = ready_data.sort_values("Members", ascending=False).head(5)
top_5_favorites = ready_data.sort_values("Favorites", ascending=False).head(5)
top_5_popularity = ready_data.sort_values("Popularity", ascending=True).head(5)

print("\nTop 5 Most Popular Anime : \n", top_5_popularity[["title", "Popularity"]])
print("\nTop 5 Most Favorite Anime : \n", top_5_favorites[["title", "Favorites"]])
print("\nTop 5 Anime with Most Members: \n", top_5_members[["title", "Members"]])


# Comparative Analysis

rating_member_correlation = ready_data["Score"].corr(ready_data["Members"])
print("\nCorrelation Between Members and Ratings of an Anime : \n", rating_member_correlation)

rating_favorites_correlation = ready_data["Score"].corr(ready_data["Favorites"])
print("\nCorrelation Between Favorites and Ratings in Anime : \n", rating_favorites_correlation)

rating_popularity_correlation = ready_data["Score"].corr(ready_data["Popularity"])
print("\nCorrelation Between an Anime's Score and Popularity : \n", rating_popularity_correlation)
