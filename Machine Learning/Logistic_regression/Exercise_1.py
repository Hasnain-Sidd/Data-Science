import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

path="C:\\Users\\PMLS\\Desktop\\Data_Sets\\HR_comma_sep.csv"
df=pd.read_csv(path)
print(df.head())
#plt.scatter(df['satisfaction_level'],df['left'],marker="+",color='red')
#plt.bar(df['Department'],df['salary'],width=0.3)
#plt.hist(df['Department'],bins=10,rwidth=0.95)
#bins = [-0.5, 0.5, 1.5, 2.5]
#plt.hist(df['salary'],bins=bins,width=0.3)
plt.bar(df['Department'],df['left'],width=0.3)
plt.xlabel('Department')
plt.ylabel('Left')
plt.show()