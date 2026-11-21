# Anime Data Analytics using Python

## Project Overview
This project explores an anime dataset using Python. It focuses on preparing the data and performing numerical and exploratory analysis to discover patterns in anime ratings, genres, popularity, and audience engagement.

## Project Modules
1. **Data Cleaning using Pandas** — prepares the dataset for analysis by handling missing values, selecting relevant columns, and organizing the data.
2. **NumPy Analysis** — performs numerical exploration of the Score field using NumPy operations such as statistical summaries and array-based calculations.
3. **Pandas Analysis** — explores the dataset through summaries, grouping, sorting, and comparisons.

## Analyses
- Dataset overview and unique-value counts
- Score statistics, including mean, median, quantiles, minimum, and maximum
- Average score by anime type and source
- Genre analysis using string splitting and `explode()`
- Anime counts and average scores by genre
- Top anime by popularity rank, members, and favorites
- Correlation between score and members, favorites, and popularity rank

## Key Insights
- Average rating - 6.53962661591968
- Standard deviation of ratings - 0.8661455927858746
- Top anime in terms of (in decreasing order of statistical values):
   Popularity - Shingeki No Kyojin, Death Note, Fullmetal Alchemist: Brotherhood, One Punch Man, Kimetsu No Yaiba
   Membership - Shingeki No Kyojin, Death Note, Fullmetal Alchemist: Brotherhood, One Punch Man, Kimetsu No Yaiba
   Favorites - One Piece, Fullmetal Alchemist: Brotherhood, Hunter x Hunter (2011), Steins; Gate, Shingeki No Kyojin
- Top rated genres (in decreasing order of statistical values) - Award Winning, Suspense, Mystery, Drama, Romance
- Correlations between:
   Membership amd Ratings - Moderately Positive Relation (0.39341092521684967)
   Popularity Ranking and Ratings - Strong Negative Relation ( -0.6545929334869383)
   Favorites and Ratings - Weak Positive Realtion (0.2419651150799461)

## Technologies Used
- Python 3.14.4
- Pandas
- NumPy

## Requirements
- Python
- Pandas
- NumPy

## How to Run
1. Clone or download this repository.
2. Place the dataset in the location expected by the scripts, or update the dataset path in the code.
3. Run the modules in the intended order:
   - Phase_1_Data_Cleaning,py
   - Phase_2_Numpy_Analysis.py
   - Phase_3_Pandas_Analysis.py

Example:

```bash
python Phase_1_Data_Cleaning.py
python Phase_2_Numpy_Analysis.py
python Phase_3_Pandas_Analysis.py
```

## Dataset
Datasets used in this project:
- mal_anime.csv (original dataset, link - https://www.kaggle.com/datasets/syahrulapriansyah2/myanimelist-2025)
- desired_fields.csv
- cleaned_data.csv
- ready_data.csv

## Notes
Correlation values describe associations between variables; they do not establish causation. Popularity rank is inversely oriented: a smaller rank number indicates greater popularity.

## Future Improvements
- Add visualizations if suitable tools/resources become available.
- Expand the analysis with additional dataset fields.
- Improve handling and documentation of missing or inconsistent values.

## Author
- Mrattyuanjai Rana
- BTech CSE Student