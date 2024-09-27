# -*- coding: utf-8 -*-
"""

Original file is located at
    https://colab.research.google.com/drive/1PDVJixewHCCgme2QnJvNc7YHAgOtgEzh
"""

import pandas as pd
list = [10,20,30,40]
pd.Series(list)

#we can pass our own index as well
pd.Series(list,index=['i','ii','iii','iv'])

#creating a dataframe
d = {"name":["sundeep","venkat", "angel"], "percentage":[90,85,95]}
pd.DataFrame(d)

#different ways of creating series in pandas
#empty series
import pandas as pd
s = pd.Series()
print(s)

#create a series using arrays
import pandas as pd
import numpy as np
array = np.array([10,20,30,40])
s = pd.Series(array)
print(s)

# create a series using list
import pandas as pd
list = [10,20,30,40,50]
s = pd.Series(list)
print(s)

# create a series using dictionay
import pandas as pd
d = {'a':10, 'b':20,'c':20,'d':20}
s = pd.Series(d)
print(s)

#different ways create a dataframe in pandas
#load the data from excel file
import pandas as pd
df= pd.read_excel("/content/Book1.xlsx")
print(df)

#laod the data from csv file
import pandas as pd
df = pd.read_csv("/content/Book1.csv")
print(df)

#create dataframe using
import pandas as pd
d = {'name':['abc','def','ghi'],
     'marks':[88,99,77],
     'branch':['cs','eee','it']
     }
df = pd.DataFrame(d)
print(df)

#create a dataframe using list of tuples

import pandas as pd

d = [('abc',88,'cse'),('def',99,'eee'),('ghi',77,'it')]
df = pd.DataFrame(d)
print(df)

#attributes in series
#1.index         ----> series.index  - return all the index values
#2.array         ----> series.array  - return an array of values
#3.values        ----> series.values - return values of series
#4.name          ----> series.name   - retuns name for the seires
#5.shape         ----> series.shape  - returns shape of the series
#6.ndim          ----> series.ndim   - returns the dimention of the series
#7.size          ----> series.size   - returns the size of series(nof of elements)
#8.nbytes        ----> series.nbytes - returns memory occupied by values
#9.memory_usage  ----> series.usage  - returns memory occupied by both index and values
#10empty         ----> series.empty  - returns true if series is empty else False
import pandas as pd
list = [10,20,30,40,50]
s = pd.Series(list)
print(s.empty)

#Mathematical functions of Series
# add
# subtract
# multiply
# divison
# modulo
# power
# lessthan
# greatethan
# equalto

s1 = pd.Series([10,20,30])
s2 = pd.Series([40,50,60])
print(s1.add(s2))
print(s1.subtract(s2))
print(s1.multiply(s2))
print(s1.divide(s2))
print(s1.mod(s2))
print(s1.pow(s2))
print(s1.le(s2))
print(s1.gt(s2))
print(s1 == s2)

#indexing or accessing and slicing in dataframes in pandas

# head                  ---->   returns first 5 rows
# head(no of rows)      ---->   retuns that many no of rows which we given in
# tail                  ---->   returns last 5 rows
# tail(no of rows)      ---->   returns the many rows which we given in bracket
# describre             ---->   returns the basic mathematical formulas like count, min, max, mean, mode, sd etc...
# shape                 ---->   returns the shape of the table i.e no of rows and columns
# slice                 ---->   [start:stop:step]
# singelcolumn          ---->    df['column_name'] it will give single mentioned column
# multiplecolumn        ---->    df[col1,col2] it will give multiple columns.
# single row            ---->    df.loc[1]  returns single row

import pandas as pd
df = pd.read_csv("/content/Book1.csv")
# print(df.describe())
# print(df.columns)
# print(df.shape)
# print(df[['Roll_No','Telugu']].tail(9))
print(df[1:10:5])

#Sorting DataFrame
import pandas as pd
d = pd.read_csv("/content/Book1.csv")
# print(d)
df = pd.DataFrame(d)
# print(df)
#we can sort by using the column name
# print(df.sort_values("Name_of_Student", ascending=False))
#we can sort by uisng multiple column as well
print(df.sort_values(["Name_of_Student","Maths"]))

#Manipulations in DataFrame in Pandas

import pandas as pd
d = pd.read_csv("/content/Book1.csv")
df = pd.DataFrame(d)
print(df)
#now we are adding the column total with default value 0
# df['Total_marks']=0
#now we are adding the column with total values i.e sum of all subjects
# df['Total_marks']=df['Telugu']+df['English']+df['Maths']+df['Science']+df['Social']
print(df)
#in the same way we can remove the column by using df.drop['columnname']

#Export Dataframe to excel to csv in pandas
import pandas as pd
d = pd.read_csv("/content/Book1.csv")
df = pd.DataFrame(d)
#now i am doing add new column and exporting
df['Total_marks'] = 0
df.to_excel("/content/Book2.xlsx", index=False)
print(df)

#understanding LOC[], ILOC[],
import pandas as pd
d = pd.read_csv("/content/Book1.csv")
df = pd.DataFrame(d)
print(df)
#LOC[] is used to retrive the data in terms of rows and columns which is label based data selecting

print(df.loc[3, 'Name_of_Student']) #for one column it is fine to call the number but for two columns we need to call the label
#we can loc using slice as well below is the examle
print(df.loc[0:4, ['Name_of_Student','Telugu','Maths']])

#ILOC[] is used to retrive the data in terms of rows and columns which is index based data retrival
print(df.iloc[0:4,1:7])

#in iloc it will be giving the values by size-1

#Handling the Missing DATA
#Two ways to handle the missing data
#1 is remove, dropna()
#2 nd is fill with default value  with fillna()

# import pandas as pd
# # d = pd.read_csv("/content/abc.csv")
# df = pd.DataFrame(d)
# df.dropna().  #it remove the rows who has missing values not in original data frame it will create a new dataframe and execute this.
# print(df)
# df.fillna('Missing') # it will fill the all the missing values missing word bcz that word given by us
# df[Telugu].fillna(40) #it will fill the missing telugu valuues with 40

#Remove duplicates
import pandas as pd
d = pd.read_csv("/content/Book1.csv")
df = pd.DataFrame(d)
print(df)
#now the following is the code to remove the duplciates in the dataframe
df.duplicated() #it will show true if there are any duplicates in the dataframe
df.drop_duplicates() #it wll remove all the duplicate values from the dataframe
#if we use inplace= True the original dataframe will be effected

#Data Filtering

import pandas as pd
d = pd.read_csv("/content/Book1.csv")
df = pd.DataFrame(d)
print(df)
print(df.loc[df['Telugu']<60]) #it will give the rows who got less than 50 in telugu

print(df.loc[(df['Telugu']<60) & (df['English']<60)]) #multiple condition it will give the rows who got less than in english and telugu

