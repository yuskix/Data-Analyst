#!/usr/bin/env python
# coding: utf-8

# # Project: Investigate a Dataset - TMDB Movie Dataset
# 
# ## Table of Contents
# <ul>
# <li><a href="#intro">Introduction</a></li>
# <li><a href="#wrangling">Data Wrangling</a></li>
# <li><a href="#eda">Exploratory Data Analysis</a></li>
# <li><a href="#conclusions">Conclusions</a></li>
# </ul>

# <a id='intro'></a>
# ## Introduction
# I picked TMDb movies dataset for my product. This dataset contains information about 10,000 movies collected from The Movie Database (TMDb), including user ratings and revenue, etc. It consists 10866 rows and 21 columns. 
# 
# ### Questions
#     1. Which year release most movies? 
#     2. Which movie gain most profit, and which movie lose most?
#     3. Which movie has highest budget, and which movie has least?
#     4. Find top 10 most popular movies.
#     5. Find the longest moive and the shortest moive.
#     6. How does popularity depends on profit?
#     7. Which genres are most popular from year to year?
#     8. Top 10 production companies with high release.
#     9. Dataset Analysis Based on Histogram.

# In[207]:


# Use this cell to set up import statements for all of the packages that you
#   plan to use.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns
import datetime as dt
sns.set_style('darkgrid')

# Remember to include a 'magic word' so that your visualizations are plotted
#   inline with the notebook. See this page for more:
#   http://ipython.readthedocs.io/en/stable/interactive/magics.html


# <a id='wrangling'></a>
# ## Data Wrangling
# 
# > In this session, I will load data and get an overrall sense about the size of the dataset. I will only keep those relevant data for analysis, and delete the un-used, null, duplicated, and zero values data so that they won't affect my analysis. 
# 
# ### General Properties

# In[208]:


# Load your data and print out a few lines. Perform operations to inspect data
#   types and look for instances of missing or possibly errant data.
df=pd.read_csv('tmdb-movies.csv')
df.head(1)


# In[209]:


df.shape


# ### Data Cleaning - Null Values, Duplicated Data, Extraneous Columns
# 
# 1. Drop columns with null values and irrevelent data, such as 'imdb_id','homepage', 'tagline','keywords', 'overview','budget_adj','revenue_adj'.
# 2. Drop all duplicated data.
# 3. Replace those columns, such as budget, revenue and runtime, that contain zero values with 'null'.
# 4. Change release date data type from string to datetime.

# In[210]:


#1 Unused, Null
df.info()


# In[211]:


df.isnull().sum()


# In[212]:


col=['imdb_id','homepage','keywords', 'tagline', 'overview','budget_adj',
    'revenue_adj']
df.drop(col,axis=1,inplace=True)


# In[213]:


df.shape


# In[214]:


#2 Duplicated
sum(df.duplicated())


# In[215]:


df.drop_duplicates(inplace=True)


# In[216]:


df.shape


# In[217]:


df.isnull().sum()


# In[218]:


na_columns=['cast','director','genres']
df.dropna(subset=na_columns, inplace=True)


# In[219]:


df.isnull().sum()


# In[220]:


df.shape


# In[221]:


#3 Zeros
df_budget=df.query('budget==0')
df_revenue=df.query('revenue==0')
df_runtime=df.query('runtime==0')


# In[222]:


df_budget.head(1)


# In[223]:


df_revenue.head(1)


# In[224]:


df_runtime.head(1)


# In[225]:


df_budget['budget'].value_counts()


# In[226]:


df_revenue['revenue'].value_counts()


# In[227]:


df_runtime['runtime'].value_counts()


# In[228]:


df['budget']=df['budget'].replace(0,np.nan)


# In[229]:


df['revenue']=df['revenue'].replace(0,np.nan)


# In[230]:


df['runtime']=df['runtime'].replace(0,np.nan)


# In[231]:


# to check row 30 budget cell become null
df.head(35)


# In[232]:


df.info()


# In[233]:


#drop all null values
df.dropna(inplace=True)


# In[234]:


df.info()


# In[235]:


#4 change release date data type
df['release_date']=pd.to_datetime(df['release_date'])


# In[236]:


df.head(1)


# In[237]:


df.describe()


# <a id='eda'></a>
# ## Exploratory Data Analysis

# ### 1. Which year releases most movies?

# In[238]:


movie_year=df.groupby('release_year').count()['id']
movie_year.plot(kind='bar',figsize=(15,10))
plt.title('Years vs Number of Movies')
plt.xlabel('Release Year',fontsize=12)
plt.ylabel('Number of Movies',fontsize=12)


# In[239]:


movie_year.max()


# # Conclusion: 
# 2011 release 196 number of movies, which is the most.

# ### 2. Which movie gain most profit, and which movie lose most?

# In[240]:


df['profit']=df['revenue']-df['budget']


# In[241]:


def df_find(x):
    low_index=df[x].idxmin()
    high_index=df[x].idxmax()
    
    low=pd.DataFrame(df.loc[low_index,:])
    high=pd.DataFrame(df.loc[high_index,:])
    
    data=pd.concat([high,low],axis=1)
    
    return data
    
df_find('profit')


# #### Conclusion:
#  Highest profit: Avatar with $2.54 billions profit
#  Lowest profit: The Warrior's Way, loss 413 millions.

# ### 3. Which movie has highest budget, and which movie has least?

# In[242]:


df_find('budget')


# #### Conclusion:
#  Highest budget: The Warrior's Way has 425 millions budget.
#  Lowest budget: Fear Clinic only has $1 budget.

# ### 4. Find top 10 most popular movies.

# In[243]:


pop_movie=pd.DataFrame(df['popularity'].sort_values(ascending=False))
pop_movie['original_title']=df['original_title']
info_movie=list(map(str,(pop_movie['original_title'])))
x=list(info_movie[:10])
y=list(pop_movie['popularity'][:10])

ax = sns.pointplot(x=y,y=x)

sns.set(rc={'figure.figsize':(15,10)})

ax.set_title("Top 10 Popular Movies",fontsize = 12)
ax.set_xlabel("Popularity",fontsize = 12)


# #### Conclusion:
# Jurassic World was the most popular movie among the years.

# ### 5. Find longest moive and shortest moive.

# In[244]:


df_find('runtime')


# In[ ]:





# #### Conclusion:
#  Carlos was the longest movie. It has 338 mins.
#  Kid's Story was the shortest. It only has 15 mins.

# ### 6. How does popularity depends on profit?

# In[254]:


ax = sns.regplot(x=df['popularity'],y=df['profit'])

ax.set_title('Popularity Vs Profit',fontsize=12)
ax.set_xlabel('Popularity',fontsize=12)
ax.set_ylabel('Profit',fontsize=12)

sns.set(rc={'figure.figsize':(15,10)})

df.corr().loc['popularity','profit']


# #### Conclusion:
#  Popularity and profit has a positive correlation (0.595), which indicates movies with high popularity tend to produce more profit.

# ###  7. Which genres are most popular from year to year?

# In[246]:


df.describe()


# In[247]:


# From last question, since popularity and profit has a positive correlation. 
# Therefore, we select the movies having profit $70.5M or more, which can also represent the entire dataset on popularity.
profit_info = df[df['profit'] >= 70500000]

profit_info.index = range(len(profit_info))

profit_info.index = profit_info.index + 1

profit_info.head(2)


# In[248]:


def gen_cat(column):
    gen_cat = profit_info[column].str.cat(sep = '|')
    
    gen_cat = pd.Series(gen_cat.split('|'))
    
    count = gen_cat.value_counts(ascending = False)
    
    return count


# In[249]:


count = gen_cat('genres')

count.head()


# In[250]:


count.sort_values(ascending = True, inplace = True)

gen=count.plot(kind= 'barh',figsize=(15, 10))

gen.set(title = 'Popular Genres')

gen.set_xlabel('Number of Movies', fontsize = '12')

plt.show()


# #### Conclusion:
# There are total 386 comedy had been released. Comedy is the most popular genres. 

# ###  8. Top 10 production companies with high release.

# In[251]:


pro_comp=gen_cat('production_companies')

pro_comp.iloc[:10].plot(kind='barh',figsize=(15,10),fontsize=12)
plt.title("Number Of Movies vs Production Companies",fontsize=12)
plt.xlabel('Number Of Movies',fontsize=12)


# ### 9. Dataset Analysis Based on Histogram.

# In[252]:


df.hist()


# #### Conclusion:
# The market starts to produce more movies after 2000.
# Majority movies have a runtime around 100 mins.
# Average vote is around 6.2.

# #### Conclusion:
# Universal Pictures releases most movies.

# <a id='conclusions'></a>
# ## Conclusions
# 
# 1. 2011 release 196 number of movies, which is the most.
# 2. Avatar gain 2.54 billions profit, which is the highest. The Warrior's Way loss 413 millions.
# 3. The Warrior's Way has 425 millions budget, which is the most. Fear Clinic only has 1 budget.
# 4. Jurassic World was the most popular movie among the years.
# 5. Carlos was the longest movie. It has 338 mins. Kid's Story was the shortest. It only has 15 mins.
# 6. Popularity and profit has a positive correlation (0.595), which indicates movies with high popularity tend to produce more profit.
# 7. There are total 386 comedy had been released over the years. Comedy is the most popular genres.
# 8. Universal Pictures releases most movies.
# 9. The market starts to produce more movies after 2000. Majority movies have a runtime around 100 mins. Average vote is around 6.2.
# 
# ### Limitations
# 1. During the data cleaning process, there are large amount of zero values in the budget and revenue columns. I choose to drop them. This might affect the final results. However, if keep those zero values and null values in the data, it will lead to wrong predications or biased analysis.
# 2. The entire dataset does not have units in it. It might be possible different moives have budget,revenue and profit in different currency; different movies have runtime in minutes or hours, etc. This could be lead to a big issue in the analysis.

# In[255]:


from subprocess import call
call(['python', '-m', 'nbconvert', 'Investigate_a_Dataset.ipynb'])


# In[ ]:




