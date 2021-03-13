
# coding: utf-8

# In[ ]:


import pandas as pd
import unittest
exampledata = pd.read_csv('test.csv')
del exampledata['Unnamed: 0']

columns = exampledata.columns
def dftest(data):
    columnnames = []
    for column in data:
        print(type(data[column][0]))
        if type(data[column][0]) == str:
            raise TypeError("This dataframe contains columns that are not of type 'int64'.")
        columnnames.append(column)
    return columnnames

