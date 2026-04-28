
# 1. To Import Excel Files in Pandas
import pandas
a = pandas.read_excel("Files/Projectpandas.xlsx")
print(a)

# 2. To Select only 5 rows from the data
import pandas
a = pandas.read_excel("Files/Projectpandas.xlsx",nrows=5)
print(a)

# 3. To print specific columns from the data
import pandas
a = pandas.read_excel("Files/Projectpandas.xlsx",usecols=["Name","Age"])
print(a)

# 4. To change the header of the columns
import pandas
a = pandas.read_excel("Files/Projectpandas.xlsx",names=["A","B","C","D","E","F"],header=0)
print(a)
