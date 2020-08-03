#%% Linear Regression -1 Marketing Data - Sales - YT, FB, print
#libraries
import numpy as np
import pandas as pd
import math 
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.metrics import mean_absolute_error
from sklearn import linear_model #1st method
import statsmodels.api as sm  #2nd method
import matplotlib.pyplot as plt
import seaborn as sns
import RegscorePy

url ='https://raw.githubusercontent.com/DUanalytics/datasets/master/R/marketing.csv'
marketing = pd.read_csv(url)
marketing.head()

#describe data
marketing.describe
marketing.shape
marketing.info()

#visualise few plots to check correlation

sns.scatterplot(data=marketing, x='youtube', y='sales')

sns.scatterplot(data=marketing, x='facebook', y='sales')

sns.scatterplot(data=marketing, x='newspaper', y='sales')

#split data into train and test

IV = marketing[['youtube','facebook','newspaper']].values
IV
DV= marketing['sales'].values
DV
IV_train, IV_test, DV_train, DV_test = train_test_split(IV, DV,test_size=0.25, random_state=123)
IV_train, IV_test, DV_train, DV_test

#build the model
#method 1

SalesPredictModel1 = linear_model.LinearRegression()
SalesPredictModel1.fit(IV_train, DV_train)  #putting data to model
SalesPredictModel1.intercept_
SalesPredictModel1.coef_

#method 2

IV1 = sm.add_constant(IV)
model = sm.OLS(DV, IV1).fit()
print(model.summary())
model.rsquared  #coeff of determination
model.rsquared_adj 

#predict on test values

DV_predicted = SalesPredictModel1.predict(IV_test)
DV_predicted
type(DV_predicted)
T=len(DV_predicted)
DV_test
r2_score(DV_train, SalesPredictModel1.predict(IV_train))

#boxplot

sns.boxplot(x=DV_test)
plt.show();

sns.boxplot(x=DV_predicted) #there are no outliers in the predicted values
plt.show();

#density plot

p1=sns.kdeplot(DV_predicted, shade=True, color="g",legend = True, label="DV_predicted")
p1=sns.kdeplot(DV_test, shade=True, color="b",legend = True, label="DV_test")
plt.show();

#Histogram
#predicted
sns.distplot( DV_predicted , color="skyblue", label="DV_predicted")
sns.plt.legend()
plt.show();
#actual
sns.distplot( DV_test , color="red", label="DV_test")
sns.plt.legend()
plt.show();

#metrics - R2, Adjt R2, RMSE, MAPE etc

#Mean Absolute Error
mae = mean_absolute_error(DV_test, DV_predicted)
print(mae)

#MSE
mse = mean_squared_error(DV_test, DV_predicted)
print(mse)

#R Square
r_squared = r2_score(DV_test, DV_predicted) 
print(r_squared)

#Adj R Square uaing SST = SSR+SSE
SS_Residual = sum((DV_test-DV_predicted)**2)      #RSS 
SS_Total = sum((DV_test-np.mean(DV_test))**2)     #TSS
SS_Error = SS_Total-SS_Residual                   #ESS
adjusted_r_squared = 1 - (1-r_squared)*(len(DV_test)-1)/(len(DV_test)-IV_test.shape[1]-1)
print (adjusted_r_squared)

#RMSE
rmse = math.sqrt(mean_squared_error(DV_test, DV_predicted))
print(rmse)

#MAPE
mape = np.mean(np.abs((DV_test - DV_predicted) / DV_test)) * 100
print(mape)

#F-statistic using F statistic = ESS / (RSS/(T-2))
Fstat = SS_Error/(SS_Residual/(T-2))
print (Fstat)
# this value is better than 570.3 obtained for the model with one fixed constant so this model is better

#AIC
AIC= RegscorePy.aic.aic(DV_test, DV_predicted, p=1)
print(AIC)


#predict on new value
newdata = pd.DataFrame({'youtube':[50,60,70], 'facebook':[20, 30, 40], 'newspaper':[70,75,80]})
newdata
DV_NewPredict = SalesPredictModel1.predict(newdata)
DV_NewPredict
#your ans should be close to [ 9.51, 11.85, 14.18] 

# The values were close to the mentioned values.

