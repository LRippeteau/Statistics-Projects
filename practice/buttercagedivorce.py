import pandas as pd
import numpy as np

# Load the data as a dictionary (could also come from a CSV file or other)
data = {
    'B': [8.2, 7, 6.5, 5.3, 5.2, 4, 4.6, 4.5, 4.2, 3.7],
    'C': [2, 2, 3, 1, 1, 2, 3, 5, 1, 4],
    'D': [5, 4.7, 4.6, 4.4, 4.3, 4.1, 4.2, 4.2, 4.2, 4.1]
}

# Convert to a Pandas DataFrame
df = pd.DataFrame(data)

print(np.mean(df['D']))
print(np.std(df['C'],ddof=1))
print(np.cov(df['B'],df['C']))
print(np.corrcoef(df['B'],df['C']))
print(np.corrcoef(df['B'],df['D']))
print(np.corrcoef(df['C'],df['D']))