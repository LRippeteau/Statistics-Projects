import pandas as pd
import scipy
df = pd.read_csv('paired.csv')

print(scipy.stats.ttest_ind(df['CORNFLK (mmol/L)'],df['OATBRAN (mmol/L)'],equal_var=False))

print(scipy.stats.ttest_rel(df['CORNFLK (mmol/L)'],df['OATBRAN (mmol/L)']))

