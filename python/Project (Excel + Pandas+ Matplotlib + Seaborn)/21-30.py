# 21 Create a Step Graph for Salary using Matplotlib.
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_excel('PProject.xlsx')
# Create step graph
plt.figure(figsize=(12,5))
plt.step(
    df.index,
    df['Salary']
)
plt.title('Salary Step Graph')
plt.xlabel('Employee Index')
plt.ylabel('Salary')
plt.show()


# 22 Create a Logarithmic Salary Graph using Matplotlib.


import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_excel('PProject.xlsx')
# Create logarithmic plot
plt.figure(figsize=(12,5))
plt.semilogy(
    df['Salary']
)
plt.title('Logarithmic Salary Plot')
plt.xlabel('Employee Index')
plt.ylabel('Salary')
plt.show()


# 23 Plot Moving Average of Salary using Matplotlib.
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_excel('PProject.xlsx')
# Calculate moving average
df['Salary_MA'] = df['Salary'].rolling(window=5).mean()
# Plot moving average
plt.figure(figsize=(12,5))
plt.plot(
    df['Salary_MA']
)
plt.title('Salary Moving Average')
plt.xlabel('Employee Index')
plt.ylabel('Moving Average Salary')
plt.show()

# 24 Plot Department Count using Vertical Bar Chart in Matplotlib.


import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_excel('PProject.xlsx')
# Count departments
counts = df['Department'].value_counts()
# Create bar chart
plt.figure(figsize=(10,5))
plt.bar(
    counts.index,
    counts.values
)
plt.title('Department Count')
plt.xlabel('Department')
plt.ylabel('Count')
plt.show()


# 25 Create a Donut Chart for Cities using Matplotlib.
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_excel('PProject.xlsx')
# Count cities
city_counts = df['City'].value_counts()
# Create donut chart
plt.figure(figsize=(8,8))
plt.pie(
    city_counts.values,
    labels=city_counts.index
)
circle = plt.Circle((0,0), 0.7, color='white')
plt.gca().add_artist(circle)
plt.title('City Distribution')
plt.show()

# 26 Create a Seaborn Scatterplot for Salary vs Performance Score.

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_excel('PProject.xlsx')
# Create scatterplot
plt.figure(figsize=(10,5))
sns.scatterplot(
    x='Salary',
    y='Performance_score',
    data=df
)
plt.title('Salary vs Performance Score')
plt.show()

# 27 Create a Seaborn Lineplot for Monthly Sales.
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_excel('PProject.xlsx')
# Create lineplot
plt.figure(figsize=(12,5))
sns.lineplot(
    x=df.index,
    y='Monthly_sales',
    data=df
)
plt.title('Monthly Sales Lineplot')
plt.show()


# 28 Create a Countplot for Departments using Seaborn.

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_excel('PProject.xlsx')
# Create countplot
plt.figure(figsize=(10,5))
sns.countplot(
    x='Department',
    data=df
)
plt.title('Department Countplot')
plt.show()

# 29 Create a Boxplot for Salary by Department using Seaborn.
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_excel('PProject.xlsx')
# Create boxplot
plt.figure(figsize=(10,5))
sns.boxplot(
    x='Department',
    y='Salary',
    data=df
)
plt.title('Salary by Department')
plt.show()


# 30 Create a Violin Plot for Salary using Seaborn.
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_excel('PProject.xlsx')
# Create violin plot
plt.figure(figsize=(8,5))
sns.violinplot(
    y='Salary',
    data=df
)
plt.title('Salary Violin Plot')
plt.show()
