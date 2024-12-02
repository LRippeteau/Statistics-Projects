# HW4
# Problem 1: Iris Data

import pandas as pd
df = pd.read_csv("AggregatedIrisData.csv")

# PDF and CDF for petal_width
petalWidthValueCounts = df['petal_width'].value_counts().sort_index()
print(petalWidthValueCounts)
petalWidthValueProbabilities = petalWidthValueCounts / len(df)
print(petalWidthValueProbabilities)
petalWidthValues = petalWidthValueProbabilities.keys()
petalWidthProbabilities = petalWidthValueProbabilities.tolist()
dictionaryPetalWidthProbabilities = dict(zip(petalWidthValues,petalWidthProbabilities))
print(dictionaryPetalWidthProbabilities)


import numpy as npy
import seaborn as sns
import matplotlib.pyplot as plt

xAxis = dictionaryPetalWidthProbabilities.keys()
xAxis = [str(x) for x in xAxis]
yAxis = dictionaryPetalWidthProbabilities.values()

dictionaryPetalWidthCumProbs = dictionaryPetalWidthProbabilities.copy()
for petalWidth in dictionaryPetalWidthProbabilities:
    cumulativeProbCurrent = dictionaryPetalWidthProbabilities[petalWidth]
    for petalWidth2 in dictionaryPetalWidthProbabilities:
        if petalWidth2 < petalWidth:
            cumulativeProbCurrent = cumulativeProbCurrent + dictionaryPetalWidthProbabilities[petalWidth2]
            print(cumulativeProbCurrent)
    dictionaryPetalWidthCumProbs[petalWidth] = cumulativeProbCurrent

print(dictionaryPetalWidthProbabilities)
print(dictionaryPetalWidthCumProbs)

# PDF
plt.bar(xAxis,yAxis,color='green')
plt.xlabel("Petal Widths")
plt.ylabel("Probability")
plt.title("PDF of Petal Widths")
plt.show()

# CDF

values = dictionaryPetalWidthCumProbs.keys()
cumulativeDistributions = dictionaryPetalWidthCumProbs.values()

plt.plot(values,cumulativeDistributions)
plt.xlabel("Petal Widths")
plt.ylabel("Cumulative Distribution Probabilities")
plt.title("CDF of petal Widths")
plt.show()


# PDF and CDF for sepal_width
sepalWidthValueCounts = df['sepal_width'].value_counts().sort_index()
print(sepalWidthValueCounts)
sepalWidthValueProbabilities = sepalWidthValueCounts / len(df)
print(sepalWidthValueProbabilities)
sepalWidthValues = petalWidthValueProbabilities.keys()
sepalWidthProbabilities = sepalWidthValueProbabilities.tolist()
dictionarySepalWidthProbabilities = dict(zip(sepalWidthValues,sepalWidthProbabilities))
print(dictionarySepalWidthProbabilities)

xAxis = dictionarySepalWidthProbabilities.keys()
xAxis = [str(x) for x in xAxis]
yAxis = dictionarySepalWidthProbabilities.values()

# PDF
plt.bar(xAxis,yAxis,color='green')
plt.xlabel("Sepal Widths")
plt.ylabel("Probability")
plt.title("PDF of Sepal Widths")
plt.show()

dictionarySepalWidthCumProbs = dictionarySepalWidthProbabilities.copy()
for sepalWidth in dictionarySepalWidthProbabilities:
    cumulativeProbCurrent = dictionarySepalWidthProbabilities[sepalWidth]
    for sepalWidth2 in dictionarySepalWidthProbabilities:
        if sepalWidth2 < sepalWidth:
            cumulativeProbCurrent = cumulativeProbCurrent + dictionarySepalWidthProbabilities[sepalWidth2]
            print(cumulativeProbCurrent)
    dictionarySepalWidthCumProbs[sepalWidth] = cumulativeProbCurrent

print(dictionarySepalWidthProbabilities)
print(dictionarySepalWidthCumProbs)

# CDF

values = dictionarySepalWidthCumProbs.keys()
cumulativeDistributions = dictionarySepalWidthCumProbs.values()

plt.plot(values,cumulativeDistributions)
plt.xlabel("Sepal Widths")
plt.ylabel("Cumulative Distribution Probabilities")
plt.title("CDF of Sepal Widths")
plt.show()


# Problem 2: Sampling Distribution
import numpy as np

def meanOfSample(sampleSize):
    sampleSet = np.random.exponential(1/4,sampleSize)
    mean = np.mean(sampleSet)
    return mean

def histogramSampleMean(sampleSize,numSampleSets):
    means = [meanOfSample(sampleSize) for i in range(numSampleSets)]
    plt.hist(means,density=True,bins=30)
    plt.title(label = 'Mean from ' + str(sampleSize) + ' samples, across ' + str(numSampleSets) + ' sets')
    plt.show()

numSampleSets = 10000
for sampleSize in [1, 5, 25, 50]:
    histogramSampleMean(sampleSize,numSampleSets)

