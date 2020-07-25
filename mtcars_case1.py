#Case Study on mtcars dataset in Python	download data

#Download data
import statsmodels.api as sm
#https://vincentarelbundock.github.io/Rdatasets/datasets.html
dataset_mtcars = sm.datasets.get_rdataset(dataname='mtcars', package='datasets')
dataset_mtcars.data.head()
mtcars = dataset_mtcars.data
#structure

#summary
mtcars

#print first / last few rows

mtcars.head() #can add number within the brackets and enter number of rows to be printed
mtcars.tail() #can add number within the brackets and enter number of rows to be printed


#print number of rows

numberofrows = len(mtcars.index)
print ("Number of rows : ", numberofrows)


#number of columns

numberofcolumns = len(mtcars.columns)
print ("Number of columns : ", numberofcolumns)

#print names of columns

Columnnames = mtcars.columns
Columnnames

#Filter Rows
#cars with cyl=8

cyl8 = mtcars['cyl']==8 
cyl8
mtcars_cyl8 = mtcars[cyl8]
print ("Rows with cyl=8 :",mtcars_cyl8)

#cars with mpg <= 27

mpg27 = mtcars['mpg']<=27
mpg27
mtcars_mpg27 = mtcars[mpg27]
print ("Rows with cyl=8 :",mtcars_mpg27)

#rows match auto tx

#First Row

firstrow = mtcars.head(1)
print("First row :", firstrow)

#last Row

lastrow = mtcars.tail(1)
print("Last row :", lastrow)

# 1st, 4th, 7th, 25th row + 1st 6th 7th columns.


# first 5 rows and 5th, 6th, 7th columns of data frame

#rows between 25 and 3rd last

#alternative rows and alternative column

#find row with Mazda RX4 Wag and columns cyl, am

#find row betwee Merc 280 and Volvo 142E Mazda RX4 Wag and columns cyl, am


# mpg > 23 or wt < 2

mpg23wt2 = mtcars[(mtcars['mpg']>23) or (mtcars['wt']<2)]
mpg23wt2
mtcars_mpg23wt2 = mtcars[mpg23wt2]
print ("Rows with mpg > 23 or wt < 2 :",mtcars_mpg23wt2)

#using lambda for above


#with or condition

#find unique rows of cyl, am, gear


#create new columns: first make a copy of mtcars to mtcars2

#keeps other cols and divide displacement by 61

# multiple mpg * 1.5 and save as original column

