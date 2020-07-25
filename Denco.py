# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 22:04:24 2020

@author: aksha
"""

import pandas as pd

data = pd.read_csv('denco.csv') #csv file with data
data
type(data)

#%%
#Top 10 Most loyal Customers
problem1 = data.groupby('custname')['custname'].count()
problem1
type(problem1)
initialresult1 = problem1.sort_values(ascending= False)
result1 = initialresult1.head(10)
print ("The most loyal Customers : \n",result1)

#%%
#Top 10 Customers contributing to revenue
problem2 = data.groupby ('custname')['revenue'].sum()
problem2
initialresult2 = problem2.sort_values(ascending = False)
result2 = initialresult2.head(10)
print ("The Customers contributing most revenue : \n",result2)

#%%
#Top 10 Parts contributing to revenue
problem3 = data.groupby ('partnum')['revenue'].sum()
problem3
initialresult3 = problem3.sort_values(ascending= False)
result3 = initialresult3.head(10)
print ("The Parts contributing most revenue : \n",result3)

#%%
#Top 10 Parts contributing highest profit margin
problem4 = data.groupby ('partnum')['margin'].sum()
problem4
initialresult4 = problem4.sort_values(ascending= False)
result4 = initialresult4.head(10)
print ("The Parts contributing highest profit margin : \n",result4)
result4

#%%
#Top 10 Customers
#Calculated by taking intersection of top 20 among most loyal customers and Customers contributing maximum revenue

loyal = initialresult1.head(20).index
loyal
revenue = initialresult2.head(20).index
revenue
result5 = loyal.intersection(revenue)
print ("The top buying customers : \n",result5)


#%%
#Top 10 Customers by revenue

problem6 = data.groupby ('custname')['revenue'].sum()
problem6
initialresult6 = problem6.sort_values(ascending= False)
result6 = initialresult6.head(10)
print ("The Customers contributing most revenue: \n",result6)










