# 1  Create a Line Chart of Salary vs Employee Index using Matplotlib.

import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_excel('PProject.xlsx')

# Create line chart
plt.figure(figsize=(12,5))
plt.plot(df['Salary'])
plt.title('Salary Line Chart')
plt.xlabel('Employee Index')
plt.ylabel('Salary')
plt.show()

# 2 Create a Bar Chart showing total employees in each department using Matplotlib.
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_excel('PProject.xlsx')
# Count employees department-wise
department_counts = df['Department'].value_counts()
# Create bar chart
plt.figure(figsize=(10,5))
plt.bar(
    department_counts.index,
    department_counts.values
)
plt.title('Employees per Department')
plt.xlabel('Department')
plt.ylabel('Employee Count')
plt.show()

# 3 Create a Histogram for Employee Ages using Matplotlib.

import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_excel('PProject.xlsx')
# Create histogram
plt.figure(figsize=(10,5))
plt.hist(
    df['Age'],
    bins=10
)
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()

# 4 Create a Scatter Plot between Salary and Performance Score using Matplotlib.

import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_excel('PProject.xlsx')
# Create scatter plot
plt.figure(figsize=(10,5))
plt.scatter(
    df['Salary'],
    df['Performance_score']
)
plt.title('Salary vs Performance Score')
plt.xlabel('Salary')
plt.ylabel('Performance Score')
plt.show()


# 5 Create a Pie Chart for Department Distribution using Matplotlib.

import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_excel('PProject.xlsx')
# Count departments
department_counts = df['Department'].value_counts()
# Create pie chart
plt.figure(figsize=(8,8))
plt.pie(
    department_counts.values,
    labels=department_counts.index,
    autopct='%1.1f%%'
)
plt.title('Department Distribution')
plt.show()


# 6 Plot Monthly Sales for First 20 Employees using Matplotlib.
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_excel('PProject.xlsx')
# Plot monthly sales
plt.figure(figsize=(12,5))
plt.plot(
    df['Monthly_sales'].head(20),
    marker='o'
)
plt.title('Monthly Sales of First 20 Employees')
plt.xlabel('Employee Index')
plt.ylabel('Monthly Sales')
plt.show()


#7 Create a Horizontal Bar Chart for City Counts using Matplotlib.
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_excel('PProject.xlsx')
# Count cities
city_counts = df['City'].value_counts()
# Create horizontal bar chart
plt.figure(figsize=(10,6))
plt.barh(
    city_counts.index,
    city_counts.values
)
plt.title('Employees by City')
plt.xlabel('Count')
plt.ylabel('City')
plt.show()
#8 Compare Monthly Sales and Monthly Expense using Line Plots.

import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_excel('PProject.xlsx')
# Create line plots
plt.figure(figsize=(12,5))
plt.plot(
    df['Monthly_sales'],
    label='Sales'
)
plt.plot(
    df['Monthly_expense'],
    label='Expense'
)
plt.title('Sales vs Expense')
plt.xlabel('Employee Index')
plt.ylabel('Amount')
plt.legend()
plt.show()


#9 Create a Box Plot for Salary using Matplotlib.

import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_excel('PProject.xlsx')
# Create box plot
plt.figure(figsize=(6,5))
plt.boxplot(df['Salary'])
plt.title('Salary Box Plot')
plt.show()

#10 Plot Profit Distribution using Histogram in Matplotlib.

import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_excel('PProject.xlsx')
# Create histogram
plt.figure(figsize=(10,5))
plt.hist(
    df['Profit'],
    bins=15
)
plt.title('Profit Distribution')
plt.xlabel('Profit')
plt.ylabel('Frequency')
plt.show()