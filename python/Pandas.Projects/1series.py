#  Series in Pandas

# 1.This program creates a Pandas Series from a list of numbers and prints it.
import pandas
a = [100,200,300,400]
b = pandas.Series(a)
print(b)

# 2. This program creates a Pandas Series with custom labels (a, b, c, d) and prints it.
import pandas
a = pandas.Series([100,200,300,400],index=["a","b","c","d"])
print(a)

# 3. This program creates a Pandas Series and prints the value at index position 0.
import pandas
a = pandas.Series([100,200,300,400])
print(a[0])

# 4. This program creates a Pandas Series and adds 10 to each value, then prints the updated values.
import pandas
a = pandas.Series([100,200,300,400],index=["a","b","c","d"])
print(a+10)

# 5.This program creates a Pandas Series and prints its values, index labels, and data type.
import pandas
a = pandas.Series([100,200,300,400],index=["a","b","c","d"])
print(a.values)
print(a.index)
print(a.dtype)