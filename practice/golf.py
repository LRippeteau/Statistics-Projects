import pandas as pd
import scipy
df = pd.read_csv('Golf.csv')
df.describe()

print(scipy.stats.ttest_ind(df['Current'], df['New']))


