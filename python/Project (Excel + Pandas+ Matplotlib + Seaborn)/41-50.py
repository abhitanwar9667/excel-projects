# 41 Create a Pointplot for Department Salary using Seaborn.

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_excel('PProject.xlsx')
# Create pointplot
plt.figure(figsize=(10,5))
sns.pointplot(
    x='Department',
    y='Salary',
    data=df
)
plt.title('Department Salary Pointplot')
plt.show()


# 42 Create a Heatmap for Missing Values using Seaborn.

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_excel('PProject.xlsx')
# Create heatmap for missing values
plt.figure(figsize=(10,5))
sns.heatmap(
    df.isnull(),
    cbar=False
)
plt.title('Missing Values Heatmap')
plt.show()


# 43 Create a scatter plot to show the relationship between Age and Salary.

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_excel('PProject.xlsx')
sns.scatterplot(x='Age', y='Salary', data=df)
plt.title('Age vs Salary')
plt.show()

# 44 Compare Salary Distributions by Department using Seaborn Boxenplot.

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_excel('PProject.xlsx')
# Create boxenplot
plt.figure(figsize=(10,5))
sns.boxenplot(
    x='Department',
    y='Salary',
    data=df
)
plt.title('Salary Distribution by Department')
plt.show()



# 45 Create a Facet Grid for Departments using Seaborn.

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_excel('PProject.xlsx')
# Create facet grid
g = sns.FacetGrid(
    df,
    col='Department'
)
g.map(
    plt.hist,
    'Salary'
)
plt.show()


# 46 Create a Displot for Profit using Seaborn.

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_excel('PProject.xlsx')
# Create displot
sns.displot(
    df['Profit'],
    kde=True
)
plt.show()


# 47 Create an ECDF Plot for Salary using Seaborn.

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_excel('PProject.xlsx')
# Create ECDF plot
plt.figure(figsize=(10,5))
sns.ecdfplot(
    df['Salary']
)
plt.title('Salary ECDF Plot')
plt.show()


# 48 Create a Relational Plot for Experience and Salary using Seaborn.
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_excel('PProject.xlsx')
# Create relational plot
sns.relplot(
    x='Experience_years',
    y='Salary',
    hue='Department',
    data=df
)
plt.show()

# 49 Create a Categorical Plot for City-wise Salary using Seaborn.

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_excel('PProject.xlsx')
# Create categorical plot
sns.catplot(
    x='City',
    y='Salary',
    kind='bar',
    data=df
)
plt.show()

# 50 Create a Dashboard-style Visualization using Multiple Plots.

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_excel('PProject.xlsx')
# Create dashboard
fig, ax = plt.subplots(2, 2, figsize=(14,10))
# Salary distribution
sns.histplot(
    df['Salary'],
    ax=ax[0,0]
)
ax[0,0].set_title('Salary Distribution')

# Department salary
sns.boxplot(
    x='Department',
    y='Salary',
    data=df,
    ax=ax[0,1]
)
ax[0,1].set_title('Department Salary')

# Experience vs Salary
sns.scatterplot(
    x='Experience_years',
    y='Salary',
    data=df,
    ax=ax[1,0]
)
ax[1,0].set_title('Experience vs Salary')

# Department count
sns.countplot(
    x='Department',
    data=df,
    ax=ax[1,1]
)
ax[1,1].set_title('Department Count')
plt.tight_layout()
plt.show()
