import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy


df = pd.read_csv("facebook_bidding_system_data.csv")
maxDf = df.loc[df["Bidding_System"]=="Maximum"]
avgDf = df.loc[df["Bidding_System"]=="Average"]

# description
print(df.describe())
print(maxDf.describe())
print(avgDf.describe())


# averages of each feature
numRecords = df["Bidding_System"].value_counts()
averageImpressions = df["Impression"].sum()/len(df)
averageClicks = df["Click"].sum()/len(df)
averagePurchase = df["Purchase"].sum()/len(df)
averageEarning = df["Earning"].sum()/len(df)
averageImpressionsMax = maxDf["Impression"].sum()/len(maxDf)
averageClicksMax = maxDf["Click"].sum()/len(maxDf)
averagePurchaseMax = maxDf["Purchase"].sum()/len(maxDf)
averageEarningMax = maxDf["Earning"].sum()/len(maxDf)
averageImpressionsAvg = avgDf["Impression"].sum()/len(avgDf)
averageClicksAvg = avgDf["Click"].sum()/len(avgDf)
averagePurchaseAvg = avgDf["Purchase"].sum()/len(avgDf)
averageEarningAvg = avgDf["Earning"].sum()/len(avgDf)

# bar chart of averages for features for avgDf
xAxisNames = ['Impressions', 'Clicks', 'Purchase', 'Earnings']
barValuesAvg = [averageImpressionsAvg, averageClicksAvg, averagePurchaseAvg, averageEarningAvg]
barValuesMax = [averageImpressionsMax, averageClicksMax, averagePurchaseMax, averageEarningMax]
xAxis = np.arange(len(xAxisNames))
plt.bar(xAxis - 0.2, barValuesAvg, 0.4, label='average bidding')
plt.bar(xAxis + 0.2, barValuesMax, 0.4, label='maximum bidding')
plt.xticks(xAxis,xAxisNames)
plt.xlabel('Features')
plt.ylabel('Average among bidding method')
plt.title("Averages of features for average and maximum bidding methods")
plt.legend()
plt.show()

# maximum and minimum of each feature
maxImpressionsAvg = avgDf['Impression'].max()
minImpressionsAvg = avgDf['Impression'].min()
maxImpressionsMax = maxDf['Impression'].max()
minImpressionsAvg = maxDf['Impression'].min()
maxClicksAvg = avgDf['Click'].max()
minClicksAvg = avgDf['Click'].min()
maxClicksMax = maxDf['Click'].max()
minClicksMax = maxDf['Click'].min()
maxPurhcaseAvg = avgDf['Purchase'].max()
minPurhcaseAvg = avgDf['Purchase'].min()
maxPurhcaseMax = maxDf['Purchase'].max()
minPurchaseMax = maxDf['Purchase'].min()
maxEarningAvg = avgDf['Earning'].max()
minEarningAvg = avgDf['Earning'].min()
maxEarningMax = maxDf['Earning'].max()
minEarningMax = maxDf['Earning'].min()

# plot of maximum and minimum of each feature
data1 = avgDf['Impression']
data2 = avgDf['Click']
data3 = avgDf['Purchase']
data4 = avgDf['Earning']

data1m = maxDf['Impression']
data2m = maxDf['Click']
data3m = maxDf['Purchase']
data4m = maxDf['Earning']
data = [data2, data2m, data3, data3m, data4, data4m]
xAxisNames = ['','Clicks (Avg)', 'Clicks (Max)', 'Purchase (Avg)', 'Purchase (Max)', 'Earnings(Avg)', 'Earnings (Max)']
xAxis = np.arange(len(xAxisNames))
# plt.boxplot(data)
# plt.xlabel('Features')
# plt.xticks(xAxis, xAxisNames, rotation=20)
# plt.title("Box-and-Whisker Plots of Features from Max and Avg Bidding Methods")
# plt.show()

# xAxisNames = ['','Impressions (Avg)', 'Impressions (Max)']
# xAxis = np.arange(len(xAxisNames))
# data = [data1, data1m]
# plt.boxplot(data)
# plt.xlabel('Features')
# plt.xticks(xAxis, xAxisNames)
# plt.title("Box-and-Whisker Plots of Impressions from Max and Avg Bidding Methods")
# plt.show()

# # histograms
# plt.hist(data1)
# plt.title("Impressions - Average Bidding Method")
# plt.show()
# plt.hist(data2)
# plt.title("Clicks - Average Bidding Method")
# plt.show()
# plt.hist(data3)
# plt.title("Purhcases - Average Bidding Method")
# plt.show()
# plt.hist(data4)
# plt.title("Earnings - Average Bidding Method")
# plt.show()
# plt.hist(data1m)
# plt.title("Impressions - Maximum Bidding Method")
# plt.show()
# plt.hist(data2m)
# plt.title("Clicks - Maximum Bidding Method")
# plt.show()
# plt.hist(data3m)
# plt.title("Purchases - Maximum Bidding Method")
# plt.show()
# plt.hist(data4m)
# plt.title("Earnings - Maximum Bidding Method")
# plt.show()


# pairplot
sns.pairplot(df, hue="Bidding_System")
plt.suptitle("Average Bidding System vs. Maximum Bidding System Pair Plot")
plt.show()



print(scipy.stats.ttest_ind(maxDf['Impression'], avgDf['Impression']))
print(scipy.stats.ttest_ind(maxDf['Click'], avgDf['Click']))
print(scipy.stats.ttest_ind(maxDf['Purchase'], avgDf['Purchase']))
print(scipy.stats.ttest_ind(maxDf['Earning'], avgDf['Earning']))


# t-tests
