#Importing the libraries

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#Importing the dataset

dataset=pd.read_csv('C:\\Users\\DELL\\Desktop\\PRAWIZARD\\MachineLearning Udemy\\Machine Learning A-Z Template Folder\\Part 2 - Regression\\Section 5 - Multiple Linear Regression\\Multiple_Linear_Regression\\50_Startups.csv')
X=dataset.iloc[:, :-1].values
y=dataset.iloc[:, 4].values


#Encoding categorical data
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_X=LabelEncoder()
X[:,3]=labelencoder_X.fit_transform(X[:,3])
onehotencoder=OneHotEncoder(categorical_features=[3])
X=onehotencoder.fit_transform(X).toarray()

#Avoiding dummy variable trap
X=X[:,1:]

#splitting the dataset into training set and test set
from sklearn.cross_validation import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=0)

#Fitting Multiple Linear Regression to the training set
from sklearn.linear_model import LinearRegression
regressor=LinearRegression()
regressor.fit(X_train,y_train)

#Predicting test set results
y_pred=regressor.predict(X_test)

#Building optimal model using backward elimination
import statsmodels.formula.api as sm
X=np.append(arr=np.ones((50,1)).astype(int), values=X, axis=1)
X_opt=X[:,[0,1,2,3,4,5]]
regressor_OLS=sm.OLS(endog=y, exog=X_opt).fit()
regressor_OLS.summary()

X_opt=X[:,[0,1,3,4,5]]
regressor_OLS=sm.OLS(endog=y, exog=X_opt).fit()
regressor_OLS.summary()

X_opt=X[:,[0,3,4,5]]
regressor_OLS=sm.OLS(endog=y, exog=X_opt).fit()
regressor_OLS.summary()

X_opt=X[:,[0,3,5]]
regressor_OLS=sm.OLS(endog=y, exog=X_opt).fit()
regressor_OLS.summary()

X_opt=X[:,[0,3]]
regressor_OLS=sm.OLS(endog=y, exog=X_opt).fit()
regressor_OLS.summary()





