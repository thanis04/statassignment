#!/usr/bin/env python
# coding: utf-8

# # Task 1: Become familiar with the dataset

# In[ ]:


import pandas as pd


# In[ ]:


data=pd.read_csv('C:\\Users\\Thanis\\Desktop\\BostonHousing.csv')


# In[25]:


data.head(20)


# In[ ]:


medv=data['medv']
medv.head()


# In[ ]:


data['crim'].head()


# In[ ]:


data['crim'].describe()


# In[ ]:


data['zn'].describe()


# In[ ]:


data['indus'].describe()


# In[ ]:


data['chas'].describe()


# In[ ]:


data['nox'].describe()


# In[ ]:


data['rm'].describe()


# In[ ]:


data['age'].describe()


# # Task 2: Generate Descriptive Statistics and Visualizations

# In[32]:


import matplotlib.pyplot as plt
import seaborn as sns


# In[22]:


plt.boxplot(medv)
plt.title('boxplot of medv')
plt.show()


# In[27]:


categories=['chas']
values=[0]

plt.bar(categories, values)
plt.title('barplot of chas')
plt.show()


# In[38]:


age_levels = [0, 35, 70, float('inf')]
age_labels = ['35 years and younger', 'Between 35 and 70 years', '70 years and older']

data['age_group'] = pd.cut(data['age'], bins=age_levels, labels=age_labels, right=False)

plt.figure(figsize=(10, 6))
sns.boxplot(x='age_group', y='medv', data=data)

plt.title('Boxplot of medv by age_group')
plt.xlabel('age group')
plt.ylabel('medv')


# In[41]:


plt.scatter(data['nox'], data['indus'])
plt.title('Relationship between Nitric oxide concentrations and the proportion of non-retail business acres per town')
plt.xlabel('nox')
plt.ylabel('indus')
plt.show()


# In[43]:


plt.hist(data['ptratio'], bins=5)
plt.title('Histogram of ptratio')
plt.show()


# # Task 3

# # T-test for independent samples

# Null Hypothesis : There is no significant difference in the median value of houses bounded by the Charles River and those not bounded by the river
# 
# Alternative Hypothesis : There is a significant difference in the median value of houses bounded by the Charles River and those not bounded by the river

# In[44]:


import pandas as pd
from scipy.stats import ttest_ind

river_bounded = data[data['chas'] == 1]['medv']
not_river_bounded = data[data['chas'] == 0]['medv']

t_statistic, p_value = ttest_ind(river_bounded, not_river_bounded)

print("T-statistic:", t_statistic)
print("P-value:", p_value)

alpha = 0.05
if p_value < alpha:
    print("Reject the null hypothesis: There is a significant difference in median values.")
else:
    print("Fail to reject the null hypothesis: There is no significant difference in median values.")


# # ANOVA

# Null Hypothesis : There is no significant difference in median values of houses for each proportion of owner-occupied units built prior to 1940
# 
# Alternative Hypothesis : There is a significant difference in median values of houses for at least one proportion of owner-occupied units built prior to 1940

# In[45]:


import pandas as pd
from scipy.stats import f_oneway

result = f_oneway(data[data['age'] <= 35]['medv'],
                  data[(data['age'] > 35) & (data['age'] <= 70)]['medv'],
                  data[data['age'] > 70]['medv'])

print("F-statistic:", result.statistic)
print("P-value:", result.pvalue)

alpha = 0.05
if result.pvalue < alpha:
    print("Reject the null hypothesis: There is a significant difference in median values across the groups.")
else:
    print("Fail to reject the null hypothesis: There is no significant difference in median values across the groups.")


# # Pearson Correlation

# Null Hypothesis : There is no relationship between Nitric oxide concentrations and the proportion of non-retail business acres per town
# 
# Alternative Hypothesis : There is a relationship between Nitric oxide concentrations and the proportion of non-retail business acres per town

# In[46]:


import pandas as pd
from scipy.stats import pearsonr

correlation_coefficient, p_value = pearsonr(data['nox'], data['indus'])

print("Pearson correlation coefficient:", correlation_coefficient)
print("P-value:", p_value)

alpha = 0.05
if p_value < alpha:
    print("Reject the null hypothesis: There is a significant relationship between NOX and INDUS.")
else:
    print("Fail to reject the null hypothesis: There is no significant relationship between NOX and INDUS.")


# # Regression analysis

# Null Hypothesis : The weighted distance to the five Boston employment centers does not have a significant impact on the median value of owner-occupied homes
# 
# Alternative Hypothesis : The weighted distance to the five Boston employment centers has a significant impact on the median value of owner-occupied homes

# In[47]:


import pandas as pd
import statsmodels.api as sm

X = data['dis']  
y = data['medv'] 

X = sm.add_constant(X)

model = sm.OLS(y, X).fit()

print(model.summary())


# In[ ]:




