# Dataframe 2

# 1. This program converts a dictionary into a structured table (DataFrame) to organize and display data in rows and columns.
import pandas
data = {
    "Name" :["Ram","Shyam","Mohan"],
    "Age" :["23","24","34"],
    "City":["Noida","Dadri","Greater Noida"]
}
a = pandas.DataFrame(data)
print(a)

# 2.This program uses **pandas** to create a table of data and print only the Name column.
import pandas
data = {
    "Name":["Ram","Shyam","Mohan"],
    "Age":["23","24","34"],
    "City":["Noida","Dadri","Greater Noida"]
}
a = pandas.DataFrame(data)
print(a["Name"])

import pandas
data = {
    "Name":["Ram","Shyam","Mohan"],
    "Age":["23","24","34"],
    "City":["Noida","Dadri","Greater Nodia"]
}
a = pandas.DataFrame(data)
print(a[["Name","Age"]])

# 3.This program uses **pandas** to create a table and print the first row by label and the second row by position.
import pandas
data = {
     "Name":["Ram","Shyam","Mohan"],
     "Age":["23","24","34"],
     "City":["Noida","Dadri","Greater Nodia"]
    }
a = pandas.DataFrame(data)
print(a.loc[0])
print(a.iloc[1])

# 4. This program uses **pandas** to create a table and print a specific value by row label and column name, and another value by row and column position.
import pandas
data = {
     "Name":["Ram","Shyam","Mohan"],
     "Age":["23","24","34"],
     "City":["Noida","Dadri","Greater Nodia"]
    }
a = pandas.DataFrame(data)
print(a.loc[1,"Name"])
print(a.iloc[1,2])

# 5.This program (using **pandas**) would show the table’s number of rows and columns, total values, column names, and data types.
import pandas
data = {
     "Name":["Ram","Shyam","Mohan"],
     "Age":["23","24","34"],
     "City":["Noida","Dadri","Greater Nodia"]
    }
a = pandas.DataFrame(data)
print(a.shape)
print(a.size)
print(a.columns)
print(a.dtypes)


# 6.This program uses **pandas** to create a sales table and calculate the total revenue and total profit.
import pandas
sales = {
     "Months":["Jan","Feb","Mar"],
     "Revenue":[5000,6000,9000],
     "Profit":[500,600,900]
    }
a = pandas.DataFrame(sales)
print("Total Revenue:",a["Revenue"].sum())
print("Total Profit:",a["Profit"].sum())

# 7.This program uses **pandas** to create a students table, display it, and calculate the average of the Marks column.
import pandas
students = {
    "Name": ["Mohan","Sohan","Sita"],
    "Marks": [15,44,49],
    "Result":["Fail","Pass","Pass"]
}
a = pandas.DataFrame(students)
print(a)
print("Average Marks:",a["Marks"].mean())