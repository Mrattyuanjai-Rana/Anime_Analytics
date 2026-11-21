import pandas as pd
import numpy as np

# Importing CSV dataset

raw_data = pd.read_csv("mal_anime.csv")


# Inspecting the dataset

print("First Five Rows : \n", raw_data.head())
print("\nStatistical Description : \n", raw_data.describe())
print("\nMissing Values : \n", raw_data.isnull().sum())
print("\nData Types : \n", raw_data.dtypes)

print("\nDuplicate Rows : \n", raw_data.duplicated().sum())
print("\nDuplicate ID's : \n", raw_data["myanimelist_id"].duplicated().sum())


# Keeping only desired fields and making a new csv file

desired_fields = raw_data[["title",
                   "Popularity",
                   "Favorites",
                   "Members",
                   "Type",
                   "Source",
                   "Genres",
                   "Ranked",
                   "Score",
                   "Demographic",
                   "Released_Year"]]

desired_fields.to_csv("desired_fields.csv", index=False)


# Importing and verifying the new csv file

data = pd.read_csv("desired_fields.csv")

print(data.info())


# Converting data into desired formats

data["Ranked"] = pd.to_numeric(data["Ranked"].str.replace("#", "", regex=False),
                                   errors="coerce")
data["Popularity"] = pd.to_numeric(data["Popularity"].str.replace("#", "", regex=False),
                                       errors="coerce")


data["Favorites"] = pd.to_numeric(data["Favorites"].str.replace(",", "", regex=False),
                                       errors="coerce")
data["Members"] = pd.to_numeric(data["Members"].str.replace(",", "", regex=False),
                                       errors="coerce")


# Checking data types

print("\nCorrected Datatypes : \n", data.dtypes)


# Substituting missing data in categorial fields

categorial_data = ["Type", "Demographic", "Source", "Genres"]
data[categorial_data] = data[categorial_data].fillna("Unknown")

print("\nMissing values after filling : \n", data.isnull().sum())


# Final checking of data

print("\nDimensions of Dataset : \n", data.shape)
print("\nData Types : \n", data.dtypes)
print("\nMissing Values : \n", data.isnull().sum())
print("\nStatistical Description : \n", data.describe())


# Exporting cleaned data

data.to_csv("cleaned_data.csv", index=False)

