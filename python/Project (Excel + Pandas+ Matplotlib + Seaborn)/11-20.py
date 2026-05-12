#11 Create an Area Chart for Monthly Sales using Matplotlib.
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_excel('PProject.xlsx')
# Create area chart
plt.figure(figsize=(12,5))
plt.fill_between(
    range(len(df)),
    df['Monthly_sales']
)
plt.title('Monthly Sales Area Chart')
plt.xlabel('Employee Index')
plt.ylabel('Monthly Sales')
plt.show()


#12 Plot Salary Trend for Employees using Matplotlib.


import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_excel('PProject.xlsx')
# Plot salary trend
plt.figure(figsize=(12,5))
plt.plot(
    df['Salary']
)
plt.title('Salary Trend')
plt.xlabel('Employee Index')
plt.ylabel('Salary')
plt.show()


#13 Create a Stacked Bar Chart for Sales and Expenses using Matplotlib.


import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_excel('PProject.xlsx')
# Create stacked bar chart
plt.figure(figsize=(12,5))
plt.bar(
    df.index,
    df['Monthly_sales'],
    label='Sales'
)
plt.bar(
    df.index,
    df['Monthly_expense'],
    bottom=df['Monthly_sales'],
    label='Expense'
)
plt.title('Sales and Expense Comparison')
plt.xlabel('Employee Index')
plt.ylabel('Amount')
plt.legend()
plt.show()


#14 Plot Age Frequency using Histogram in Matplotlib.


import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_excel('PProject.xlsx')
# Create histogram
plt.figure(figsize=(10,5))
plt.hist(
    df['Age'],
    bins=8,
    edgecolor='black'
)
plt.title('Age Frequency')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()


#15 Create a Scatter Plot for Experience vs Salary using Matplotlib.


import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_excel('PProject.xlsx')
# Create scatter plot
plt.figure(figsize=(10,5))
plt.scatter(
    df['Experience_years'],
    df['Salary']
)
plt.title('Experience vs Salary')
plt.xlabel('Experience')
plt.ylabel('Salary')
plt.show()

#16 Plot Department-wise Average Salary using Matplotlib.
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_excel('PProject.xlsx')
# Calculate average salary
avg_salary = df.groupby('Department')['Salary'].mean()
# Create bar chart
plt.figure(figsize=(10,5))
plt.bar(
    avg_salary.index,
    avg_salary.values
)
plt.title('Average Salary by Department')
plt.xlabel('Department')
plt.ylabel('Average Salary')
plt.show()


#17 Create a Cumulative Salary Graph using Matplotlib.

import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_excel('PProject.xlsx')
# Create cumulative graph
plt.figure(figsize=(12,5))
plt.plot(
    df['Salary'].cumsum()
)
plt.title('Cumulative Salary')
plt.xlabel('Employee Index')
plt.ylabel('Cumulative Salary')
plt.show()

#18 Compare Employee Profits using Bar Chart in Matplotlib.

import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_excel('PProject.xlsx')
# Create bar chart
plt.figure(figsize=(12,5))
plt.bar(
    df.index,
    df['Profit']
)
plt.title('Employee Profits')
plt.xlabel('Employee Index')
plt.ylabel('Profit')
plt.show()

#19 Create Subplots for Salary and Profit using Matplotlib.

import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_excel('PProject.xlsx')
# Create subplots
fig, ax = plt.subplots(1, 2, figsize=(12,5))
# Salary plot
ax[0].plot(df['Salary'])
ax[0].set_title('Salary')
# Profit plot
ax[1].plot(df['Profit'])
ax[1].set_title('Profit')
plt.show()

#20 Create a Stem Plot for Performance Score using Matplotlib.

import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_excel('PProject.xlsx')
# Create stem plot
plt.figure(figsize=(10,5))
plt.stem(
    df['Performance_score']
)
plt.title('Performance Score Stem Plot')
plt.xlabel('Employee Index')
plt.ylabel('Performance Score')
plt.show()