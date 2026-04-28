# 1.to print the top 10 rows from the data
import pandas
a = pandas.read_excel("Files/Projectpandas.xlsx")
print(a.head(10))

# 2. to print the bottom 10 rows from the data
import pandas
a = pandas.read_excel("Files/Projectpandas.xlsx")
print(a.tail(10))

# 3. to print the info of the data like dtype,count
import pandas
a = pandas.read_excel("Files/Projectpandas.xlsx")
print(a.info())

# 4. to print the shape of the data like number of rows and columns
import pandas
a = pandas.read_excel("Files/Projectpandas.xlsx")
print(a.shape)

# 5. to describe the data
import pandas
a = pandas.read_excel("Files/Projectpandas.xlsx")
print(a.describe)

# 6. to print the columns header from the data
import pandas
a = pandas.read_excel("Files/Projectpandas.xlsx")
print(a.columns)

# 7. to print the datatype
import pandas
a = pandas.read_excel("Files/Projectpandas.xlsx")
print(a.dtypes)