# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 20:48:08 2022

@author: MANAS
"""

import numpy as np
import pandas as pd

def getNumber(s):
    if s=="male":
        return 1
    else:
        return 2
    
titanic = pd.read_csv(r'C:\Users\MANAS\Desktop\Mission DS\Shared Files\7th,8th\TASK-13\DATASET/train.csv', header = 0, dtype={'Age': np.float64})
titanic.tail()

titanic.describe()

del titanic["Name"]
titanic.head()

del titanic["Ticket"]
titanic.head()

del titanic["Fare"]
titanic.head()

del titanic['Cabin']
titanic.head()



titanic["Gender"]=titanic["Sex"].apply(getNumber)
#We have created a new column called "Gender" and 
#filling it with values 1,2 based on the values of sex column
titanic.head()

# Deleting Sex column, since no use of it now
del titanic["Sex"]
titanic.head()
titanic.isnull().sum()

meanS = titanic[titanic.Survived == 1].Age.mean()
meanS

titanic["age"]=np.where(pd.isnull(titanic.Age) & titanic["Survived"]==1,meanS, titanic["Age"])
titanic.head()
titanic.isnull().sum()

# Finding the mean age of " Not Survived " People
meaNS = titanic[titanic.Survived==0].Age.mean()
meaNS

titanic.age.fillna(meaNS,inplace=True)
titanic.head()
titanic.isnull().sum()

del titanic['Age']
titanic.head()

# Finding the no. of people that survived
# given that they've embarked or boarded from a particular port
survivedQ = titanic[titanic.Embarked == 'Q'][titanic.Survived ==1].shape[0]
survivedC = titanic[titanic.Embarked == 'C'][titanic.Survived ==1].shape[0]
survivedS = titanic[titanic.Embarked == 'S'][titanic.Survived ==1].shape[0]
print(survivedQ)
print(survivedC)
print(survivedS)

survivedQ = titanic[titanic.Embarked == 'Q'][titanic.Survived == 0].shape[0]
survivedC = titanic[titanic.Embarked == 'C'][titanic.Survived == 0].shape[0]
survivedS = titanic[titanic.Embarked == 'S'][titanic.Survived == 0].shape[0]
print(survivedQ)
print(survivedC)
print(survivedS)

titanic.dropna(inplace=True)
titanic.head()
titanic.isnull().sum()

# Renaming "age" & "gender" columns
titanic.rename(columns={'age':'Age'}, inplace=True)
titanic.head()

titanic.rename(columns={'Gender':'Sex'}, inplace=True)
titanic.head()

def getEmb(str):
    if str=="S":
        return 1
    elif str=="Q":
        return 2
    else:
        return 3
    titanic["Embark"]=titanic["Embarked"].apply(getEmb)
    titanic.head()

del titanic['Embarked']
titanic.rename(columns={'Embark':'Embarked'},inplace=True)
titanic.head()

#Drawing a pie chart for number of males and females aboard
import matplotlib.pyplot as plt
from matplotlib import style

males = (titanic['Sex'] == 1).sum() 
#Summing up all the values of column gender with a 
#condition for male and similary for females
females = (titanic['Sex'] == 2).sum()
print(males)
print(females)
p = [males, females]
plt.pie(p,    #giving array
       labels = ['Male', 'Female'], #Correspndingly giving labels
       colors = ['green', 'yellow'],   # Corresponding colors
       explode = (0.15, 0),    #How much the gap should me there between the pies
       startangle = 0)  #what start angle should be given
plt.axis('equal') 
plt.show()

# More Precise Pie Chart
MaleS=titanic[titanic.Sex==1][titanic.Survived==1].shape[0]
print(MaleS)
MaleN=titanic[titanic.Sex==1][titanic.Survived==0].shape[0]
print(MaleN)
FemaleS=titanic[titanic.Sex==2][titanic.Survived==1].shape[0]
print(FemaleS)
FemaleN=titanic[titanic.Sex==2][titanic.Survived==0].shape[0]
print(FemaleN)

chart=[MaleS,MaleN,FemaleS,FemaleN]
colors=['lightskyblue','yellowgreen','Yellow','Orange']
labels=["Survived Male","Not Survived Male","Survived Female","Not Survived Female"]
explode=[0,0.05,0,0.1]
plt.pie(chart,labels=labels,colors=colors,explode=explode,startangle=100,counterclock=False,autopct="%.2f%%")
plt.axis("equal")
plt.show()
