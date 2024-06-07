import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt

file_Path="C:\\Users\\PMLS\\Documents\\Stats.txt"
Path="C:\\Users\\PMLS\\Downloads\\annual-enterprise-survey-2021-financial-year-provisional-csv.csv"
try:
    data1=np.loadtxt(file_Path,dtype="str")# Suit for data set that does not have any missing value 
    data=np.genfromtxt(Path, delimiter=";",dtype="str",skip_header=True) # suit for data set that may have some missing values 
    df=pd.DataFrame(data)
    df1=pd.DataFrame(data1)
    
    x1=df1[5]
    x2=df1[7]
    print(df.head(10))
    #print(df1)
    #plt.hist(x1,bins=10)
    #plt.scatter(x1,x2,s=8,c='red')
    #plt.show()

except Exception as e:
    print(e)
