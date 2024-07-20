import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns
import statsmodels.api as sm
import math as mt
from sklearn.metrics import mean_squared_error as msc

df=pd.read_excel("C:\\Users\\PMLS\\Desktop\\Data_Sets\\Big_Mac.xlsx")
model=sm.OLS.from_formula("hourly_wages_usd ~ big_mac_prices",data=df).fit()
net_hourly_wages=-4.5397+4.7435*df['big_mac_prices']
sns.relplot(x=df['big_mac_prices'],y=df['hourly_wages_usd'],data=df,kind='scatter',s=60)
plt.plot(df['big_mac_prices'],net_hourly_wages,'r-')

ssr=np.sum(np.square((net_hourly_wages-net_hourly_wages.mean())))
sse=np.sum(np.square((net_hourly_wages-df['hourly_wages_usd'].values)))
df_ssr=1
df_sse=25
F_Statistics=((ssr/df_ssr)/(sse/df_sse))
print("F Statistisc Value:",F_Statistics)
sst=sse+ssr
R_Square=(1-(sse/sst))
print("Strenght of the Model is:",R_Square*100,"%")
Net_hourly_Wages=-4.5397+4.7435*3
print("Net Hourly Wages of the $3 Big Mac Price:",Net_hourly_Wages)
print(df.corr())

#print(model.summary())
#plt.show()
