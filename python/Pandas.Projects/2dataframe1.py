#  Dataframe in pandas

# 1. This program reads data from a CSV file named **1.csv** into a Pandas DataFrame and prints it.
import pandas
a = pandas.read_csv("1.csv")
print(a)

# 2. This program creates a 2D NumPy array, converts it into a Pandas DataFrame with column names (Jan, Feb, Mar), and prints it.
import numpy
import pandas
a = numpy.array([[10,20,30,],
                [40,50,60]])
b = pandas.DataFrame(a,columns=["Jan","Feb","Mar"])
print(b)

# 3.This program creates a Pandas DataFrame from a list of lists with columns "Name" and "Age" and prints it.
import pandas
list_data = (["Ram",10],
             ["Shyam",12])
a = pandas.DataFrame(list_data,columns=("Name","Age"))
print(a)

# 4. This program creates a Pandas DataFrame from a dictionary and prints only the "Score" column.
import pandas
dict_data = {
    "Name": ["X", "Y"],
    "Score": [90, 85]
    }
a = pandas.DataFrame(dict_data)
print(a["Score"])

# 5.This program creates a 2×2 NumPy array, converts it into a Pandas DataFrame, and prints it. 
import numpy
import pandas
a = numpy.array([[10,20],
                 [30,40]])
b = pandas.DataFrame(a)
print(b)