# Problem 1: Titanic Data
import pandas as pd
df = pd.read_csv("titanic.csv")

print(len(df))
print(df.columns)
columnsWithMissingValues = df.columns[df.isnull().any()]
print(columnsWithMissingValues)

cleandf = df[['passClass','survived','sex','age']].copy()
cleandf.columns = ['class','survived','gender','age']
cleandf = cleandf.dropna()
print(len(cleandf))
numSurvived = cleandf['survived'].sum()
print(numSurvived)
numMale = cleandf['gender'].value_counts("male") * len(cleandf)
print(numMale)
numEachClass = cleandf['class'].value_counts()
print(numEachClass)
classOne = cleandf['class']

survived = cleandf.loc[cleandf['survived']==1]
didNotSurvive = cleandf.loc[cleandf['survived']==0]
survivedByClass = survived['class'].value_counts()
didNotSurviveByGender = didNotSurvive['gender'].value_counts()
didNotSurviveByAge = didNotSurvive.loc[didNotSurvive['age'].ge(18)]
adults = cleandf['age'].ge(18)
print(len(didNotSurviveByAge))
print(len(adults))
didNotSurviveByClass = didNotSurvive['class'].value_counts()
print(didNotSurviveByClass)
print(numEachClass)

adultMaleDied = didNotSurvive.loc[(didNotSurvive['gender']=='male') & (didNotSurvive['age'].ge(18))]
print(len(adultMaleDied))
male2nd3rdClassDied = didNotSurvive.loc[(didNotSurvive['gender']=='male') & ((didNotSurvive['class']==2) | (didNotSurvive['class']==3))]
print(len(male2nd3rdClassDied))
adults2nd3rdClassDied = didNotSurvive.loc[(didNotSurvive['age'].ge(18)) & ((didNotSurvive['class']==2) | (didNotSurvive['class']==3))]
print(len(adults2nd3rdClassDied))
adultMale2nd3rdClassDied = didNotSurvive.loc[(didNotSurvive['age'].ge(18)) & (didNotSurvive['gender']=='male') & 
                                             ((didNotSurvive['class']==2) | (didNotSurvive['class']==3))]
print(len(adultMale2nd3rdClassDied))
print(len(didNotSurvive))

adultss = cleandf['age'].ge(18).value_counts()
print(adultss)
secondThirdClass = cleandf.loc[(cleandf['class']==2) | (cleandf['class']==3)]
print(len(secondThirdClass))
maleAdult = cleandf.loc[(cleandf['age'].ge(18)) & (cleandf['gender']=='male')]
print(len(maleAdult))
adult2nd3rdClass = cleandf.loc[(cleandf['age'].ge(18)) & ((cleandf['class']==2) | (cleandf['class']==3))]
print(len(adult2nd3rdClass))
male2nd3rdClass = cleandf.loc[(cleandf['gender']=='male') & ((cleandf['class']==2) | (cleandf['class']==3))]
print(len(male2nd3rdClass))
adultMale2nd3rdClass = cleandf.loc[(cleandf['gender']=='male') & ((cleandf['class']==2) | (cleandf['class']==3)) & (cleandf['age'].ge(18))]
print(len(adultMale2nd3rdClass))

males = cleandf.loc[(cleandf['gender']=='male')]
malesSurvived = males.loc[(males['survived']==1)]
print(len(malesSurvived))
adults = cleandf.loc[(cleandf['age'].ge(18))]
adultsSurvived = adults.loc[(adults['survived']==1)]
print(len(adultsSurvived))
secondThirdClassSurvived = secondThirdClass.loc[(secondThirdClass['survived']==1)]
print(len(secondThirdClassSurvived))
print(len(males))


# Problem 2: Loan Default data
dataframe = pd.read_csv("loan_default.csv")

underThirtyEducationLoan = dataframe.loc[(dataframe['Age']<30) & (dataframe['LoanPurpose']=='Education')]
defaultsUnderThirdyEducationLoan = underThirtyEducationLoan['Default'].value_counts()
print(defaultsUnderThirdyEducationLoan/len(underThirtyEducationLoan)*100)

employedMarriedDependent = dataframe.loc[(dataframe['EmploymentType']!='Unemployed') & (dataframe['MaritalStatus']=='Married') & (dataframe['HasDependents']=='Yes')]
emdCosigner = employedMarriedDependent.loc[(employedMarriedDependent['HasCoSigner']=="Yes")]
print(emdCosigner['Default'].value_counts()/len(emdCosigner)*100)
emdBadCredit = employedMarriedDependent.loc[(employedMarriedDependent['CreditScore']<800)]
print(emdBadCredit['Default'].value_counts()/len(emdCosigner)*100)
emdPhD = employedMarriedDependent.loc[(employedMarriedDependent['Education'])=='PhD']
print(emdPhD['Default'].value_counts()/len(emdPhD)*100)
