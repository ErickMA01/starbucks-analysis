import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# colors = sns.color_palette('husl', n_colors=20)

df = pd.read_csv('starbucks.csv')
df.info()
print(df.describe())
df.shape
df.nunique()
df.dtypes
df.isnull().sum()

'''
Renaming Columns
df.rename(columns ={ 
    ' Total Fat (g)': 'total_fat_g',
    'Trans Fat (g) ': 'trans_fat_g',
    'Saturated Fat (g)': 'saturated_fat_g',
    ' Sodium (mg)': 'sodium_mg',
    ' Total Carbohydrates (g) ': 'total_carbohydrates_g',
    'Cholesterol (mg)': 'cholesterol_mg',
    ' Dietary Fibre (g)': 'dietary_fibre_g',
    ' Sugars (g)': 'sugar_g',
    ' Protein (g) ': 'protein_g',
    'Vitamin A (% DV) ': 'Vitamin_A_DV',
    'Vitamin C (% DV)': 'Vitamin_C_DV',
    ' Calcium (% DV) ': 'calcium_DV',
    'Iron (% DV) ': 'iron_DV',
    'Caffeine (mg)': 'caffeine_mg'}, inplace=True
         )
         '''

# Display the columns in the DataFrame
print(df.columns)

df['Beverage_category'].value_counts().plot(kind='bar', color='violet')
plt.show()

# Distribution of calories using a histogram
plt.figure(figsize=(10, 6))
sns.histplot(df['Calories'], bins=40, kde=True, color='pink')
plt.title('Distribution of Calories in Starbucks beverages')
plt.xlabel('Calories')
plt.ylabel('Frequency')
plt.show()

# Distribution of Sugars (g) using a histogram
plt.figure(figsize=(10, 4))
sns.histplot(df[' Sugars (g)'], bins=30, kde=True, color='magenta')
plt.title('Distribution of Sugars (g)')
plt.ylabel(' Sugars (g)')
plt.xlabel('Frequency')
plt.show()

# Explore the relationship between 'Total Carbohydrates' and 'Sugars' using a scatter plot
plt.figure(figsize=(10, 6))
sns.scatterplot(x=' Total Carbohydrates (g) ', y=' Sugars (g)', data=df, color='red')
plt.title('Relationship between Total Carbohydrates and Sugars')
plt.xlabel(' Total Carbohydrates (g) ')
plt.ylabel(' Sugars (g)')
plt.show()

# Explore the distribution of beverages across different categories

plt.figure(figsize=(12, 6))
sns.countplot(x='Beverage_category', data=df, color='maroon')
plt.title('Distribution of Beverages across Categories')
plt.xlabel('beverage Category')
plt.ylabel('Count')
plt.xticks(rotation=15, ha='right')
plt.show()

numeric_columns = df.select_dtypes(include='number')
# Create a correlation Heatmap
plt.figure(figsize=(12, 6))
sns.heatmap(numeric_columns.corr(), annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Heatmap')
plt.show()


# Distribution of nutritional components for different beverage categories
plt.figure(figsize=(12, 6))
sns.boxplot(x='Beverage_category', y='Calories', data=df, color='red')
plt.title('Calories Distribution Across Beverage Categories')
plt.xlabel('Beverage Category')
plt.ylabel('Calories')
plt.xticks(rotation=10, ha='right')
plt.show()

df.boxplot(column=[' Sugars (g)'])
plt.show()

# Relationships between many numerical variables
sns.pairplot(df[['Calories', ' Total Carbohydrates (g) ', ' Total Fat (g)', 'Cholesterol (mg)']])
plt.suptitle('Pair Plot of Nutritional Components')
plt.show()

# Top n beverages based on Calories
top_n = 10
top_calories = df.nlargest(top_n, 'Calories')

plt.figure(figsize=(10, 6))
sns.barplot(x='Calories', y='Beverage', data=top_calories, color='green')
plt.title(f'Top {top_n} Beverages with Highest Calories')
plt.xlabel('Calories')
plt.ylabel('Beverage')
plt.yticks(rotation=10, ha='right')
plt.show()

# Top n beverages based on Sugars
top_n = 10
top_sugars = df.nlargest(top_n, ' Sugars (g)')

plt.figure(figsize=(10, 6))
sns.barplot(x=' Sugars (g)', y='Beverage', data=top_calories, color='yellow')
plt.title(f'Top {top_n} Beverages with Highest Sugars')
plt.xlabel(' Sugars (g)')
plt.ylabel('Beverage')
plt.yticks(rotation=10, ha='right')
plt.show()

# Top n beverages based on Total Carbohydrates
top_n = 10
top_carbohydrates = df.nlargest(top_n, ' Total Carbohydrates (g) ')

plt.figure(figsize=(10, 6))
sns.barplot(x=' Total Carbohydrates (g) ', y='Beverage', data=top_carbohydrates, color='gold')
plt.title(f'Top {top_n} Beverages with Highest Carbohydrates')
plt.xlabel(' Total Carbohydrates (g) ')
plt.ylabel('Beverage')
plt.yticks(rotation=10, ha='right')
plt.show()





