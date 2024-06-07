import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns

def Manipulation_Data(path):
    df=pd.read_csv(path,encoding='unicode_escape')
    print(df.head())
    df.drop(["Status","unnamed1"],axis=1,inplace=True)
    print(df.info())
    df.dropna(inplace=True)
    print(pd.isnull(df).sum())
    df["Amount"]=df["Amount"].astype('int')
    print(df.info())
def Data_Analysis(path):
    df=pd.read_csv(path,encoding='unicode_escape')
    colors=['blue','brown']
    df.drop(["Status","unnamed1"],axis=1,inplace=True)
    df.dropna(inplace=True)
    df["Amount"]=df["Amount"].astype('int')
    #Gender=sns.countplot(x='Gender',data=df,palette=colors,width=0.4)
    #for bars in Gender.containers:
     #   Gender.bar_label(bars)
    
    sales_gen=df.groupby(['Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)
    sns.barplot(x=df['Gender'], y=df["Amount"], data=sales_gen,width=0.4)
    plt.show()


    



path="C:\\Users\\PMLS\\Downloads\\Python_Diwali_Sales_Analysis-main\\Python_Diwali_Sales_Analysis-main\\Diwali_Sales_Data.csv"
#Manipulation_Data(path=path)
Data_Analysis(path=path)