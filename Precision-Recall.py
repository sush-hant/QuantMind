import pandas as pd
import numpy as np

# Set random seed for reproducibility
np.random.seed(42)

# Initialize an empty list to store rows
rows = []

for _ in range(50):
    row = [0, 0, 0]  # Start with all zeros
    idx = np.random.choice([0, 1, 2])  # Randomly choose one column to set to 1
    row[idx] = 1
    rows.append(row)

# Create DataFrame
df = pd.DataFrame(rows, columns=['true_positive', 'false_positive', 'false_negative'])

print(df)

#Write a code to calculate precision


#Write a code to calculate recall


#Write a code to calculate F1-score
