# 31 Create a Heatmap of Correlation Matrix using Seaborn.
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_excel('PProject.xlsx')

# Correlation matrix
corr = df.corr(numeric_only=True)

# Create heatmap
plt.figure(figsize=(10,6))

sns.heatmap(
    corr,
    annot=True
)

plt.title('Correlation Heatmap')

plt.show()
# 32Create a Pairplot for Numeric Columns using Seaborn.

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_excel('PProject.xlsx')

# Create pairplot
sns.pairplot(
    df[['Age', 'Salary', 'Profit', 'Performance_score']]
)

plt.show()

# 33 Plot Salary Distribution using KDEPlot in Seaborn.

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_excel('PProject.xlsx')

# Create kdeplot
plt.figure(figsize=(10,5))

sns.kdeplot(
    df['Salary'],
    fill=True
)

plt.title('Salary Distribution')

plt.show()

# 34 Create a Histogram with KDE using Seaborn.
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_excel('PProject.xlsx')

# Create histogram with KDE
plt.figure(figsize=(10,5))

sns.histplot(
    df['Age'],
    kde=True
)

plt.title('Age Distribution with KDE')

plt.show()
# 35 Create a Department-wise Salary Stripplot using Seaborn.

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_excel('PProject.xlsx')

# Create stripplot
plt.figure(figsize=(10,5))

sns.stripplot(
    x='Department',
    y='Salary',
    data=df
)

plt.title('Department-wise Salary Stripplot')

plt.show()

# 36 Create a Swarmplot for Performance Score using Seaborn.

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_excel('PProject.xlsx')

# Create swarmplot
plt.figure(figsize=(10,5))

sns.swarmplot(
    x='Department',
    y='Performance_score',
    data=df
)

plt.title('Performance Score Swarmplot')

plt.show()

# 37 Create a Regression Plot for Experience vs Salary using Seaborn.

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_excel('PProject.xlsx')

# Create regression plot
plt.figure(figsize=(10,5))

sns.regplot(
    x='Experience_years',
    y='Salary',
    data=df
)

plt.title('Experience vs Salary Regression Plot')

plt.show()

# 38 Create a Jointplot for Salary and Profit using Seaborn.

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_excel('PProject.xlsx')

# Create jointplot
sns.jointplot(
    x='Salary',
    y='Profit',
    data=df
)

plt.show()

# 39 Create a Rugplot for Age using Seaborn.

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_excel('PProject.xlsx')

# Create rugplot
plt.figure(figsize=(10,5))

sns.rugplot(
    df['Age']
)

plt.title('Age Rugplot')

plt.show()

# 40 Create a Categorical Barplot for Average Salary using Seaborn.

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_excel('PProject.xlsx')

# Create barplot
plt.figure(figsize=(10,5))

sns.barplot(
    x='Department',
    y='Salary',
    data=df
)

plt.title('Average Salary by Department')

plt.show()