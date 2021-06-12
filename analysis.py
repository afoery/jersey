import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import numpy as np
import os

data_dir = "participant_data"
scores = []

# Get ratings from each participant file in the data directory
for filename in os.listdir(data_dir):
    if filename.endswith(".csv"):
        # Open the csv file and convert it to a numpy array
        df = pd.read_csv(os.path.join(data_dir, filename))
        ratings = df["slider.response"].to_numpy().astype(np.int64)[:-1]
        nums = df["Numbers"].to_numpy().astype(np.int64)[:-1]

        # Subtract the average ratings for the small numbers from the large numbers
        large_idxs = np.where(nums >= 50)
        small_idx = np.where(nums < 50)
        score = ratings[large_idxs].mean() - ratings[small_idx].mean()
        scores.append(score)

# Perform t-test
ttest = stats.ttest_rel(scores, np.zeros(len(scores)))
print(ttest)

# Plot the difference score for each participant
plt.bar(np.arange(len(scores)), scores)
plt.show()
