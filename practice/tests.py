import scipy
import pandas as pd

set_a = [4, 7, 9, 12, 15, 18, 21, 24, 27, 30]
set_b = [2, 5, 10, 16, 19, 22, 25, 28, 31, 33]

df = pd.DataFrame({'Set A': set_a, 'Set B': set_b})

print(scipy.stats.shapiro(set_a))
print(scipy.stats.shapiro(set_b))

print(scipy.stats.ttest_ind(set_a,set_b))

print(scipy.stats.ttest_rel(set_a,set_b))

print(scipy.stats.mannwhitneyu(set_a,set_b))

print(scipy.stats.wilcoxon(set_a,set_b))

set_c = [1, 3, 6, 8, 11, 14, 17, 20, 23, 26]
print(scipy.stats.f_oneway(set_a,set_b,set_c))