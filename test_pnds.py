import numpy as np
import pandas as pd
"""
#Creating dataset, converting to dataframe
myds = {'subject' : ["Math", "Physics", "Chemistry", "CS"], 'grade' : [98, 97, 100, 100]}
mydf = pd.DataFrame(myds)
print(mydf)

#Series
arr = [10, 20, 30]
result = pd.Series(arr)
print(result) #int64
result2 = pd.Series(arr, index = ["x", "y", "z"])
print(result, result2["y"]) #Gives value corresponding to index 20

#Iterating through dataframe
arr = [10, 20, 30]
result = pd.Series(arr, index = ["x", "y", "z"])
print(result)
for i in range(len(result)):
    print(result[i])

#Location in dataframe
myds = {'Subject' : ["Math", "Physics", "Chemistry", "CS"], 'Grade' : [98, 97, 100, 100]}
mydf = pd.DataFrame(myds)
print(mydf.loc[0]) #Prints first row
print(mydf.loc[[0, 1]]) #Printing first 2 rows at once
print(mydf.loc[[0, 2]]) #Printing first and third rows at once
myds = {'Subject' : ["Math", "Physics", "Chemistry", "CS"], 'Grade' : [98, 97, 100, 100]}
mydf = pd.DataFrame(myds, index = ["Sub1", "Sub2", "Sub3", "Sub4"])
print(mydf.loc["Sub1"]) #Prints first row
print(mydf.loc[["Sub1", "Sub2"]]) #Printing first 2 rows at once
print(mydf.loc[["Sub1", "Sub3"]]) #Printing first and third rows at once
"""

#Loading from csv files
result = pd.read_csv('data.csv')
#print(result.to_string())
#print(pd.options.display.max_rows)#max no. of rows comp wants to read
#print(pd.options.display.min_rows)
#print(result.head(10)) #Prints 0 to 9 rows
#print(result.tail(10)) #Displays the last n rows, 5 by default
#print(result.info()) #Gives metadata - data about data
#result.dropna(inplace = True)  #Dropping rows with no values (NaN) and modifies result
#print(result.info())
#Fill Na
#result1 = result.fillna(result1["Calories"].mean()) #Replaces nan values with 130
#print(result1.to_string())
#x = result["Calories"].mean()
#y = result["Calories"].median()
#z = result["Calories"].mode()
#print(x, y, z)
#result = result.fillna(round(result["Calories"].mean(), 2))
#print(result.to_string())
#result.dropna(inplace = True)
#result["Date"] = pd.to_datetime(result['Date']) #Formatting dates
#print(result.to_string())
#result.loc[3, 'Duration'] = 45 #sets value of row, column
#print(result.to_string())
"""
#Modifying values in a loop
for x in result.index:
    if result.loc[x, 'Duration'] > 120:
        result.loc[x, 'Duration'] = 120
print(result.to_string())
"""
#print(result.duplicated().to_string()) #searches for duplicates
#result.drop_duplicates(inplace = True)
#print(result.duplicated().to_string())
#print(result.to_string())