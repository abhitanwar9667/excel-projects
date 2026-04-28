# 1. simple filter
import pandas
a = pandas.read_excel("Files/Projectpandas.xlsx")
print(a["Total Fees"] > 4000)

# 2. multiple condition AND &
import pandas
a = pandas.read_excel("Files/Projectpandas.xlsx")
print(a[(a["Total Fees"] > 4000) & (a["Tution Fees"] > 1100)])

# 3. multiple condition OR
import pandas
a = pandas.read_excel("Files/Projectpandas.xlsx")
print(a[(a["Total Fees"] > 4000) |( a["Bus Fees"] > 1200)])

# 4. isin function 
import pandas
a = pandas.read_excel("Files/Projectpandas.xlsx")
print(a[a["Class"].isin([4])])

# 5. between function
import pandas
a = pandas.read_excel("Files/Projectpandas.xlsx")
print(a[a["Total Fees"].between(4000,4500)])

# 6. text fileter (startswith)
import pandas
a = pandas.read_excel("Files/Projectpandas.xlsx")
print(a[a["Name"].str.startswith("R")])

# 7. text filter(contain)
import pandas
a = pandas.read_excel("Files/Projectpandas.xlsx")
print(a[a["Name"].str.contains("ee")])