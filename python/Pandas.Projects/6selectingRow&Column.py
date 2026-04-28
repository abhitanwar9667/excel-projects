# 1. to select the name from the data
import pandas
a = pandas.read_excel("Files/Projectpandas.xlsx")
print(a["Name"]) 

# 2. to select the two or more columns at one time
import pandas
a = pandas.read_excel("Files/Projectpandas.xlsx")
print(a[["Name","Age"]])

# 3. to print the row by location
import pandas
a = pandas.read_excel("Files/Projectpandas.xlsx")
print(a.loc[0])
print(a.loc[0:2])
print(a.iloc[0:4,1:3])

# 4. to print the row and columns together
import pandas
a = pandas.read_excel("Files/Projectpandas.xlsx")
print(a.loc[0:3,["Name","Class"]])
print(a.iloc[0:4,1:3])