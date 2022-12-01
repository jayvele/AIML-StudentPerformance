# -*- coding: utf-8 -*-
"""ML-Mini-Project.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/105-AQkFi1CmbZrf0VX-jGibNkTZtTPD8

**Problem Statement:**
We have been given a set of student scores in multiple subjects and a list of factors which might possibly affect the student performance. We have to use a ML algorithm (Decision Tree Regressor) to find the factor on which the student performance is the most dependent.

**Importing libraries**
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

"""**Loading dataset using pandas**"""

df = pd.read_csv('/content/StudentsPerformance.csv.xls')
df.head()

"""**Checking for null values**"""

df.isnull().sum()

"""**No null values found**"""

from sklearn.preprocessing import LabelEncoder

"""**Importing LabelEncoder to convert categorical data to integer data**"""

le = LabelEncoder()
df['gender'] = le.fit_transform(df['gender'])
df['race/ethnicity'] = le.fit_transform(df['race/ethnicity'])
df['parental level of education'] = le.fit_transform(df['parental level of education'])
df['lunch'] = le.fit_transform(df['lunch'])
df['test preparation course'] = le.fit_transform(df['test preparation course'])

df.head()

"""**Calculating Average of scores of all the three subjects to get a single attribute to compare and build the model on.**"""

df['Average'] = (df['math score']+df['reading score']+df['writing score'])/3
df.head()

from sklearn.tree import DecisionTreeRegressor
clf  = DecisionTreeRegressor(random_state=1234)

"""**Applying Decision Tree Regressor to the whole dataset first**"""

X=df.iloc[:,:-4]
y=df.iloc[:,1]
model = clf.fit(X,y)

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=70)
print(X_train.shape)
print(y_train.shape)

DT = DecisionTreeRegressor(max_depth = 2)
DT.fit(X_train,y_train)

print(DT.score(X_test,y_test))
print(DT.score(X_train,y_train))

"""**Applying Decision Tree Regressor on Specific Two features**

**Parental Level of Education and Test Preparation Course**
"""

col_names = ['parental level of education','test preparation course']
X = df[col_names]

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=70)

DT1 = DecisionTreeRegressor()
DT1.fit(X_train,y_train)

print(DT1.score(X_test,y_test))

print(DT1.score(X_train,y_train))

"""**The data underfits the tree hence not accepted**

**Applying Decision Tree Regressor on Specific Three features**  


**On Parental Level of Education and Test Preparation Course and race/ethnicity**
"""

col_names = ['test preparation course','parental level of education','race/ethnicity']
X = df[col_names]
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=70)
DT1 = DecisionTreeRegressor(max_depth = 2)
DT1.fit(X_train,y_train)
print(DT1.score(X_test,y_test))

"""**The Addition of race/ethnicity increases the accuracy of the model, thus making it the most important feature for this dataset**  
**This may speak to people of higher races thus having more money generally may have better resources to study and get good grades**
"""

col_names = ['test preparation course','parental level of education','race/ethnicity','gender']
X = df[col_names]
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=70)
DT1 = DecisionTreeRegressor(max_depth = 2)
DT1.fit(X_train,y_train)
print(DT1.score(X_test,y_test))

"""**Thus on adding gender there is no change in the accuracy of the model making it redundant as a parameter**"""

col_names = ['test preparation course','parental level of education','race/ethnicity','lunch','gender']

X = df[col_names]
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=70)
DT1 = DecisionTreeRegressor(max_depth = 2)
DT1.fit(X_train,y_train)
print(DT1.score(X_test,y_test))

"""**Same can be said of lunch, making both lunch and gender redundant as parameters**"""

accuracies = [0.011125143368274193,0.9545078284357265,0.9545078284357265,0.9545078284357265]
parameters = [2,3,4,5]

plt.plot(parameters,accuracies)
plt.title('parameters vs accuracies')
plt.xlabel('Parameter')
plt.ylabel('Accuracy')
plt.show()

"""**Now we check at which depth does the model overfit**"""

col_names = ['test preparation course','parental level of education','race/ethnicity']
X = df[col_names]
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=70)

scores_test = []
scores_train = []
for i in range(1,100):
    DT1 = DecisionTreeRegressor(max_depth = i)
    DT1.fit(X_train,y_train)
    scores_test.append(DT1.score(X_test,y_test))
    scores_train.append(DT1.score(X_train,y_train))

x = [i for i in range(1,100)]
plt.plot(x, scores_test, label ='Test')
plt.plot(x, scores_train, '-.', label ='Train')

plt.xlabel("Depth")
plt.ylabel("Accuracy")
plt.legend()
plt.title('Test vs Train')
plt.show()

"""**We can see that both test and train plots go together until around max depth of 3 after which they become constant thus overfitting the model**"""

