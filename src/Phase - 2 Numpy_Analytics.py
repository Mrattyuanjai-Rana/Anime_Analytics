import numpy as np
import pandas as pd

# Importing and verifying the clean dataset

clean_data = pd.read_csv("cleaned_data.csv")

print("\nFirst Five Rows : \n", clean_data.head())


# Extracting the "Score" field and analysing
# NOTE - We are using nan aware functions so that our operations ignore missing values

score = clean_data["Score"].to_numpy()

print("\nScore Mean : \n", np.nanmean(score))
print("\nScore Median : \n", np.nanmedian(score))
print("\nScore Standard Deviation : \n", np.nanstd(score))
print("\nScore Minimum Value : \n", np.nanmin(score))
print("\nScore Maximum Value : \n", np.nanmax(score))
print("\n25th and 75th Percentiles : \n", np.nanquantile(score, [0.25, 0.75]))


# Reducing numeric data into simpler values

score_categories = np.select([score>7.16, score>5.94, np.isnan(score)],
                      ["High", "Medium", "Unknown"], default="Low")

print("\nReduced Array : \n", score_categories)


# Adding score category field to original file and creating new csv file

clean_data["score_category"] = score_categories

clean_data.to_csv("ready_data.csv", index=False)
