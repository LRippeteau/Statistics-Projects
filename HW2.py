
# problem 2
import pandas as pd;

df = pd.read_csv('data/framingham.csv')
# print(df.head())
# print(len(df))
# print(df.columns)
# print(df.dtypes)

print(df.isna())
newdf = df.dropna()
print(newdf)

import numpy as npy
import seaborn as sns

males = newdf["male"].value_counts()[1]
totalpeople = newdf["male"].count()
print(males / totalpeople * 100)
nonmales = newdf["male"].value_counts()[0]
print(nonmales / totalpeople * 100)
tfcholabove300 = newdf["totChol"].ge(300)
cholabove300 = tfcholabove300.value_counts("True") * 100
print(cholabove300)

import matplotlib.pyplot as plt
newdf.hist(column="diaBP", bins=20)
plt.title("Histogram of diaBP")
plt.xlabel("diaBP")
plt.ylabel("Number participants")

plt.show()

newdf.hist(column="sysBP", bins=20)
plt.title("Histogram of sysBP")
plt.xlabel("sysBP")
plt.ylabel("Number participants")

plt.show()
diaBPmean = newdf["diaBP"].mean()
sysBPmean = newdf["sysBP"].mean()
diaBPmedian = newdf["diaBP"].median()
sysBPmedian = newdf["sysBP"].median()

print("DiaBP mean: " + str(diaBPmean))
print("sysBP mean: " + str(sysBPmean))
print("diaBP median: " + str(diaBPmedian))
print("sysBP median: " + str(sysBPmedian))


sns.boxplot(data=newdf,x=newdf["TenYearCHD"],y=newdf["totChol"])
plt.show()

sns.scatterplot(data=newdf, x=newdf["education"], y=newdf["cigsPerDay"])
plt.title("education vs. cigs per day")
plt.show()





# problem 3
dataframe = pd.read_csv('data/NBA22-23.csv')
print(dataframe.head())
dataframe["Field Goal Percentage"] = dataframe["FG"]/dataframe["FGA"] * 100
print(dataframe.head())
dfmean = dataframe["MP"].mean()
print(dfmean)
dfpointsscored = dataframe["PTS"].mean()
print(dfpointsscored)
dffieldgoalsshot = dataframe["FGA"].mean()
dffieldgoalsmade = dataframe["FG"].mean()
fieldgoalpercentage = dffieldgoalsmade / dffieldgoalsshot * 100
print(fieldgoalpercentage)
avgminutes = dataframe["MP"].mean()

meanage = dataframe["Age"].mean()

youngplayerspartone = dataframe[(dataframe["Age"] < meanage) & 
                                     ((dataframe["FG"]/dataframe["FGA"])> (fieldgoalpercentage / 100)) & 
                                     (dataframe["MP"] > avgminutes)]
youngplayerspartonelength = len(youngplayerspartone)
print(youngplayerspartonelength)

youngplayerspartonetwo = youngplayerspartone.sort_values(by="Field Goal Percentage",ascending=False)
print(youngplayerspartonetwo.head())

youngplayersparttwo = dataframe[(dataframe["Age"] < meanage) & 
                                     ((dataframe["PTS"])> dfpointsscored) & 
                                     (dataframe["MP"] > avgminutes)]
youngplayersparttwolength = len(youngplayersparttwo)
print(youngplayersparttwolength)

youngplayersparttwotwo = youngplayerspartone.sort_values(by="PTS",ascending=False)
print(youngplayersparttwotwo.head())

